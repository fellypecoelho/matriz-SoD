from customtkinter import *
from tkinter import messagebox, ttk
import random
import sqlite3

#O CODIGO ABAIXO ESTÁ COMENTADO PARA NÃO CRIAR UM BANDO DE DADOS SEM QUERER QUANDO EXECUTAR
#MAS MANTIVE O CODIGO AQUI PARA VOCÊS VISUALIZAREM COMO EU FIZ

# #Criando o Banco de Dados:
#
# conexao = sqlite3.connect('banco_sistemas.db')
#
# # Criando o cursor:
# c = conexao.cursor()
#
# # Criando a tabela:
#
# # c.execute("""CREATE TABLE tabela_sistemas (
# #     nome text,
# #     codigo text,
# #     )""")
#
# #Commit as mudanças:
# conexao.commit()
#
# #Fechar o banco de dados:
# conexao.close()


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

        self.home()  # Cria o quadro da seção "home"
        self.perfil()  # Cria o quadro da seção "perfil"
        self.sistema()  # Cria o quadro da seção "sistema"
        self.usuario()  # Cria o quadro da seção "usuário"

        self.show_home_frame()  # Exibe o quadro "home" por padrão

        self.update_data_table()  # Inicializar a tabela com dados existentes

    # Configurações da janela principal
    def layout_config(self):
        self.title('Escola XYZ')
        self.geometry('910x550')
        self.resizable(width=True, height=True)

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

        btn_nomes = ['home', 'perfil', 'sistema', 'usuario']

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
    def show_home_frame(self):
        self.show_frame('home')

    # Exibe o quadro "perfil"
    def show_perfil_frame(self):
        self.show_frame('perfil')

    # Exibe o quadro "sistema"
    def show_sistema_frame(self):
        self.show_frame('sistema')

    # Exibe o quadro "usuário"
    def show_usuario_frame(self):
        self.show_frame('usuario')

    # Cria o quadro da seção "home"
    def home(self):
        frameHome = CTkFrame(self, fg_color='transparent', width=750, height=500, corner_radius=0)
        self.frames['home'] = frameHome
        labelTitulo_frame = CTkLabel(frameHome, text='H O M E', font=('Arial', 20))
        labelTitulo_frame.place(x=10, y=10)

    # Cria o quadro da seção "perfil"
    def perfil(self):
        framePerfil = CTkFrame(self, fg_color='transparent', width=750, height=500, corner_radius=0)
        self.frames['perfil'] = framePerfil
        labelTitulo_frame = CTkLabel(framePerfil, text='P E R F I L', font=('Arial', 20))
        labelTitulo_frame.place(x=10, y=10)

    # Cria o quadro da seção "sistema"
    def sistema(self):
        frameSistema = CTkFrame(self, fg_color='transparent', width=750, height=500, corner_radius=0)
        self.frames['sistema'] = frameSistema

        labelTitulo_frame = CTkLabel(frameSistema, text='S I S T E M A', font=('Arial', 20))
        labelTitulo_frame.place(x=10, y=10)

        label_nome = CTkLabel(frameSistema, text='Nome:')
        label_nome.place(x=10, y=60)
        self.nome_entry = CTkEntry(frameSistema, width=200)
        self.nome_entry.place(x=80, y=60)

        label_codigo = CTkLabel(frameSistema, text='Código:')
        label_codigo.place(x=10, y=100)
        self.codigo_entry = CTkEntry(frameSistema, width=140)
        self.codigo_entry.place(x=80, y=100)

        gerar_codigo_button = CTkButton(frameSistema, text='Gerar', width=50, command=self.gerar_codigo)
        gerar_codigo_button.place(x=230, y=100)

        confirm_button = CTkButton(frameSistema, text='Criar Cadastro', command=self.criar_cadastro)
        confirm_button.place(x=10, y=150)

        # Cria uma tabela para exibir dados
        self.data_table = ttk.Treeview(frameSistema, columns=('Nome', 'Código'), show='headings')
        self.data_table.heading('#1', text='Nome')
        self.data_table.heading('#2', text='Código')
        self.data_table.column('#1', width=300)
        self.data_table.column('#2', width=150)

        # Remover a coluna de índice padrão
        self.data_table['show'] = 'headings'

        self.data_table.place(x=10, y=300)

        # Adicione a entrada de texto e o botão de filtro
        self.filtro_entry = CTkEntry(frameSistema, width=300)
        self.filtro_entry.place(x=10, y=250)

        filtro_button = CTkButton(frameSistema, text='Filtrar', command=self.filtrar_tabela)
        filtro_button.place(x=320, y=250)

    # Cria o quadro da seção "usuário"
    def usuario(self):
        frameUsuario = CTkFrame(self, fg_color='transparent', width=750, height=500, corner_radius=0)
        self.frames['usuario'] = frameUsuario
        labelTitulo_frame = CTkLabel(frameUsuario, text='U S U Á R I O', font=('Arial', 20))
        labelTitulo_frame.place(x=10, y=10)

    # Gera um código aleatório e insere na entrada de texto
    def gerar_codigo(self):
        # Crie uma conexão com o banco de dados SQLite
        conexao = sqlite3.connect('banco_sistemas.db')
        c = conexao.cursor()

        while True:
            codigo_aleatorio = random.randint(1000, 9999)

            # Verifique se o código já existe no banco de dados
            c.execute("SELECT COUNT(*) FROM tabela_sistemas WHERE codigo=?", (str(codigo_aleatorio),))
            count = c.fetchone()[0]

            if count == 0:  # O código é único
                break

        self.codigo_entry.delete(0, 'end')
        self.codigo_entry.insert(0, str(codigo_aleatorio))

        # Feche a conexão com o banco de dados
        conexao.close()

    # Criar novo cadastro no banco de dados
    def criar_cadastro(self):
        sistemaNome = self.nome_entry.get().lower().replace(" ", "") # Converte para letras minúsculas e elimina espaços
        sistemaCodigo = self.codigo_entry.get()

        if sistemaNome and sistemaCodigo:
            # Verifique se o nome já existe no banco de dados
            conexao = sqlite3.connect('banco_sistemas.db')
            c = conexao.cursor()

            c.execute("SELECT * FROM tabela_sistemas WHERE nome = ?", (sistemaNome,))
            nome_existente = c.fetchone()

            # Verifique se o código já existe no banco de dados
            c.execute("SELECT * FROM tabela_sistemas WHERE codigo = ?", (sistemaCodigo,))
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
                    c.execute('INSERT INTO tabela_sistemas VALUES (:nome, :codigo)',
                              {
                                  'nome': sistemaNome,
                                  'codigo': sistemaCodigo
                              })
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
        conexao = sqlite3.connect('banco_sistemas.db')
        c = conexao.cursor()
        c.execute("SELECT nome, codigo FROM tabela_sistemas")
        data = c.fetchall()
        conexao.close()

        for row in data:
            self.data_table.insert('', 'end', values=row)

    # Função para filtrar a tabela com base no critério de pesquisa
    def filtrar_tabela(self):
        # Obtém o critério de pesquisa da entrada de texto
        criterio = self.filtro_entry.get().strip().lower()

        # Limpa os dados existentes na tabela
        for item in self.data_table.get_children():
            self.data_table.delete(item)

        # Busca os dados do banco de dados
        conexao = sqlite3.connect('banco_sistemas.db')
        c = conexao.cursor()
        c.execute("SELECT nome, codigo FROM tabela_sistemas")
        data = c.fetchall()
        conexao.close()

        # Preenche a tabela com os dados que correspondem ao critério de pesquisa
        for row in data:
            if criterio in row[0].lower() or criterio in row[1].lower():
                self.data_table.insert('', 'end', values=row)


# Executa a aplicação
if __name__ == '__main__':
    app = App()
    app.mainloop()
