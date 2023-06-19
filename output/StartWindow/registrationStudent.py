import sqlite3
import urllib.parse
import urllib.request
import json
import webbrowser
import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt
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
import StartWindow


class registrationStudent(QMainWindow):
    def __init__(self):
        super(registrationStudent, self).__init__()

        uic.loadUi("UIStartWindows/registrationStudent.ui", self)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.fillComboBox()
        self.init_UI()

    def init_UI(self):
        self.pushButton.clicked.connect(self.returnMain)
        self.pushButton_2.clicked.connect(self.close)
        self.process_2.clicked.connect(self.send_data)

    def returnMain(self):
        self.hide()



    def close(self):
        sys.exit()

    def fillComboBox(self):
        # Подключение к базе данных
        connection = sqlite3.connect('DataBase/competencies.db')
        cursor = connection.cursor()

        # Запрос направлений
        cursor.execute('SELECT direction FROM courses')
        directions = cursor.fetchall()

        # Заполнение ComboBox с направлениями
        self.comboBox.clear()
        for direction in directions:
            self.comboBox.addItem(direction[0])

        # Закрытие соединения с базой данных
        connection.close()

    def send_data(self):
        name = self.lineEdit.text()
        password = self.lineEdit_2.text()
        direction = self.comboBox.currentText()

        data = {
            "name": name,
            "password": password,
            "direction": direction
        }

        # Преобразование данных в формат JSON
        data_json = json.dumps(data).encode('utf-8')

        # URL базы данных Firebase
        url = 'https://wearegods-c4d19-default-rtdb.firebaseio.com/students.json'

        # Отправка POST-запроса с данными
        req = urllib.request.Request(url, data=data_json, method='POST')
        response = urllib.request.urlopen(req)

        if response.getcode() == 200:
            print("Данные успешно отправлены в базу данных")
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle('Успех')
            msg_box.setText('Данные успешно отправлены в базу данных')

            # Установка стиля текста


            # Установка иконки
            msg_box.setIcon(QtWidgets.QMessageBox.Information)

            # Отображение QMessageBox
            msg_box.exec_()
            self.hide()
        else:
            print("Ошибка при отправке данных")


def main():
    app = QtWidgets.QApplication([])  # функции работы дизайна
    application = registrationStudent()  # передаем наши правила оформелния дизайна
    application.show()  # открытие программы
    sys.exit(app.exec_())  # закрытие программы


if __name__ == '__main__':  # по стилистике и правилам оформления указываем main в которую занесены основные функции
    main()