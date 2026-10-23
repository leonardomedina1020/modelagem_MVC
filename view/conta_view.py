import tkinter as tk
from tkinter import ttk, messagebox


class ContaView:
    """Responsável pela interface gráfica com o usuário utilizando Tkinter."""

    def __init__(self, root=None):
        # Configuração da janela principal
        if root is None:
            self.root = tk.Tk()
        else:
            self.root = root

        self.root.title("Sistema Bancário - MVC")
        self.root.geometry("480x570")
        self.root.minsize(450, 530)

        # Referência ao controller para coordenação das ações
        self.controller = None

        # Configurar estilos visuais e criar os componentes da interface
        self._configurar_estilos()
        self._criar_componentes()

    def definir_controller(self, controller):
        """Vincula o controller que responderá aos eventos da interface gráfica."""
        self.controller = controller

    def _configurar_estilos(self):
        """Define estilos visuais modernos e limpos usando ttk."""
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure("Header.TLabel", font=("Segoe UI", 14, "bold"), foreground="#1a365d")
        self.style.configure("Subheader.TLabel", font=("Segoe UI", 9), foreground="#4a5568")
        self.style.configure("Nav.TButton", font=("Segoe UI", 10, "bold"), padding=6)
        self.style.configure("Action.TButton", font=("Segoe UI", 10, "bold"), padding=6)
        self.style.configure("DataTitle.TLabel", font=("Segoe UI", 10, "bold"), foreground="#2d3748")
        self.style.configure("DataValue.TLabel", font=("Segoe UI", 10), foreground="#1a202c")

    def _criar_componentes(self):
        """Cria e organiza todos os widgets da interface gráfica."""
        # --- CABEÇALHO ---
        frame_cabecalho = ttk.Frame(self.root, padding="15 10 15 5")
        frame_cabecalho.pack(fill="x")

        lbl_titulo = ttk.Label(
            frame_cabecalho,
            text="SISTEMA BANCÁRIO",
            style="Header.TLabel",
            anchor="center",
        )
        lbl_titulo.pack(fill="x")

        lbl_subtitulo = ttk.Label(
            frame_cabecalho,
            text="Arquitetura MVC — Interface Gráfica Tkinter",
            style="Subheader.TLabel",
            anchor="center",
        )
        lbl_subtitulo.pack(fill="x")

        ttk.Separator(self.root, orient="horizontal").pack(fill="x", padx=15, pady=5)

        # --- MENU DE OPÇÕES (Criar Conta, Consultar Conta, Sair) ---
        frame_menu = ttk.LabelFrame(self.root, text=" Menu de Opções ", padding=10)
        frame_menu.pack(fill="x", padx=15, pady=5)

        self.btn_nav_criar = ttk.Button(
            frame_menu,
            text="Criar Conta",
            style="Nav.TButton",
            command=self.mostrar_tela_criar,
        )
        self.btn_nav_criar.pack(side="left", expand=True, fill="x", padx=3)

        self.btn_nav_consultar = ttk.Button(
            frame_menu,
            text="Consultar Conta",
            style="Nav.TButton",
            command=self.mostrar_tela_consultar,
        )
        self.btn_nav_consultar.pack(side="left", expand=True, fill="x", padx=3)

        self.btn_nav_sair = ttk.Button(
            frame_menu,
            text="Sair",
            style="Nav.TButton",
            command=self.fechar,
        )
        self.btn_nav_sair.pack(side="left", expand=True, fill="x", padx=3)

        # --- ÁREA DINÂMICA DE FORMULÁRIOS ---
        self.frame_conteudo = ttk.Frame(self.root, padding=5)
        self.frame_conteudo.pack(fill="x", padx=15, pady=5)

        # 1. Formulário de Criação de Conta
        self.frame_criar = ttk.LabelFrame(self.frame_conteudo, text=" Abertura de Conta ", padding=10)

        lbl_nome = ttk.Label(self.frame_criar, text="Nome do Titular:")
        lbl_nome.pack(anchor="w", pady=(2, 0))
        self.entry_nome = ttk.Entry(self.frame_criar, font=("Segoe UI", 10))
        self.entry_nome.pack(fill="x", pady=(0, 6))

        lbl_cpf = ttk.Label(self.frame_criar, text="CPF:")
        lbl_cpf.pack(anchor="w", pady=(2, 0))
        self.entry_cpf = ttk.Entry(self.frame_criar, font=("Segoe UI", 10))
        self.entry_cpf.pack(fill="x", pady=(0, 6))

        lbl_saldo = ttk.Label(self.frame_criar, text="Saldo Inicial (R$):")
        lbl_saldo.pack(anchor="w", pady=(2, 0))
        self.entry_saldo = ttk.Entry(self.frame_criar, font=("Segoe UI", 10))
        self.entry_saldo.pack(fill="x", pady=(0, 8))

        self.btn_cadastrar = ttk.Button(
            self.frame_criar,
            text="Confirmar Abertura de Conta",
            style="Action.TButton",
            command=self._ao_clicar_criar,
        )
        self.btn_cadastrar.pack(fill="x", pady=4)

        # Atalho: pressionar Enter nos campos aciona o cadastro
        self.entry_nome.bind("<Return>", lambda event: self._ao_clicar_criar())
        self.entry_cpf.bind("<Return>", lambda event: self._ao_clicar_criar())
        self.entry_saldo.bind("<Return>", lambda event: self._ao_clicar_criar())

        # 2. Formulário de Consulta de Conta
        self.frame_consultar = ttk.LabelFrame(self.frame_conteudo, text=" Consulta de Conta ", padding=10)

        lbl_cpf_busca = ttk.Label(self.frame_consultar, text="Informe o CPF para consulta:")
        lbl_cpf_busca.pack(anchor="w", pady=(2, 0))
        self.entry_cpf_consulta = ttk.Entry(self.frame_consultar, font=("Segoe UI", 10))
        self.entry_cpf_consulta.pack(fill="x", pady=(0, 8))

        self.btn_buscar = ttk.Button(
            self.frame_consultar,
            text="Buscar Conta",
            style="Action.TButton",
            command=self._ao_clicar_consultar,
        )
        self.btn_buscar.pack(fill="x", pady=4)

        # Atalho: pressionar Enter no campo de busca aciona a consulta
        self.entry_cpf_consulta.bind("<Return>", lambda event: self._ao_clicar_consultar())

        # --- ÁREA DE EXIBIÇÃO DOS DADOS DA CONTA ---
        self.frame_dados = ttk.LabelFrame(self.root, text=" Dados da Conta ", padding=10)
        self.frame_dados.pack(fill="x", padx=15, pady=5)

        grid_dados = ttk.Frame(self.frame_dados)
        grid_dados.pack(fill="x")

        ttk.Label(grid_dados, text="Titular:", style="DataTitle.TLabel").grid(row=0, column=0, sticky="w", pady=2)
        self.lbl_titular_valor = ttk.Label(grid_dados, text="-", style="DataValue.TLabel")
        self.lbl_titular_valor.grid(row=0, column=1, sticky="w", padx=10, pady=2)

        ttk.Label(grid_dados, text="CPF:", style="DataTitle.TLabel").grid(row=1, column=0, sticky="w", pady=2)
        self.lbl_cpf_valor = ttk.Label(grid_dados, text="-", style="DataValue.TLabel")
        self.lbl_cpf_valor.grid(row=1, column=1, sticky="w", padx=10, pady=2)

        ttk.Label(grid_dados, text="Saldo:", style="DataTitle.TLabel").grid(row=2, column=0, sticky="w", pady=2)
        self.lbl_saldo_valor = ttk.Label(grid_dados, text="-", style="DataValue.TLabel")
        self.lbl_saldo_valor.grid(row=2, column=1, sticky="w", padx=10, pady=2)

        # --- BARRA DE STATUS / MENSAGENS VISUAIS ---
        frame_status = ttk.Frame(self.root, padding="10 5 10 10")
        frame_status.pack(side="bottom", fill="x")

        self.lbl_status = tk.Label(
            frame_status,
            text="Selecione uma opção no menu acima.",
            font=("Segoe UI", 9),
            anchor="w",
            relief="sunken",
            padx=8,
            pady=4,
            bg="#ffffff",
            fg="#4a5568",
        )
        self.lbl_status.pack(fill="x")

        # Exibe a tela de criação por padrão ao iniciar
        self.mostrar_tela_criar()

    # --- NAVEGAÇÃO ENTRE TELAS ---
    def mostrar_tela_criar(self):
        """Exibe o formulário de cadastro e oculta o de consulta."""
        self.frame_consultar.pack_forget()
        self.frame_criar.pack(fill="x")
        self.entry_nome.focus_set()

    def mostrar_tela_consultar(self):
        """Exibe o formulário de consulta e oculta o de cadastro."""
        self.frame_criar.pack_forget()
        self.frame_consultar.pack(fill="x")
        self.entry_cpf_consulta.focus_set()

    def fechar(self):
        """Fecha a janela da aplicação gráfica."""
        self.root.destroy()

    # --- MÉTODOS DE AÇÃO (INTERAÇÃO COM O CONTROLLER) ---
    def _ao_clicar_criar(self):
        """Repassa a solicitação de criação de conta ao Controller."""
        if self.controller:
            self.controller.criar_conta()

    def _ao_clicar_consultar(self):
        """Repassa a solicitação de consulta de conta ao Controller."""
        if self.controller:
            self.controller.consultar_conta()

    # --- MÉTODOS DE OBTENÇÃO DE DADOS ---
    def obter_dados_conta(self):
        """Recupera os dados informados nos campos de cadastro (nome, CPF, saldo)."""
        nome = self.entry_nome.get().strip()
        cpf = self.entry_cpf.get().strip()
        saldo = self.entry_saldo.get().strip()
        return nome, cpf, saldo

    # Alias para manter compatibilidade com métodos anteriores
    solicitar_dados_conta = obter_dados_conta

    def obter_cpf_consulta(self):
        """Recupera o CPF informado no campo de consulta."""
        return self.entry_cpf_consulta.get().strip()

    # Alias para manter compatibilidade com métodos anteriores
    solicitar_cpf = obter_cpf_consulta

    # --- MÉTODOS DE LIMPEZA E EXIBIÇÃO ---
    def limpar_campos_cadastro(self):
        """Limpa os campos de entrada do formulário de criação."""
        self.entry_nome.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_saldo.delete(0, tk.END)
        self.entry_nome.focus_set()

    def limpar_campos_consulta(self):
        """Limpa o campo de entrada do formulário de consulta."""
        self.entry_cpf_consulta.delete(0, tk.END)

    def mostrar_conta(self, conta):
        """Atualiza a seção de dados da conta na interface gráfica com os dados do objeto Conta."""
        self.lbl_titular_valor.config(text=conta.cliente.nome)
        self.lbl_cpf_valor.config(text=conta.cliente.cpf)
        self.lbl_saldo_valor.config(text=f"R$ {conta.saldo:.2f}")

    def limpar_dados_conta(self):
        """Reseta a exibição dos dados da conta para os valores padrão."""
        self.lbl_titular_valor.config(text="-")
        self.lbl_cpf_valor.config(text="-")
        self.lbl_saldo_valor.config(text="-")

    def mostrar_mensagem(self, mensagem: str, tipo: str = "info"):
        """Exibe mensagens visuais para o usuário via barra de status e janela de diálogo (messagebox)."""
        if tipo == "sucesso":
            self.lbl_status.config(text=f"✔ {mensagem}", fg="#155724", bg="#d4edda")
            messagebox.showinfo("Sucesso", mensagem, parent=self.root)
        elif tipo == "erro":
            self.lbl_status.config(text=f"✖ {mensagem}", fg="#721c24", bg="#f8d7da")
            messagebox.showerror("Erro", mensagem, parent=self.root)
        else:
            self.lbl_status.config(text=f"ℹ {mensagem}", fg="#0c5460", bg="#d1ecf1")
            messagebox.showinfo("Informação", mensagem, parent=self.root)

    def iniciar(self):
        """Inicia o loop principal de eventos do Tkinter."""
        self.root.mainloop()
