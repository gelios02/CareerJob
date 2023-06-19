import sqlite3

import urllib.parse
import urllib.request
import json
import webbrowser
import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QVBoxLayout, QLabel
from PyQt5 import uic, QtWidgets
import sys
from PyQt5 import QtGui
import asyncio
import aiohttp
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.uic.properties import QtCore, QtGui
import registrationStudent
import StartWindow
import MainWindowsStudent
import MainWindowProfessor
import registrationStudent
import StartWindowStudent
import StartWindowProfeccor
import StartWindow

class SecondForm1(QMainWindow):
    credentialsMatched = pyqtSignal(str, str)
    def __init__(self):
        super(SecondForm1, self).__init__()

        uic.loadUi("UIStartWindows/StartWindowsStudent.ui", self)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.init_UI()

    def init_UI(self):
        self.pushButton.clicked.connect(self.returnMain)
        self.pushButton_2.clicked.connect(self.close)
        self.process_2.clicked.connect(self.check_credentials)

    def close(self):
        sys.exit()

    def returnMain(self):
        self.hide()
        self.secondWindow = StartWindow.UI()
        self.secondWindow.show()

    def check_credentials(self):
        name = self.lineEdit.text()  # Получение введенного имени из lineEdit
        password = self.lineEdit_2.text()  # Получение введенного пароля из lineEdit_2

        url = 'https://wearegods-c4d19-default-rtdb.firebaseio.com/students.json'  # Ссылка на вашу базу данных

        try:
            with urllib.request.urlopen(url) as response:
                data = json.loads(response.read())

                # Поиск совпадения имени и пароля в данных
                for key, value in data.items():
                    if value['name'] == name and value['password'] == password:
                        name = value['name']
                        direction = value['direction']
                        with open('DataBase/data.json', 'w') as file:
                            file.truncate(0)
                            file.seek(0)
                        data = {
                            'name': name,
                            'direction': direction
                        }
                        json_data = json.dumps(data, ensure_ascii=False).encode('utf-8')
                        # Запись данных в файл с указанием кодировки UTF-8
                        with open('DataBase/data.json', 'wb') as file:
                            file.write(json_data)
                        self.hide()
                        self.secondWindow = MainWindowsStudent.registrationStudent()
                        self.secondWindow.show()
                        return
                else:
                    msg_box = QtWidgets.QMessageBox(self)
                    msg_box.setIcon(QtWidgets.QMessageBox.Warning)
                    msg_box.setWindowTitle('Ошибка входа')
                    msg_box.setText('Неправильный логин или пароль')
                    msg_box.setStyleSheet("QMessageBox QLabel { color: white; }")
                    msg_box.exec_()
        except urllib.error.URLError as e:
            print("Ошибка при выполнении запроса:", e)


def main():
    app = QtWidgets.QApplication([])  # функции работы дизайна
    application = SecondForm1()  # передаем наши правила оформелния дизайна
    application.show()  # открытие программы
    sys.exit(app.exec_())  # закрытие программы


if __name__ == '__main__':  # по стилистике и правилам оформления указываем main в которую занесены основные функции
    main()