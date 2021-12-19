from tkinter import *
from tkinter import ttk

def erroLogin():
    app = Tk()
    app.title("Erro ao logar!!")
    app.configure(background = "#ddd")
    app.geometry("400x300")

    title = Label(app, text="Erro ao logar no sistema", background = "#ddd", foreground = "red", font = ("arial", 16, "bold"), anchor = W )
    title.grid(row=0, column=0, padx=20, pady=20)

    msg = Label(app, text="Usuário ou senha não conferem com as informações\ncadastrada no sistema, tente novamente.", background="#ddd", foreground="red", font=("arial", 12, ), anchor=W)
    msg.grid(row=1, column=0, padx=20, pady=20)

    btn = Button(app, text = "OK")
    btn.grid(row=2, column = 0, sticky = "e", padx = 40, pady = 40)
    btn.config(bg = "#389ed8", fg = "#ffffff", font = ('arial', 14, 'bold'), activebackground = "#909bff", activeforeground = "#ffffff")
    btn.config(bd = 0, padx = 5, pady = 5)

    app.mainloop()

erroLogin()