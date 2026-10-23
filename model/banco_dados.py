class BancoDados:
    """Simula um banco de dados em memória armazenando contas em um dicionário."""

    def __init__(self):
        # Dicionário onde a chave é o CPF do cliente e o valor é o objeto Conta
        self.contas = {}

    def salvar(self, conta):
        """Salva ou atualiza a conta no dicionário usando o CPF do cliente como chave."""
        self.contas[conta.cliente.cpf] = conta

    def buscar(self, cpf: str):
        """Busca e retorna a conta pelo CPF, ou None se não encontrada."""
        return self.contas.get(cpf)
