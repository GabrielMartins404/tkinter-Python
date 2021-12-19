from tkinter import *
from tkinter import ttk

def cancelar():
    app = Tk()
    app.title("Cancelar ação")
    app.configure(background = "#ddd")
    app.geometry("400x300")

    title = Label(app, text="Cancelar ação", background = "#ddd", foreground = "black", font = ("arial", 16, "bold"), anchor = W )
    title.grid(row=0, column=0, padx=60, pady=20)

    msg = Label(app, text="Deseja realmente cancelar esta ação?.", background="#ddd", foreground="black", font=("arial", 12, ), anchor=W)
    msg.grid(row=1, column=0, padx=60, pady=20)

    btnS = Button(app, text = "Sim")
    btnS.place(x=200, y = 190, width = 50, height = 50)
    btnS.config(bg = "#4CAF7A", fg = "#ffffff", font = ('arial', 14, 'bold'), activebackground = "#50DC55", activeforeground = "#ffffff")
    btnS.config(bd = 0, padx = 5, pady = 5)

    btnN = Button(app, text = "Não")
    btnN.place(x = 290, y = 190, width = 50, height = 50)
    btnN.config(bg = "#AF644C", fg = "#ffffff", font = ('arial', 14, 'bold'), activebackground = "#AF4C4C", activeforeground = "#ffffff")
    btnN.config(bd = 0, padx = 5, pady = 5)

    app.mainloop()

cancelar()