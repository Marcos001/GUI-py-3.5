# Importing necessary libraries, mainly the OpenCV, and PyQt libraries
import cv2
import numpy as np
import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal


class ShowVideo(QtCore.QObject):
    # initiating the built in camera
    camera_port = 0
    camera = cv2.VideoCapture(camera_port)
    VideoSignal = QtCore.pyqtSignal(QtGui.QImage)

    def __init__(self, parent=None):
        super(ShowVideo, self).__init__(parent)

    @QtCore.pyqtSlot()
    def startVideo(self):
        arqCasc = '/home/nig/PycharmProjects/GUI-py-3.5/asserts/haarcascade_frontalface_default.xml'
        faceCascade = cv2.CascadeClassifier(arqCasc)
        run_video = True
        while run_video:

            ret, image = self.camera.read()

            image = cv2.flip(image, 180)  # espelha a imagem

            faces = faceCascade.detectMultiScale(
                image,
                minNeighbors=5,
                minSize=(30, 30),
                maxSize=(200, 200)
            )

            # Desenha um retângulo nas faces detectadas
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            color_swapped_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            height, width, _ = color_swapped_image.shape



            qt_image = QtGui.QImage(color_swapped_image.data,
                                    width,
                                    height,
                                    color_swapped_image.strides[0],
                                    QtGui.QImage.Format_RGB888)

            self.VideoSignal.emit(qt_image)

            #



class ImageViewer(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)
        self.image = QtGui.QImage()
        self.setAttribute(QtCore.Qt.WA_OpaquePaintEvent)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.image)
        self.image = QtGui.QImage()

    def initUI(self):
        self.setWindowTitle('Test')

    @QtCore.pyqtSlot(QtGui.QImage)
    def setImage(self, image):
        if image.isNull():
            print("Viewer Dropped frame!")

        self.image = image
        if image.size() != self.size():
            self.setFixedSize(image.size())
        self.update()

def close_app():
    sys.exit(0)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    thread = QtCore.QThread()
    thread.start()
    vid = ShowVideo()
    vid.moveToThread(thread)
    image_viewer = ImageViewer()

    vid.VideoSignal.connect(image_viewer.setImage)

    # Button to start the videocapture:

    push_iniciar_video = QtWidgets.QPushButton('Iniciar Video')
    push_detectar = QtWidgets.QPushButton('Detectar')

    push_iniciar_video.clicked.connect(vid.startVideo)
    push_detectar.clicked.connect(close_app)

    vertical_layout = QtWidgets.QVBoxLayout()

    vertical_layout.addWidget(image_viewer)
    vertical_layout.addWidget(push_iniciar_video)
    vertical_layout.addWidget(push_detectar)

    layout_widget = QtWidgets.QWidget()
    layout_widget.setLayout(vertical_layout)

    main_window = QtWidgets.QMainWindow()
    main_window.setCentralWidget(layout_widget)
    main_window.show()
    sys.exit(app.exec_())