
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class window(QWidget):

    #constutor
    def __init__(self, parent=None):

        super(window, self).__init__(parent)
        self.setWindowTitle("Hello Word")
        self.resize(450,300)

        #icon of application
        self.setWindowIcon(QIcon('../asserts/icon_unix.png'))



if __name__ == '__main__':

    # create PyQt5 application project
    app = QApplication([])

    janela = window()

    janela.show()

    sys.exit(app.exec_())

