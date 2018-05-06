
import sys
from PyQt4.QtGui import *

def janela():
    # create PyQt4 application project
    app = QApplication(sys.argv)

    # The QWidget is the base class of all user interace objetcs in PyQt4
    window = QWidget()

    # set window size
    window.resize(480, 320)

    # set Window title
    window.setWindowTitle("Hello World!")

    # show window
    window.show()

    sys.exit(app.exec_())



def windows():

    app = QApplication(sys.argv)
    button = QPushButton("Hello World", None)
    button.show()
    app.exec_()


if __name__ == '__main__':
    janela()