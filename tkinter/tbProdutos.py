from tkinter import *
from tkinter import ttk

app = Tk()

azul = "#389ed8"
azulC = "#4a71ff"
font = "Ms shell dig 2"

Label(app, text = "Lista de Produtos", background = azul, foreground = "#fff", font = (font, 16, "bold"),  padx = 10, pady = 10).pack(anchor = N, expand = TRUE, pady = 20)

def tabelarProdutos(componente):

    listaProdutos = [
        ['1','Arroz', 55 ,'R$ 17.00'],
        ['2', 'Feijão', 60, 'R$ 4.00'],
        ['3', 'Macarrão', 45, 'R$ 3.00'],
        ['4', 'Café', 98 , 'R$ 3.00'],
        ['5', 'Acúcar', 19 , 'R$ 2.00'],
        ['6', 'Sal', 105 , 'R$ 0.90'],
        ['7', 'Sabonete', 68, 'R$ 2.00'],
        ['8', 'Óleo de Soja', 77, 'R$ 7.00'],
        ['9', 'Vinagre', 73, 'R$ 5.00'],
        ['10', 'Sorvete', 18, 'R$ 12.00'],
        ['11', 'Flocão', 99, 'R$ 3.00'],
        ['12', 'Bolacha', 457, 'R$ 2.00'],
        ['13', 'Refrigerantes', 47, 'R$ 7.00'],
        ['14', 'Sabão', 38, 'R$ 4.00'],
        ['15', 'Sabão em Pó', 60, 'R$ 10.00'],

    ]

    linha = ttk.Treeview(componente, columns=('id', 'nome', 'qtd', 'preco'), show='headings')
    linha.column('id', minwidth=0, width=50)
    linha.column('nome', minwidth=0, width=250)
    linha.column('qtd', minwidth=0, width=100)
    linha.column('preco', minwidth=0, width=150)

    linha.heading('id', text='Índices')
    linha.heading('nome', text='Nome do Produto')
    linha.heading('qtd', text='Quantidade')
    linha.heading('preco', text='Preço Individual')
    linha.pack(pady = 30)

    for(id,nome,qtd,preco) in listaProdutos:
        linha.insert("","end", values=(id,nome,qtd,preco))

tabelarProdutos(app)

btnEdit = Button(app, text="Editar")
btnEdit.config(bg = "#4CAF7A", fg="#ffffff", font=('Ms shell dig 2', 12, 'bold'), activebackground = "#50DC55",activeforeground="#ffffff")
btnEdit.config(bd=0, padx=30, pady=5)
btnEdit.pack(side=LEFT, padx=20, pady=10, anchor=S)

btnExclui = Button(app, text="Excluir")
btnExclui.config(bg = "#AF644C", fg="#ffffff", font=('Ms shell dig 2', 12, 'bold'), activebackground = "#AF4C4C", activeforeground="#ffffff")
btnExclui.config(bd=0, padx=30, pady=5)
btnExclui.pack(side=RIGHT, padx=20, pady=10, anchor=S)
app.mainloop()

