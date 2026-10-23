class Conta:
    """Representa a conta bancária associada a um cliente com saldo."""

    def __init__(self, cliente, saldo: float = 0.0):
        self.cliente = cliente
        self.saldo = saldo
