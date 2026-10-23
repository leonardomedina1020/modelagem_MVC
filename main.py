from model.banco_dados import BancoDados
from view.conta_view import ContaView
from controller.conta_controller import ContaController


def main():
    # Inicialização dos componentes da arquitetura MVC
    banco_dados = BancoDados()
    view = ContaView()
    controller = ContaController(banco_dados, view)

    # Loop principal da aplicação
    while True:
        try:
            opcao = view.mostrar_menu()

            if opcao == "1":
                controller.criar_conta()
            elif opcao == "2":
                controller.consultar_conta()
            elif opcao == "3":
                view.mostrar_mensagem("Encerrando o sistema. Até logo!")
                break
            else:
                view.mostrar_mensagem("Opção inválida! Escolha 1, 2 ou 3.")
        except (KeyboardInterrupt, EOFError):
            view.mostrar_mensagem("\nPrograma finalizado pelo usuário.")
            break
        except Exception as erro:
            view.mostrar_mensagem(f"Ocorreu um erro inesperado: {erro}")


if __name__ == "__main__":
    main()
