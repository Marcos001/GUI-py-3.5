
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QHBoxLayout,
                             QMessageBox, QRadioButton, QGroupBox, QVBoxLayout)
from PyQt5.QtGui import QIcon

class window(QWidget):

    #constutor
    def __init__(self, parent=None):

        super(window, self).__init__()

        # firts widgets
        self.button = QPushButton("Exibir Mensagem")
        self.button.clicked.connect(self.exibir) # active
        self.line_edit = QLineEdit()

        # group box of widgets
        self.groupbox = QGroupBox('Opções de Diálogo')

        # options
        self.opt_information = QRadioButton('Information')
        self.opt_information.setChecked(True)
        self.opt_warning = QRadioButton('Warning')
        self.opt_critical = QRadioButton('Critical')

        # Adicionando os RadioButtons em um Layout vertical
        self.layout_options = QVBoxLayout()
        self.layout_options.addWidget(self.opt_information)
        self.layout_options.addWidget(self.opt_critical)
        self.layout_options.addWidget(self.opt_warning)
        self.groupbox.setLayout(self.layout_options)

        # layout of QPushButton e QLineEdit
        self.layout_first_widgets = QHBoxLayout()
        self.layout_first_widgets.addWidget(self.line_edit)
        self.layout_first_widgets.addWidget(self.button)

        # main layout
        self.layout_master = QVBoxLayout()
        self.layout_master.addLayout(self.layout_first_widgets)
        self.layout_master.addWidget(self.groupbox)
        self.setLayout(self.layout_master)

        self.setWindowTitle("Hello Word")
        self.resize(450,300)

        #icon of application
        self.setWindowIcon(QIcon('../asserts/icon_unix.png'))

    def exibir(self):
        self.text = self.line_edit.text()

        if self.opt_information.isChecked():
            self.message_box = QMessageBox.information(self, "Exemplo 1", self.text)
        elif self.opt_critical.isChecked():
            self.message_box = QMessageBox.critical(self, "Exemplo 1", self.text)
        else:
            self.message_box = QMessageBox.warning(self, "Exemplo 1", self.text)





if __name__ == '__main__':

    # create PyQt5 application project
    app = QApplication([])

    janela = window()

    janela.show()

    sys.exit(app.exec_())