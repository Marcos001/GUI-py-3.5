

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QGridLayout, QFileDialog, QHBoxLayout)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
import sys, os


class mainWindow(QWidget):

    def __init__(self, parent=None):
        """
        contrutor da classe
        :param parent:
        """
        super(mainWindow, self).__init__()
        self.preview_screen = QApplication.primaryScreen().grabWindow(0)

        # funcoes implementadas para configuração da GUI e acoes
        self.settings()       #
        self.create_widgets() #
        self.set_layout()     #


    def settings(self):
        """
         insere configurações para a nossa janela
        """
        self.resize(320, 200)
        self.setWindowTitle('Screenshoter')


    def create_widgets(self):
        """
        cria e configura os widgets necessários
        """
        self.img_preview =  QLabel()
        self.img_preview.setPixmap(self.preview_screen.scaled(350,350, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        self.bnt_save_screenshort = QPushButton('save Screenshot')
        self.bnt_save_screenshort.setStyleSheet("background-color:rgb(30,144,255)")

        self.bnt_new_screenshort = QPushButton('New screenshot')
        self.bnt_new_screenshort.setStyleSheet("background-color:rgb(30,144,255)")

        # signals connections
        self.bnt_save_screenshort.clicked.connect(self.save_screenshot)
        self.bnt_new_screenshort.clicked.connect(self.new_screenshot)


    def set_layout(self):
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.img_preview, 0, 0, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.bnt_new_screenshort, 2, 0, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.bnt_save_screenshort, 2, 0, alignment=Qt.AlignRight)
        self.setLayout(self.layout)


    def save_screenshot(self):

        img, _ = QFileDialog.getSaveFileName(None, "Salvar imagem", os.getcwd()+"/", "PNG(*.png);; JPEG(*.jpg)")

        if img[-3:] == 'png':
            self.preview_screen.save(img, "png")
        elif img[-3:] == 'jpg':
            self.preview_screen.save(img, "jpg")


    def new_screenshot(self):
        self.hide()
        QTimer.singleShot(1000, self.take_screenshot)


    def take_screenshot(self):
        self.preview_screen = QApplication.primaryScreen().grabWindow(0)
        self.img_preview.setPixmap(self.preview_screen.scaled(350,350,
                                    Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.show()

def main():
    ""
    root = QApplication([])
    app = mainWindow()
    app.show()
    sys.exit(root.exec_())

main()