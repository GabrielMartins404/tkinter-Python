from PyQt5 import uic, QtWidgets

app = QtWidgets.QApplication([])

#importação das telas
telaCadastro = uic.loadUi("screens/tela_cadastroProdutos.ui")
telaLogin = uic.loadUi("screens/tela_login.ui")
telaEdicao = uic.loadUi("screens/tela_edicaoProdutos.ui")
mainTela = uic.loadUi("screens/tela_mainTable.ui")
telaEdicao.show()
telaCadastro.show()
telaLogin.show()
mainTela.show()
app.exec()