
from PyQt5.QtWidgets import QWidget, QProgressBar, QApplication, QVBoxLayout, QPushButton
from PyQt5.QtCore import QBasicTimer
import sys

class Window(QWidget):

    # contrutor da classe janela
    def __init__(self, parent=None):
        super(Window, self).__init__()
        self.set_settings()
        self.create_widgets()
        self.run = True

    # definindo o tamanho da janela
    def set_settings(self):
        self.resize(350,200)

    def create_widgets(self):
        self.progress_bar = QProgressBar(self)
        #self.progress_bar.setFixedWidth(300)
        #self.progress_bar.move(50,80)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.progress_bar)
        self.setLayout(self.layout)

        # timer creator
        self.timer = QBasicTimer()
        self.step = 0
        self.timer.start(100, self)

        # BUTTON
        self.button = QPushButton()
        self.button.setText("Stop")
        self.button.clicked.connect(self.stop_timer_event)
        self.layout.addWidget(self.button)

    def stop_timer_event(self):

        if self.run:
            self.timer.stop()
            self.button.setText("Start")
            self.run = False

        else:
            print('else')
            self.run = True
            self.timerEvent(self)


    def resume_time(self, QTimerEvent):
        self.button.setText("Stop")
        self.timer.start(self.step, self)
        self.step += 1
        self.progress_bar.setValue(self.step)

    def timerEvent(self, QTimerEvent):
        if self.step >= 100:
            self.timer.stop()

        if self.run is True:
            self.step += 1
            self.progress_bar.setValue(self.step)


if __name__ == '__main__':
    app = QApplication([])

    janela = Window()
    janela.show()

    sys.exit(app.exec_())