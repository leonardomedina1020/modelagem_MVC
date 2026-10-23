from model.banco_dados import BancoDados
from view.conta_view import ContaView
from controller.conta_controller import ContaController


def main():
    """Inicializa os componentes da arquitetura MVC e inicia a interface gráfica Tkinter."""
    # Instanciação dos componentes MVC
    banco_dados = BancoDados()
    view = ContaView()
    controller = ContaController(banco_dados, view)

    # Inicia o loop da interface gráfica
    view.iniciar()


if __name__ == "__main__":
    main()
