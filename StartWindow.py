
import matplotlib
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QVBoxLayout, QLabel
from PyQt5 import uic, QtWidgets
import sys
from PyQt5.QtCore import Qt
import StartWindowStudent
import StartWindowProfeccor


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        mpl_data_dir = matplotlib.get_data_path()
        datas = [
            (mpl_data_dir, "matplotlib/mpl-data"),
        ]
        uic.loadUi("UIStartWindows/StartWindows.ui", self)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.init_UI()

    def init_UI(self):
        self.process.clicked.connect(self.openSecondForm)
        self.process_2.clicked.connect(self.openSecondForm1)
        self.pushButton_2.clicked.connect(self.close)


    def openSecondForm(self):
        self.hide()
        self.secondWindow = StartWindowProfeccor.SecondWindow()
        self.secondWindow.show()

    def close(self):
        sys.exit()

    def openSecondForm1(self):
        self.hide()
        self.secondWindow = StartWindowStudent.SecondForm1()
        self.secondWindow.show()
def main():
    app = QtWidgets.QApplication([])  # функции работы дизайна
    application = UI()  # передаем наши правила оформелния дизайна
    application.show()  # открытие программы
    sys.exit(app.exec_())  # закрытие программы


if __name__ == '__main__':  # по стилистике и правилам оформления указываем main в которую занесены основные функции
    main()