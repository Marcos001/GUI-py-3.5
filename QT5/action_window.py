
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QHBoxLayout, QMessageBox)
from PyQt5.QtGui import QIcon

class window(QWidget):

    #constutor
    def __init__(self, parent=None):

        super(window, self).__init__()

        self.button = QPushButton("Exibir Mensagem")
        self.button.clicked.connect(self.exibir)

        self.line_edit = QLineEdit()

        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.setWindowTitle("Hello Word")
        self.resize(450,300)

        #icon of application
        self.setWindowIcon(QIcon('../asserts/icon_unix.png'))

    def exibir(self):
        self.text = self.line_edit.text()
        self.message_box = QMessageBox.information(self, "Exemplo 1", self.text)



if __name__ == '__main__':

    # create PyQt5 application project
    app = QApplication([])

    janela = window()

    janela.show()

    sys.exit(app.exec_())