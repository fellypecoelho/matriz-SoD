from tkinter import *
from tkinter import ttk
from customtkinter import *



def show_home_frame():
    perfilFrame.grid_forget()
    sistemaFrame.grid_forget()
    usuarioFrame.grid_forget()
    homeFrame.grid(row=0, column=1, padx=(5, 0), pady=(0,0), sticky='nswe', columnspan=1)

    btn_homeMenu.configure(fg_color='#1f6aa5')
    btn_perfilMenu.configure(fg_color='#2b2b2b')
    btn_sistemaMenu.configure(fg_color='#2b2b2b')
    btn_usuarioMenu.configure(fg_color='#2b2b2b')


def show_perfil_frame():
    homeFrame.grid_forget()
    sistemaFrame.grid_forget()
    usuarioFrame.grid_forget()
    perfilFrame.grid(row=0, column=1, padx=(5, 0), pady=(0,0), sticky='nswe', columnspan=1)

    btn_homeMenu.configure(fg_color='#2b2b2b')
    btn_perfilMenu.configure(fg_color='#1f6aa5')
    btn_sistemaMenu.configure(fg_color='#2b2b2b')
    btn_usuarioMenu.configure(fg_color='#2b2b2b')

def show_sistema_frame():
    homeFrame.grid_forget()
    perfilFrame.grid_forget()
    usuarioFrame.grid_forget()
    sistemaFrame.grid(row=0, column=1, padx=(5, 0), pady=(0,0), sticky='nswe', columnspan=1)

    btn_homeMenu.configure(fg_color='#2b2b2b')
    btn_perfilMenu.configure(fg_color='#2b2b2b')
    btn_sistemaMenu.configure(fg_color='#1f6aa5')
    btn_usuarioMenu.configure(fg_color='#2b2b2b')

def show_usuario_frame():
    homeFrame.grid_forget()
    perfilFrame.grid_forget()
    sistemaFrame.grid_forget()
    usuarioFrame.grid(row=0, column=1, padx=(5, 0), pady=(0,0), sticky='nswe', columnspan=1)

    btn_homeMenu.configure(fg_color='#2b2b2b')
    btn_perfilMenu.configure(fg_color='#2b2b2b')
    btn_sistemaMenu.configure(fg_color='#2b2b2b')
    btn_usuarioMenu.configure(fg_color='#1f6aa5')





app = CTk()
#Tema do Sistema
app._set_appearance_mode('dark') #Modos: "system", "dark" e "light"
set_default_color_theme("blue") #Temas: "blue" (standard), "green", "dark-blue"

app.title('Cadastro Sistema')

#Dimenções da Janela
app.geometry('900x500')
app.resizable(width=False, height=False) #Bloquear dimensões



#LAYOUT
menuFrame=CTkFrame(app, fg_color='#2b2b2b')
menuFrame.grid(row=0, column=0, padx=(0, 0), pady=(0,0), sticky='nswe', columnspan=1)
menuFrame.configure(width=250, height=500)

homeFrame=CTkFrame(app, fg_color='#242424')
homeFrame.grid(row=0, column=1, padx=(5, 0), pady=(0,0), sticky='nswe', columnspan=1)
homeFrame.configure(width=650, height=500)

perfilFrame=CTkFrame(app, fg_color='#242424')
perfilFrame.grid(row=0, column=1, padx=(5, 0), pady=(0,0), sticky='nswe', columnspan=1)
perfilFrame.configure(width=650, height=500)
perfilFrame.grid_forget()  # Oculta o frame perfilFrame

sistemaFrame=CTkFrame(app, fg_color='#242424')
sistemaFrame.grid(row=0, column=1, padx=(5, 0), pady=(0,0), sticky='nswe', columnspan=1)
sistemaFrame.configure(width=650, height=500)
sistemaFrame.grid_forget()  # Oculta o frame perfilFrame

usuarioFrame=CTkFrame(app, fg_color='#242424')
usuarioFrame.grid(row=0, column=1, padx=(5, 0), pady=(0,0), sticky='nswe', columnspan=1)
usuarioFrame.configure(width=650, height=500)
usuarioFrame.grid_forget()  # Oculta o frame perfilFrame





#CONTEÚDO MENUFRAME
btn_homeMenu = CTkButton(menuFrame, text='Home', font=('Arial', 15, 'bold'), text_color='#c3c3c3', fg_color='#1f6aa5', corner_radius=0, height=40, anchor='w', border_spacing=15, command=show_home_frame)
btn_homeMenu.grid(row=0, column=0, padx=0, pady=(0,0), sticky='nswe', columnspan=1)

btn_perfilMenu = CTkButton(menuFrame, text='Perfil', font=('Arial', 15, 'bold'), text_color='#c3c3c3', fg_color='#2b2b2b', corner_radius=0, height=40, anchor='w', border_spacing=15, command=show_perfil_frame)
btn_perfilMenu.grid(row=1, column=0, padx=0, pady=(2,0), sticky='nswe', columnspan=1)

btn_sistemaMenu = CTkButton(menuFrame, text='Sistema', font=('Arial', 15, 'bold'), text_color='#c3c3c3', fg_color='#2b2b2b', corner_radius=0, height=40, anchor='w', border_spacing=15, command=show_sistema_frame)
btn_sistemaMenu.grid(row=2, column=0, padx=0, pady=(2,0), sticky='nswe', columnspan=1)

btn_usuarioMenu = CTkButton(menuFrame, text='Usuário', font=('Arial', 15, 'bold'), text_color='#c3c3c3', fg_color='#2b2b2b', corner_radius=0, height=40, anchor='w', border_spacing=15, command=show_usuario_frame)
btn_usuarioMenu.grid(row=3, column=0, padx=0, pady=(2,0), sticky='nswe', columnspan=1)




#CONTEÚDO MAINFRAME
label_tituloHome = CTkLabel(homeFrame, width=200, text='H O M E', font=('Arial', 20))
label_tituloHome.grid(row=0, column=0, padx=10, pady=(30,10), sticky='nswe', columnspan=2)



label_tituloPerfil = CTkLabel(perfilFrame, width=200, text='P E R F I L', font=('Arial', 20))
label_tituloPerfil.grid(row=0, column=0, padx=10, pady=(30,10), sticky='nswe', columnspan=2)


label_tituloSistema = CTkLabel(sistemaFrame, width=200, text='S I S T E M A', font=('Arial', 20))
label_tituloSistema.grid(row=0, column=0, padx=10, pady=(30,10), sticky='nswe', columnspan=2)


label_tituloUsuario = CTkLabel(usuarioFrame, width=200, text='U S U Á R I O', font=('Arial', 20))
label_tituloUsuario.grid(row=0, column=0, padx=10, pady=(30,10), sticky='nswe', columnspan=2)




app.mainloop()

