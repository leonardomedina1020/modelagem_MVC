from model.cliente import Cliente
from model.conta import Conta


class ContaController:
    """Intermedeia a comunicação entre a View e o Model."""

    def __init__(self, banco_dados, view):
        self.banco_dados = banco_dados
        self.view = view

    def criar_conta(self):
        """Recebe dados da View, valida regras de negócio, cria a conta e solicita exibição."""
        # 1. Receber os dados da View
        nome, cpf, saldo = self.view.solicitar_dados_conta()

        # Validação de regra de negócio: Impedir CPF duplicado
        if self.banco_dados.buscar(cpf) is not None:
            self.view.mostrar_mensagem("Erro: Já existe uma conta cadastrada com este CPF.")
            return

        # Validação de regra de negócio: Impedir saldo negativo
        if saldo < 0:
            self.view.mostrar_mensagem("Erro: O saldo inicial não pode ser negativo.")
            return

        # 2. Instanciar Cliente e Conta
        cliente = Cliente(nome, cpf)
        conta = Conta(cliente, saldo)

        # 3. Salvar a conta no BancoDados
        self.banco_dados.salvar(conta)

        # 4. Solicitar à View a exibição da conta criada
        self.view.mostrar_mensagem("Conta criada com sucesso!")
        self.view.mostrar_conta(conta)

    def consultar_conta(self):
        """Permite consultar uma conta pelo CPF e exibi-la via View."""
        cpf = self.view.solicitar_cpf()
        conta = self.banco_dados.buscar(cpf)

        if conta is not None:
            self.view.mostrar_conta(conta)
        else:
            self.view.mostrar_mensagem("Conta não encontrada para o CPF informado.")
