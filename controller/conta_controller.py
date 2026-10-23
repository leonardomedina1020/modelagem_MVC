from model.cliente import Cliente
from model.conta import Conta


class ContaController:
    """Intermedeia a comunicação entre a View e o Model, coordenando as regras e o fluxo de dados."""

    def __init__(self, banco_dados, view):
        self.banco_dados = banco_dados
        self.view = view
        # Vincula o controller à view para responder aos eventos da interface gráfica
        self.view.definir_controller(self)

    def criar_conta(self):
        """Coordena a criação de uma nova conta bancária com base nas entradas da interface gráfica."""
        dados = self.view.obter_dados_conta()
        if not dados:
            return

        nome, cpf, saldo_str = dados

        # Validação: Nome não pode ser vazio
        if not nome:
            self.view.mostrar_mensagem("O nome não pode ficar em branco.", tipo="erro")
            return

        # Validação: CPF não pode ser vazio
        if not cpf:
            self.view.mostrar_mensagem("O CPF não pode ficar em branco.", tipo="erro")
            return

        # Validação: Saldo inicial não pode ser vazio
        if not saldo_str:
            self.view.mostrar_mensagem("O saldo inicial não pode ficar em branco.", tipo="erro")
            return

        # Validação: Entrada de saldo deve ser um valor numérico válido
        try:
            saldo = float(saldo_str.replace(",", "."))
        except ValueError:
            self.view.mostrar_mensagem("Valor inválido! Digite um número válido para o saldo.", tipo="erro")
            return

        # Validação de regra de negócio: Impedir saldo negativo
        if saldo < 0:
            self.view.mostrar_mensagem("Erro: O saldo inicial não pode ser negativo.", tipo="erro")
            return

        # Validação de regra de negócio: Impedir CPF duplicado
        if self.banco_dados.buscar(cpf) is not None:
            self.view.mostrar_mensagem("Erro: Já existe uma conta cadastrada com este CPF.", tipo="erro")
            return

        # Instanciação dos objetos de domínio (Model)
        cliente = Cliente(nome, cpf)
        conta = Conta(cliente, saldo)

        # Armazenamento no banco de dados em memória
        self.banco_dados.salvar(conta)

        # Notificação e exibição dos dados na interface gráfica
        self.view.mostrar_mensagem("Conta criada com sucesso!", tipo="sucesso")
        self.view.mostrar_conta(conta)
        self.view.limpar_campos_cadastro()

    def consultar_conta(self):
        """Coordena a busca e exibição de dados de uma conta através do CPF informado."""
        cpf = self.view.obter_cpf_consulta()

        # Validação: CPF de consulta não pode ser vazio
        if not cpf:
            self.view.mostrar_mensagem("O CPF não pode ficar em branco.", tipo="erro")
            return

        # Consulta no banco de dados
        conta = self.banco_dados.buscar(cpf)

        if conta is not None:
            # Exibe os dados da conta encontrada na interface gráfica
            self.view.mostrar_conta(conta)
            self.view.mostrar_mensagem("Conta localizada com sucesso!", tipo="sucesso")
        else:
            # Limpa dados exibidos e avisa visualmente sobre conta não encontrada
            self.view.limpar_dados_conta()
            self.view.mostrar_mensagem("Conta não encontrada para o CPF informado.", tipo="erro")
