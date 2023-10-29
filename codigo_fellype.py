from customtkinter import *
from tkinter import messagebox, ttk, Toplevel
import random
import sqlite3
from databse.systems_db import SystemsDb


# Classe principal da aplicação
class App(CTk):
    def __init__(self):
        super().__init__()

        self.layout_config()  # Configura a janela principal
        self.frames = {}  # Dicionário para armazenar os quadros da aplicação
        self.menu_buttons = {}  # Dicionário para armazenar os botões do menu lateral
        self.menu_lateral()  # Cria o menu lateral
        self.frameAtivo = None  # Armazena o quadro ativo

        self.nome_entry = None
        self.codigo_entry = None

        self.matriz()  # Cria o quadro da seção "home"
        self.perfil()  # Cria o quadro da seção "perfil"
        self.sistema()  # Cria o quadro da seção "sistema"
        self.usuario()  # Cria o quadro da seção "usuário"
        self.sobre()  # Cria o quadro da seção "sobre"

        self.show_matriz_frame()  # Exibe o quadro "home" por padrão

        self.update_data_table()  # Inicializar a tabela com dados existentes

        self.systemsdb = SystemsDb()

    # Configurações da janela principal
    def layout_config(self):
        self.title('Escola XYZ')
        self.geometry('910x550')
        self.resizable(width=False, height=False)

        set_appearance_mode('dark')
        set_default_color_theme('blue')

        # Definir estilos personalizados para o Treeview
        style = ttk.Style()
        style.configure('Treeview.Heading', font=('Arial', 10, 'bold'))
        style.configure('Treeview', font=('Arial', 10))
        style.layout('Treeview', [('Treeview.treearea', {'sticky': 'nswe'})])

    # Cria o menu lateral
    def menu_lateral(self):
        frameMenu = CTkFrame(self, width=150, height=500, corner_radius=0)
        frameMenu.place(x=0, y=0)

        btn_nomes = ['matriz', 'perfil', 'sistema', 'usuario', 'sobre']

        for i, btn_nome in enumerate(btn_nomes):
            # Cria os botões do menu
            button = CTkButton(frameMenu, text=btn_nome.capitalize(), font=('Arial', 15, 'bold'),
                               fg_color='transparent', bg_color='transparent', corner_radius=0, width=150, height=50,
                               anchor='w', border_spacing=10,
                               command=lambda b=btn_nome: self.show_frame(b))
            button.place(x=0, y=i * 50)
            self.menu_buttons[btn_nome] = button

    # Mostra o quadro especificado
    def show_frame(self, frame_nome):
        btn_corAtiva = '#3498db'
        btn_corInativa = 'transparent'

        if self.frameAtivo:
            self.frameAtivo.place_forget()

        frame = self.frames[frame_nome]
        frame.place(x=160, y=0)
        self.frameAtivo = frame

        for button_name, button in self.menu_buttons.items():
            if button_name == frame_nome:
                button.configure(fg_color=btn_corAtiva)
            else:
                button.configure(fg_color=btn_corInativa)

    # Exibe o quadro "home"
    def show_matriz_frame(self):
        self.show_frame('matriz')

    # Exibe o quadro "perfil"
    def show_perfil_frame(self):
        self.show_frame('perfil')

    # Exibe o quadro "sistema"
    def show_sistema_frame(self):
        self.show_frame('sistema')

    # Exibe o quadro "usuário"
    def show_usuario_frame(self):
        self.show_frame('usuario')

    # Exibe o quadro "sobre"
    def show_sobre_frame(self):
        self.show_frame('sobre')

    # Cria o quadro da seção "home"
    def matriz(self):
        frameMatriz = CTkFrame(self, fg_color='transparent', width=750, height=500, corner_radius=0)
        self.frames['matriz'] = frameMatriz

        labelTitulo_frame = CTkLabel(frameMatriz, text='M A T R I Z   S O D', font=('Arial', 20))
        labelTitulo_frame.place(x=10, y=10)

    # Cria o quadro da seção "perfil"
    def perfil(self):
        framePerfil = CTkFrame(self, fg_color='transparent', width=750, height=500, corner_radius=0)
        self.frames['perfil'] = framePerfil

        labelTitulo_frame = CTkLabel(framePerfil, text='P E R F I L', font=('Arial', 20))
        labelTitulo_frame.place(x=10, y=10)

        label_nomeSistema = CTkLabel(framePerfil, text='Sistema:')
        label_nomeSistema.place(x=10, y=60)
        self.codigo_comboBox = CTkComboBox(framePerfil, width=200)
        self.codigo_comboBox.place(x=70, y=60)

        label_nome = CTkLabel(framePerfil, text='Nome:')
        label_nome.place(x=10, y=100)
        self.nome_entry = CTkEntry(framePerfil, width=200)
        self.nome_entry.place(x=70, y=100)

        label_descricao = CTkLabel(framePerfil, text='Descrição:')
        label_descricao.place(x=300, y=60)
        self.descricao_entry = CTkTextbox(framePerfil, width=280, height=70, fg_color='#343638', border_width=2, border_color='#565b5e')
        self.descricao_entry.place(x=380, y=60)

        criar_button = CTkButton(framePerfil, text='Criar Cadastro')
        criar_button.place(x=10, y=150)

        # Cria uma tabela para exibir dados
        self.data_table = ttk.Treeview(framePerfil, columns=('Nome', 'Código', 'Ações'), show='headings')
        self.data_table.heading('#1', text='Nome')
        self.data_table.heading('#2', text='Código')
        self.data_table.column('#1', width=300)
        self.data_table.column('#2', width=150)

        # Remover a coluna de índice padrão
        self.data_table['show'] = 'headings'

        self.data_table.place(x=10, y=300)

        label_filtro = CTkLabel(framePerfil, text='Filtro:')
        label_filtro.place(x=10, y=250)

        # Adicione a entrada de texto e o botão de filtro
        self.filtro_entry = CTkEntry(framePerfil, width=300)
        self.filtro_entry.place(x=70, y=250)

        self.filtro_entry.bind('<KeyRelease>', self.filtrar_tabela)


    # Cria o quadro da seção "sistema"
    def sistema(self):
        frameSistema = CTkFrame(self, fg_color='transparent', width=750, height=500, corner_radius=0)
        self.frames['sistema'] = frameSistema

        labelTitulo_frame = CTkLabel(frameSistema, text='S I S T E M A', font=('Arial', 20))
        labelTitulo_frame.place(x=10, y=10)

        label_nome = CTkLabel(frameSistema, text='Nome:')
        label_nome.place(x=10, y=60)
        self.entry_nome = CTkEntry(frameSistema, width=210)
        self.entry_nome.place(x=70, y=60)

        label_codigo = CTkLabel(frameSistema, text='Código:')
        label_codigo.place(x=10, y=100)
        self.entry_codigo = CTkEntry(frameSistema, width=150)
        self.entry_codigo.place(x=70, y=100)

        button_gerarCodigo = CTkButton(frameSistema, text='Gerar', width=50, command=self.gerar_codigo)
        button_gerarCodigo.place(x=230, y=100)

        button_criarSistema = CTkButton(frameSistema, text='Criar Cadastro', command=self.criar_cadastro)
        button_criarSistema.place(x=10, y=150)

        # Cria uma tabela para exibir dados
        self.data_table = ttk.Treeview(frameSistema, columns=('Nome', 'Código', 'Ações'), show='headings')
        self.data_table.heading('#1', text='Nome')
        self.data_table.heading('#2', text='Código')
        self.data_table.column('#1', width=300)
        self.data_table.column('#2', width=150)

        # Remover a coluna de índice padrão
        self.data_table['show'] = 'headings'

        self.data_table.place(x=10, y=300)

        label_filtro = CTkLabel(frameSistema, text='Filtro:')
        label_filtro.place(x=10, y=250)

        # Adicione a entrada de texto e o botão de filtro
        self.entry_filtro = CTkEntry(frameSistema, width=300)
        self.entry_filtro.place(x=70, y=250)

        self.entry_filtro.bind('<KeyRelease>', self.filtrar_tabela)

        # Crie botões para editar e excluir registros
        button_editar = CTkButton(frameSistema, text='Editar', width=50, command=self.editar_registro)
        button_editar.place(x=550, y=250)

        button_excluir = CTkButton(frameSistema, text='Excluir', width=50, command=self.excluir_registro)
        button_excluir.place(x=610, y=250)

    # Cria o quadro da seção "usuário"
    def usuario(self):
        frameUsuario = CTkFrame(self, fg_color='transparent', width=750, height=500, corner_radius=0)
        self.frames['usuario'] = frameUsuario

        labelTitulo_frame = CTkLabel(frameUsuario, text='U S U Á R I O', font=('Arial', 20))
        labelTitulo_frame.place(x=10, y=10)

        label_nomeSistema = CTkLabel(frameUsuario, text='Sistema:')
        label_nomeSistema.place(x=10, y=60)
        self.comboBox_nomeSistema = CTkComboBox(frameUsuario, width=200)
        self.comboBox_nomeSistema.place(x=70, y=60)

        label_nomePerfil = CTkLabel(frameUsuario, text='Perfil:')
        label_nomePerfil.place(x=10, y=100)
        self.comboBox_nomeCodigo = CTkComboBox(frameUsuario, width=200)
        self.comboBox_nomeCodigo.place(x=70, y=100)

        label_nome = CTkLabel(frameUsuario, text='Nome:')
        label_nome.place(x=300, y=60)
        self.entry_nome = CTkEntry(frameUsuario, width=200)
        self.entry_nome.place(x=360, y=60)

        label_cpf = CTkLabel(frameUsuario, text='CPF:')
        label_cpf.place(x=300, y=100)
        self.entry_cpf = CTkEntry(frameUsuario, width=200)
        self.entry_cpf.place(x=360, y=100)

        criar_button = CTkButton(frameUsuario, text='Criar Cadastro')
        criar_button.place(x=10, y=150)

        # Cria uma tabela para exibir dados
        self.data_table = ttk.Treeview(frameUsuario, columns=('Nome', 'Código', 'Ações'), show='headings')
        self.data_table.heading('#1', text='Nome')
        self.data_table.heading('#2', text='Código')
        self.data_table.column('#1', width=300)
        self.data_table.column('#2', width=150)

        # Remover a coluna de índice padrão
        self.data_table['show'] = 'headings'

        self.data_table.place(x=10, y=300)

        label_filtro = CTkLabel(frameUsuario, text='Filtro:')
        label_filtro.place(x=10, y=250)

        # Adicione a entrada de texto e o botão de filtro
        self.filtro_entry = CTkEntry(frameUsuario, width=300)
        self.filtro_entry.place(x=70, y=250)

        self.filtro_entry.bind('<KeyRelease>', self.filtrar_tabela)

    # Cria o quadro da seção "sobre"
    def sobre(self):
        frameSobre = CTkFrame(self, fg_color='transparent', width=750, height=500, corner_radius=0)
        self.frames['sobre'] = frameSobre

        labelTitulo_frame = CTkLabel(frameSobre, text='S O B R E', font=('Arial', 20))
        labelTitulo_frame.place(x=10, y=10)

        label_subTitulo = CTkLabel(frameSobre, text='informações do Projeto:', font=('Arial', 18))
        label_subTitulo.place(x=10, y=60)

        label_textoSimples = CTkLabel(frameSobre, text='Curso:')
        label_textoSimples.place(x=10, y=100)
        label_textoSimples = CTkLabel(frameSobre, text='Desenvolvimento Full Stack')
        label_textoSimples.place(x=80, y=100)

        label_textoSimples = CTkLabel(frameSobre, text='Semestre:')
        label_textoSimples.place(x=10, y=125)
        label_textoSimples = CTkLabel(frameSobre, text='2023.3')
        label_textoSimples.place(x=80, y=125)

        label_textoSimples = CTkLabel(frameSobre, text='Objetivo:')
        label_textoSimples.place(x=10, y=150)
        label_textoSimples = CTkLabel(frameSobre, text='Missão Certificação')
        label_textoSimples.place(x=80, y=150)

        label_textoSimples = CTkLabel(frameSobre, text='Disciplina:')
        label_textoSimples.place(x=10, y=175)
        label_textoSimples = CTkLabel(frameSobre, text='Projetando uma Aplicação Desktop')
        label_textoSimples.place(x=80, y=175)

        label_textoSimples = CTkLabel(frameSobre, text='Professor:')
        label_textoSimples.place(x=10, y=200)
        label_textoSimples = CTkLabel(frameSobre, text='Andre Luiz Avelino Sobral')
        label_textoSimples.place(x=80, y=200)

        label_subTitulo = CTkLabel(frameSobre, text='Equipe:', font=('Arial', 18))
        label_subTitulo.place(x=10, y=250)

        label_textoSimples = CTkLabel(frameSobre, text='Nome:')
        label_textoSimples.place(x=10, y=300)
        label_textoSimples = CTkLabel(frameSobre, text='Nome Número Um')
        label_textoSimples.place(x=80, y=300)
        label_textoSimples = CTkLabel(frameSobre, text='Matricula:')
        label_textoSimples.place(x=10, y=320)
        label_textoSimples = CTkLabel(frameSobre, text='202300000000')
        label_textoSimples.place(x=80, y=320)

        label_textoSimples = CTkLabel(frameSobre, text='Nome:')
        label_textoSimples.place(x=10, y=350)
        label_textoSimples = CTkLabel(frameSobre, text='Nome Número Dois')
        label_textoSimples.place(x=80, y=350)
        label_textoSimples = CTkLabel(frameSobre, text='Matricula:')
        label_textoSimples.place(x=10, y=370)
        label_textoSimples = CTkLabel(frameSobre, text='202300000000')
        label_textoSimples.place(x=80, y=370)

        label_textoSimples = CTkLabel(frameSobre, text='Nome:')
        label_textoSimples.place(x=10, y=400)
        label_textoSimples = CTkLabel(frameSobre, text='Nome Número Três')
        label_textoSimples.place(x=80, y=400)
        label_textoSimples = CTkLabel(frameSobre, text='Matricula:')
        label_textoSimples.place(x=10, y=420)
        label_textoSimples = CTkLabel(frameSobre, text='202300000000')
        label_textoSimples.place(x=80, y=420)

        label_textoSimples = CTkLabel(frameSobre, text='Nome:')
        label_textoSimples.place(x=300, y=300)
        label_textoSimples = CTkLabel(frameSobre, text='Nome Número Quatro')
        label_textoSimples.place(x=370, y=300)
        label_textoSimples = CTkLabel(frameSobre, text='Matricula:')
        label_textoSimples.place(x=300, y=320)
        label_textoSimples = CTkLabel(frameSobre, text='202300000000')
        label_textoSimples.place(x=370, y=320)

        label_textoSimples = CTkLabel(frameSobre, text='Nome:')
        label_textoSimples.place(x=300, y=350)
        label_textoSimples = CTkLabel(frameSobre, text='Nome Número Cinco')
        label_textoSimples.place(x=370, y=350)
        label_textoSimples = CTkLabel(frameSobre, text='Matricula:')
        label_textoSimples.place(x=300, y=370)
        label_textoSimples = CTkLabel(frameSobre, text='202300000000')
        label_textoSimples.place(x=370, y=370)

        label_textoSimples = CTkLabel(frameSobre, text='Nome:')
        label_textoSimples.place(x=300, y=400)
        label_textoSimples = CTkLabel(frameSobre, text='Nome Número Seis')
        label_textoSimples.place(x=370, y=400)
        label_textoSimples = CTkLabel(frameSobre, text='Matricula:')
        label_textoSimples.place(x=300, y=420)
        label_textoSimples = CTkLabel(frameSobre, text='202300000000')
        label_textoSimples.place(x=370, y=420)

    # Gera um código aleatório e insere na entrada de texto
    def gerar_codigo(self):
        # Crie uma conexão com o banco de dados SQLite
        num = random.randint(0, 3)
        sistema_bd = self.systemsdb.search_id(num,)

        while sistema_bd is not None:
            print(f"O número {num} já existe no banco de dados.")
            num = random.randint(1, 3)
            sistema_bd = self.systemsdb.search_id(num, )
        print(f"O número {num} é único e será inserido no banco de dados.")



        self.codigo_entry.delete(0, 'end')
        self.codigo_entry.insert(0, str(num))

    # Criar novo cadastro no banco de dados
    def criar_cadastro(self):
        sistemaNome = self.nome_entry.get().lower().replace(" ", "") # Converte para letras minúsculas e elimina espaços
        sistemaCodigo = self.codigo_entry.get()

        if sistemaNome and sistemaCodigo:
            # Verifique se o nome já existe no banco de dados
            conexao = sqlite3.connect('database.db')
            c = conexao.cursor()

            c.execute("SELECT * FROM sistemas WHERE nome_sistema = ?", (sistemaNome,))
            nome_existente = c.fetchone()

            # Verifique se o código já existe no banco de dados
            c.execute("SELECT * FROM sistemas WHERE cod_sistema = ?", (sistemaCodigo,))
            codigo_existente = c.fetchone()

            # Mensagem de erro padrão
            mensagem = 'Ocorreu algum erro. Tente novamente.'

            if nome_existente:
                mensagem = f'Nome "{sistemaNome}" já está em uso. Tente outro nome.'

            if codigo_existente:
                mensagem = f'Código "{sistemaCodigo}" já está em uso. Tente outro código.\n\n Se desejar, utilize o gerador automatico de código, clicando no botão "Gerar".'

            if nome_existente and codigo_existente:
                mensagem = f'Nome e código já estão em uso. Tente novamente.\n\n Se desejar, utilize o gerador automatico de código, clicando no botão "Gerar".'

            if not (nome_existente or codigo_existente):
                resposta = messagebox.askquestion('Confirmação', 'Confirmar o cadastro?')
                if resposta == 'yes':
                    # Inserir dados na tabela:
                    c.execute('INSERT INTO sistemas VALUES (?,?)', (sistemaCodigo, sistemaNome))
                    # Confirmar as alterações:
                    conexao.commit()
                    # Fechar o banco de dados:
                    conexao.close()

                    print(f'Cadastro criado - Nome: {sistemaNome}, Código: {sistemaCodigo}')
                    self.nome_entry.delete(0, 'end')
                    self.codigo_entry.delete(0, 'end')
                    self.update_data_table()  # Atualizar a tabela quando uma nova entrada é criada
                    return

            # Exiba uma mensagem de erro com informações sobre as duplicatas
            messagebox.showerror("Erro", mensagem)
        else:
            print('Erro', 'Por favor, preencha todos os campos.')
            messagebox.showerror('Erro', 'Por favor, preencha todos os campos.')  # Exibe um alerta de erro

    # Adicione um método para atualizar a tabela com dados do banco de dados
    def update_data_table(self):
        # Limpar dados existentes na tabela
        for item in self.data_table.get_children():
            self.data_table.delete(item)

        # Buscar dados do banco de dados e preencher a tabela
        conexao = sqlite3.connect('database.db')
        c = conexao.cursor()
        c.execute("SELECT nome_sistema, cod_sistema FROM sistemas")
        data = c.fetchall()
        conexao.close()

        for row in data:
            self.data_table.insert('', 'end', values=(row[0], row[1]))

    # Função para filtrar a tabela com base no critério de pesquisa
    def filtrar_tabela(self, event):
        criterio = self.filtro_entry.get().lower().replace(" ", "")

        for item in self.data_table.get_children():
            self.data_table.delete(item)

        conexao = sqlite3.connect('banco_sistemas.db')
        c = conexao.cursor()
        c.execute("SELECT nome, codigo FROM tabela_sistemas")
        data = c.fetchall()
        conexao.close()

        for row in data:
            if criterio in row[0].lower() or criterio in row[1].lower():
                self.data_table.insert('', 'end', values=(row[0], row[1]))

    from tkinter import simpledialog, Label, Entry, Button, Toplevel

    # ...

    def editar_registro(self):
        # Recupere o item selecionado na tabela
        selected_item = self.data_table.selection()
        if selected_item:
            # Recupere os dados do registro selecionado
            item = self.data_table.item(selected_item)
            nome = item['values'][0]
            codigo = item['values'][1]

            # Crie uma janela de diálogo personalizada
            dialog = Toplevel(self)
            dialog.title('Editar Registro')
            dialog.geometry('400x150')
            dialog.resizable(width=False, height=False)

            # Altere o estilo do widget Toplevel
            dialog.tk_setPalette(background="#2E2E2E", foreground="white")  # Defina as cores para o modo dark

            # Crie campos de entrada para editar o nome e o código
            CTkLabel(dialog, text="Nome:").place(x=10, y=20)
            novo_nome_entry = CTkEntry(dialog, width=180)
            novo_nome_entry.insert(0, nome)
            novo_nome_entry.place(x=10, y=50)

            CTkLabel(dialog, text="Código:").place(x=210, y=20)
            novo_codigo_entry = CTkEntry(dialog, width=180)
            novo_codigo_entry.insert(0, codigo)
            novo_codigo_entry.place(x=210, y=50)

            # Função para atualizar o registro no banco de dados
            def atualizar_registro():
                novo_nome = novo_nome_entry.get().lower().replace(" ", "")
                novo_codigo = novo_codigo_entry.get()
                if novo_nome and novo_codigo:
                    conexao = sqlite3.connect('database.db')
                    c = conexao.cursor()
                    c.execute("UPDATE sistemas SET nome_sistema=?, cod_sistema=? WHERE nome_sistema=?",
                              (novo_nome, novo_codigo, nome))
                    conexao.commit()
                    conexao.close()
                    self.update_data_table()
                    dialog.destroy()

            # Crie um botão para confirmar a atualização
            CTkButton(dialog, text="Confirmar", command=atualizar_registro).place(x=125, y=100)

            # Centralize a janela Toplevel
            x = (self.winfo_screenwidth() - dialog.winfo_reqwidth()) / 2
            y = (self.winfo_screenheight() - dialog.winfo_reqheight()) / 2
            dialog.geometry("+%d+%d" % (x, y))

    def excluir_registro(self):
        # Recupere o item selecionado na tabela
        selected_item = self.data_table.selection()
        if selected_item:
            # Exiba um diálogo de confirmação
            resposta = messagebox.askyesno("Confirmação", "Tem certeza de que deseja excluir este registro?")
            if resposta == True:
                # Recupere os dados do registro selecionado
                item = self.data_table.item(selected_item)
                nome = item['values'][0]

                # Exclua o registro do banco de dados
                conexao = sqlite3.connect('database.db')
                c = conexao.cursor()
                c.execute("DELETE FROM sistemas WHERE nome_sistema=?", (nome,))
                conexao.commit()
                conexao.close()
                self.update_data_table()


# Executa a aplicação
if __name__ == '__main__':
    app = App()
    app.mainloop()
