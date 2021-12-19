from tkinter import *
from tkinter import ttk

app = Tk()

azul = "#389ed8"
azulC = "#4a71ff"
font = "Ms shell dig 2"

Label(app, text = "Lista de Gastos", background = azul, foreground = "#fff", font = (font, 16, "bold"),  padx = 10, pady = 10).pack(anchor = N, expand = TRUE, pady = 20)

def tabelarSaida(componente):

    listaProdutos = [
        ['1','Arroz', 55 ,'R$ 17.00', 'R$ 4235.00'],
        ['2', 'Feijão', 60, 'R$ 4.00', 'R$ 240.00'],
        ['3', 'Macarrão', 45, 'R$ 3.00', 'R$ 135.00'],
        ['4', 'Café', 98 , 'R$ 3.00', 'R$ 294.00'],
        ['5', 'Acúcar', 19 , 'R$ 2.00', 'R$ 38.00'],
        ['6', 'Sal', 105 , 'R$ 0.90', 'R$ 94.05'],
        ['7', 'Sabonete', 68, 'R$ 2.00', 'R$ 136.00'],
        ['8', 'Óleo de Soja', 77, 'R$ 7.00', 'R$ 539.00'],
        ['9', 'Vinagre', 73, 'R$ 5.00', 'R$ 365.00'],
        ['10', 'Sorvete', 18, 'R$ 12.00', 'R$ 216.00'],
        ['11', 'Flocão', 99, 'R$ 3.00', 'R$ 297.00'],
        ['12', 'Bolacha', 457, 'R$ 2.00', 'R$ 914.00'],
        ['13', 'Refrigerantes', 47, 'R$ 7.00', 'R$ 329.00'],
        ['14', 'Sabão', 38, 'R$ 4.00', 'R$ 152.00'],
        ['15', 'Sabão em Pó', 60, 'R$ 10.00', 'R$ 600.00'],

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
    linha.heading('preco', text='Preço Individual')
    linha.heading('ttG', text='Total de ganhos previsto')
    linha.pack(pady = 30)

    for(id,nome,qtd,preco,ttG) in listaProdutos:
        linha.insert("","end", values=(id,nome,qtd,preco,ttG))

tabelarSaida(app)
app.mainloop()

