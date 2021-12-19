from tkinter import *
from tkinter import ttk
import tbProdutos
import tbValidade
import tbSaida
import tbEntrada

def mainTela():
    azul = "#389ed8"
    azulC = "#4a71ff"
    font = "Ms shell dig 2"

    app = Tk()
    app.title("Tela Principal")
    app.configure(background = "#ddd")
    app.geometry("1000x650")

    largura_screen = app.winfo_screenwidth()

    #Parte de cima
    sttBar = Frame(master=app, height = 70, bg=azul)
    sttBar.pack(fill=X, side=TOP)

    btnSair = Button(sttBar, text = "Sair")
    btnSair.config(bg = "#AF644C", fg = "#ffffff", font = ('Ms shell dig 2', 12,), activebackground = "#D92E2E", activeforeground = "#ffffff")
    btnSair.config(bd = 0, padx = 15, pady = 5)
    btnSair.pack(side = LEFT, padx = 10, pady = 10)

    #parte principal
    mainFr = Frame(master=app, height = 510 , bg="#ddd")
    mainFr.pack(fill = BOTH, expand = TRUE)

    btnTable = Button(mainFr, text = "Tabelas")
    btnTable.config(bg = azul, fg = "#ffffff", font = ('Ms shell dig 2', 12, 'bold'), activebackground = azulC, activeforeground = "#ffffff")
    btnTable.config(bd = 0, padx = 30, pady = 5)
    btnTable.pack(side = LEFT, padx = 150, pady = 20, anchor = N)

    btnCadast = Button(mainFr, text="Cadastrar")
    btnCadast.config(bg=azul, fg="#ffffff", font=('Ms shell dig 2', 12, 'bold'), activebackground=azulC, activeforeground="#ffffff")
    btnCadast.config(bd=0, padx=30, pady=5)
    btnCadast.pack(side=RIGHT, padx=150, pady = 20, anchor = N)

    #Abas de dados
    posx = (largura_screen/2) - (900/2)
    print(posx)
    note = ttk.Notebook(mainFr)
    note.place(x = posx, y = 100, width = 900, height = 460,)

    style = ttk.Style()

    style.theme_create("yummy", parent="alt", settings={
        "TNotebook": {
            "configure":
                {"tabmargins": [2, 5, 2, 0]}
        },

        "TNotebook.Tab": {
            "configure":
                {
                    "padding": [10, 5],
                    "background": azul,
                    "foreground": "#fff",
                    "font": ('Ms shell dig 2', 12),
                    "bordercolor": azul
                },
            "map":
                {
                    "background": [("selected", azulC)],
                    "expand": [("selected", [1, 1, 1, 0])],
                    "bordercolor": azul
                }
        }
    })

    style.theme_use("yummy")

    tb1 = Frame(note)
    tb2 = Frame(note)
    tb3 = Frame(note)
    tb4 = Frame(note)

    Label(tb1, text = "Lista de Produtos", background = azul, foreground = "#fff", font = (font, 16, "bold"), padx = 10, pady = 10).pack(anchor = N, expand = TRUE, pady = 20)
    Label(tb2, text="Lista de Gastos com os fornecedores", background=azul, foreground="#fff", font=(font, 16, "bold"),padx=10, pady=10).pack(anchor=N, expand=TRUE, pady=20)
    Label(tb3, text="Lista de ganhos previstos", background=azul, foreground="#fff", font=(font, 16, "bold"),padx=10, pady=10).pack(anchor=N, expand=TRUE, pady=20)
    Label(tb4, text="Lista de validade de produtos", background=azul, foreground="#fff", font=(font, 16, "bold"), padx=10, pady=10).pack(anchor=N, expand=TRUE, pady=20)

    #Adicionar as tabelas ao frame
    table1 = tbProdutos.tabelarProdutos(tb1)
    table2 = tbEntrada.tabelarEntrada(tb2)
    table3 = tbSaida.tabelarSaida(tb3)
    table4 = tbValidade.tabelaValidade(tb4)

    note.add(tb1, text = "Produtos")
    note.add(tb2, text="Saida")
    note.add(tb3, text="Entrada")
    note.add(tb4, text="validade")

    #Botões inferiores

    btnEdit = Button(tb1, text="Editar")
    btnEdit.config(bg = "#4CAF7A", fg="#ffffff", font=('Ms shell dig 2', 12, 'bold'), activebackground = "#50DC55",activeforeground="#ffffff")
    btnEdit.config(bd=0, padx=30, pady=5)
    btnEdit.pack(side=LEFT, padx=50, pady=10, anchor=S)

    btnExclui = Button(tb1, text="Excluir")
    btnExclui.config(bg = "#AF644C", fg="#ffffff", font=('Ms shell dig 2', 12, 'bold'), activebackground = "#AF4C4C", activeforeground="#ffffff")
    btnExclui.config(bd=0, padx=30, pady=5)
    btnExclui.pack(side=RIGHT, padx=50, pady=10, anchor=S)

    #parte de baixo
    footer = Frame(master=app, height = 40, bg=azul)
    footer.pack(fill=X, side=BOTTOM)

    app.mainloop()

mainTela()