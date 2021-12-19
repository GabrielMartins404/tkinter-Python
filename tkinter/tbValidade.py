from tkinter import *
from tkinter import ttk

app = Tk()

azul = "#389ed8"
azulC = "#4a71ff"
font = "Ms shell dig 2"

Label(app, text = "Lista de validade de produtos", background = azul, foreground = "#fff", font = (font, 16, "bold"),  padx = 10, pady = 10).pack(anchor = N, expand = TRUE, pady = 20)

def tabelaValidade(componente):

    listaProdutos = [
        ['1','Arroz', '11/04/2022' ,'105 dias vencer'],
        ['2', 'Feijão', '15/10/2022', '140 dias até vencer'],
        ['3', 'Macarrão', '19/07/2023', '300 dias até vencer'],
        ['4', 'Café', '07/10/2021' , 'vencido a 10 dias'],
        ['5', 'Acúcar', '14/10/2022' , '120 dias até vencer'],
        ['6', 'Sal', '05/03/2025' , '600 dias até vencer'],
        ['7', 'Sabonete', '09/01/2025', '600 dias até vencer'],
        ['8', 'Óleo de Soja', '22/06/2019', 'vencido a 300 dias'],
        ['9', 'Vinagre', '06/06/2023', '400 dias até vencer'],
        ['10', 'Sorvete', '04/05/2021', '200 dias até vencer'],

    ]

    linha = ttk.Treeview(componente, columns=('id', 'nome', 'dtValidade', 'dEstrago'), show='headings')
    linha.column('id', minwidth=0, width=50)
    linha.column('nome', minwidth=0, width=250)
    linha.column('dtValidade', minwidth=0, width=100)
    linha.column('dEstrago', minwidth=0, width=150)

    linha.heading('id', text='Índices')
    linha.heading('nome', text='Nome do Produto')
    linha.heading('dtValidade', text='Data de Validade')
    linha.heading('dEstrago', text='Dias até estragar')
    linha.pack(pady = 30)

    for(id,nome,dtValidade,dEstrago) in listaProdutos:
        linha.insert("","end", values=(id,nome,dtValidade,dEstrago))

tabelaValidade(app)

btnEdit = Button(app, text="Editar")
btnEdit.config(bg = "#4CAF7A", fg="#ffffff", font=('Ms shell dig 2', 12, 'bold'), activebackground = "#50DC55",activeforeground="#ffffff")
btnEdit.config(bd=0, padx=30, pady=5)
btnEdit.pack(side=LEFT, padx=20, pady=10, anchor=S)

btnExclui = Button(app, text="Excluir")
btnExclui.config(bg = "#AF644C", fg="#ffffff", font=('Ms shell dig 2', 12, 'bold'), activebackground = "#AF4C4C", activeforeground="#ffffff")
btnExclui.config(bd=0, padx=30, pady=5)
btnExclui.pack(side=RIGHT, padx=20, pady=10, anchor=S)
app.mainloop()

