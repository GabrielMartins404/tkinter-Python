from tkinter import *
from tkinter import ttk

app = Tk()

azul = "#389ed8"
azulC = "#4a71ff"
font = "Ms shell dig 2"

Label(app, text = "Lista de Gastos com os fornecedores", background = azul, foreground = "#fff", font = (font, 16, "bold"),  padx = 10, pady = 10).pack(anchor = N, expand = TRUE, pady = 20)

def tabelarEntrada(componente):

    listaProdutos = [
        ['1','Arroz', 55 ,'R$ 14.00', 'R$ 770.00'],
        ['2', 'Feijão', 60, 'R$ 3.00', 'R$ 180.00'],
        ['3', 'Macarrão', 45, 'R$ 1.00', 'R$ 45.00'],
        ['4', 'Café', 98 , 'R$ 2.00', 'R$ 196.00'],
        ['5', 'Acúcar', 19 , 'R$ 0.99', 'R$ 19.00'],
        ['6', 'Sal', 105 , 'R$ 0.40', 'R$ 42.05'],
        ['7', 'Sabonete', 68, 'R$ 1.00', 'R$ 68.00'],
        ['8', 'Óleo de Soja', 77, 'R$ 3.00', 'R$ 231.00'],
        ['9', 'Vinagre', 73, 'R$ 1.00', 'R$ 73.00'],
        ['10', 'Sorvete', 18, 'R$ 9.00', 'R$ 162.00'],
        ['11', 'Flocão', 99, 'R$ 1.00', 'R$ 99.00'],
        ['12', 'Bolacha', 457, 'R$ 1.00', 'R$ 457.00'],
        ['13', 'Refrigerantes', 47, 'R$ 4.00', 'R$ 188.00'],
        ['14', 'Sabão', 38, 'R$ 2.00', 'R$ 76.00'],
        ['15', 'Sabão em Pó', 60, 'R$ 15.00', 'R$ 300.00'],

    ]

    linha = ttk.Treeview(componente, columns=('id', 'nome', 'qtd', 'preco', 'ttG'), show='headings')
    linha.column('id', minwidth=0, width=50)
    linha.column('nome', minwidth=0, width=250)
    linha.column('qtd', minwidth=0, width=100)
    linha.column('preco', minwidth=0, width=150)
    linha.column('ttG', minwidth=0, width=150)

    linha.heading('id', text='Índices')
    linha.heading('nome', text='Nome do Produto')
    linha.heading('qtd', text='Quantidade')
    linha.heading('preco', text='Preço Individual do Fornecedor')
    linha.heading('ttG', text='Total de Custos')
    linha.pack(pady = 30)

    for(id,nome,qtd,preco,ttG) in listaProdutos:
        linha.insert("","end", values=(id,nome,qtd,preco,ttG))

tabelarEntrada(app)

app.mainloop()

