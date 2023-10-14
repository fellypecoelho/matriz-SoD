from customtkinter import *

class App(CTk):
    def __init__(self):
        super().__init__()

        # Configurações iniciais e inicialização de variáveis
        self.layout_config()  # Configurações da janela
        self.frames = {}  # Dicionário para armazenar os frames
        self.menuLateral()  # Cria o menu lateral
        self.current_frame = None  # Inicializa o frame atual como vazio

        # Primeiro, crie todos os frames, incluindo o 'frameHome'.
        self.home()
        self.perfil()
        self.sistema()
        self.usuario()

        # Em seguida, exiba o frame 'frameHome' como padrão.
        self.show_home_frame()

    def layout_config(self):
        # Configurações iniciais da janela
        self.title('Escola XYZ')  # Define o título da janela
        self.geometry('910x550')  # Define o tamanho da janela
        self.resizable(width=True, height=True)  # Permite redimensionar a janela

    def menuLateral(self):
        frameMenu = CTkFrame(self, width=150, height=500, corner_radius=0)
        frameMenu.place(x=0, y=0)

        # Botões do menu lateral
        btn_menuHome = CTkButton(frameMenu, text='Home', font=('Arial', 15, 'bold'), text_color='#c3c3c3',
                              fg_color='#1f6aa5', corner_radius=0, width=150, height=50, anchor='w', border_spacing=10,
                              command=self.show_home_frame)
        btn_menuHome.place(x=0, y=0)
        btn_menuPerfil = CTkButton(frameMenu, text='Perfil', font=('Arial', 15, 'bold'), text_color='#c3c3c3',
                                fg_color='#1f6aa5', corner_radius=0, width=150, height=50, anchor='w',
                                border_spacing=10, command=self.show_perfil_frame)
        btn_menuPerfil.place(x=0, y=50)
        btn_menuSistema = CTkButton(frameMenu, text='Sistema', font=('Arial', 15, 'bold'), text_color='#c3c3c3',
                                 fg_color='#1f6aa5', corner_radius=0, width=150, height=50, anchor='w',
                                 border_spacing=10, command=self.show_sistema_frame)
        btn_menuSistema.place(x=0, y=100)
        btn_menuUsuario = CTkButton(frameMenu, text='Usuário', font=('Arial', 15, 'bold'), text_color='#c3c3c3',
                                 fg_color='#1f6aa5', corner_radius=0, width=150, height=50, anchor='w',
                                 border_spacing=10, command=self.show_usuario_frame)
        btn_menuUsuario.place(x=0, y=150)

    def show_frame(self, frame):
        if self.current_frame:
            self.current_frame.place_forget()  # Oculta o frame atual
        frame.place(x=160, y=0)  # Exibe o novo frame
        self.current_frame = frame  # Atualiza o frame atual

    def show_home_frame(self):
        self.show_frame(self.frames['home'])  # Exibe o frame 'home' e atualiza o frame atual

    def show_perfil_frame(self):
        self.show_frame(self.frames['perfil'])  # Exibe o frame 'perfil' e atualiza o frame atual

    def show_sistema_frame(self):
        self.show_frame(self.frames['sistema'])  # Exibe o frame 'sistema' e atualiza o frame atual

    def show_usuario_frame(self):
        self.show_frame(self.frames['usuario'])  # Exibe o frame 'usuario' e atualiza o frame atual

    def home(self):
        frameHome = CTkFrame(self, fg_color='transparent', width=750, height=500, corner_radius=0)
        self.frames['home'] = frameHome  # Armazena o frame 'home' no dicionário
        labelTitulo_frame = CTkLabel(frameHome, text='H O M E', font=('Arial', 20))
        labelTitulo_frame.place(x=10, y=10)

    def perfil(self):
        framePerfil = CTkFrame(self, fg_color='transparent', width=750, height=500, corner_radius=0)
        self.frames['perfil'] = framePerfil  # Armazena o frame 'perfil' no dicionário
        labelTitulo_frame = CTkLabel(framePerfil, text='P E R F I L', font=('Arial', 20))
        labelTitulo_frame.place(x=10, y=10)

    def sistema(self):
        frameSistema = CTkFrame(self, fg_color='transparent', width=750, height=500, corner_radius=0)
        self.frames['sistema'] = frameSistema  # Armazena o frame 'sistema' no dicionário
        labelTitulo_frame = CTkLabel(frameSistema, text='S I S T E M A', font=('Arial', 20))
        labelTitulo_frame.place(x=10, y=10)

    def usuario(self):
        frameUsuario = CTkFrame(self, fg_color='transparent', width=750, height=500, corner_radius=0)
        self.frames['usuario'] = frameUsuario  # Armazena o frame 'usuario' no dicionário
        labelTitulo_frame = CTkLabel(frameUsuario, text='U S U Á R I O', font=('Arial', 20))
        labelTitulo_frame.place(x=10, y=10)

if __name__ == '__main__':
    app = App()
    app.mainloop()
