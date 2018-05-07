
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QFileDialog, QHBoxLayout)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class HandlerWindow(QWidget):
    def __init__(self, parent=None):
        super(HandlerWindow, self).__init__(parent)

        self.altura = 300
        self.largura = 350

        self.resize(self.altura,self.largura)
        self.label = CustomLabel(self)
        self.label.setStyleSheet("background-color:rgb(255,200,0)");
        self.label.setPixmap(QPixmap("../asserts/icon_unix.png").scaled(self.largura,self.altura,
                                    Qt.KeepAspectRatio))

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)


class CustomLabel(QLabel):
    def __init__(self, parent=None):
        super(CustomLabel, self).__init__(parent)
        self.setMouseTracking(True)


    def mouseMoveEvent(self, e):
        QApplication.setOverrideCursor(Qt.PointingHandCursor)


    def mousePressEvent(self, QMouseEvent):
        img, re = QFileDialog.getOpenFileName(self, "Selecionar Arquivo", filter="All(*.png, *.jpg)")
        if re:
            self.setPixmap(QPixmap(img).scaled(300, 350, Qt.KeepAspectRatio))


    def leaveEvent(self, QEvent):
        QApplication.setOverrideCursor(Qt.ArrowCursor)


if __name__ == '__main__':

    # create PyQt5 application project
    app = QApplication([])

    janela = HandlerWindow()

    janela.show()

    sys.exit(app.exec_())