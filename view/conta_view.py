class ContaView:
    """Responsável pela interação com o usuário no terminal (entrada e saída)."""

    def mostrar_menu(self) -> str:
        print("\n" + "=" * 30)
        print("       SISTEMA BANCÁRIO       ")
        print("=" * 30)
        print("1. Criar conta")
        print("2. Consultar conta")
        print("3. Sair")
        print("=" * 30)
        return input("Escolha uma opção: ").strip()

    def solicitar_dados_conta(self):
        """Solicita os dados para abertura de conta com validação de entrada."""
        print("\n--- Abertura de Conta ---")

        nome = input("Informe o nome: ").strip()
        while not nome:
            print("O nome não pode ficar em branco.")
            nome = input("Informe o nome: ").strip()

        cpf = input("Informe o CPF: ").strip()
        while not cpf:
            print("O CPF não pode ficar em branco.")
            cpf = input("Informe o CPF: ").strip()

        # Validação do saldo inicial para aceitar apenas valores numéricos e não negativos
        while True:
            entrada_saldo = input("Informe o saldo inicial: ").strip()
            try:
                saldo = float(entrada_saldo.replace(",", "."))
                if saldo < 0:
                    print("O saldo inicial não pode ser negativo. Tente novamente.")
                    continue
                return nome, cpf, saldo
            except ValueError:
                print("Valor inválido! Digite um número válido para o saldo.")

    def solicitar_cpf(self) -> str:
        """Solicita o CPF para consulta."""
        print("\n--- Consulta de Conta ---")
        cpf = input("Informe o CPF da conta: ").strip()
        while not cpf:
            print("O CPF não pode ficar em branco.")
            cpf = input("Informe o CPF da conta: ").strip()
        return cpf

    def mostrar_conta(self, conta):
        """Exibe de forma formatada os dados da conta."""
        print("\n" + "-" * 30)
        print("      DADOS DA CONTA          ")
        print("-" * 30)
        print(f"Titular: {conta.cliente.nome}")
        print(f"CPF:     {conta.cliente.cpf}")
        print(f"Saldo:   R$ {conta.saldo:.2f}")
        print("-" * 30)

    def mostrar_mensagem(self, mensagem: str):
        """Exibe mensagens informativas ou de erro para o usuário."""
        print(f"\n{mensagem}")
