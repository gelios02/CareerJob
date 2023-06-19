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

class Professor(QtWidgets.QMainWindow):
    def __init__(self):
        super(Professor, self).__init__()
        uic.loadUi("UIStartWindows/MainWindowProfessor.ui", self)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.fillComboBox()
        self.radioButton_2.setChecked(True)

        # Устанавливаем иконку для стрелки вниз в QComboBox
        self.init_UI()

    def init_UI(self):
        self.pushButton.clicked.connect(self.returnMain)
        self.pushButton_2.clicked.connect(self.close)
        self.process_2.clicked.connect(self.searchCompetencies)
        self.checkBox.clicked.connect(self.selectAllCheckBoxes)
        self.process_3.clicked.connect(self.registration)
        self.process_4.clicked.connect(self.parseVacancies)
        self.process_5.clicked.connect(self.showGraph)

    def close(self):
        sys.exit()
    def returnMain(self):
        self.hide()
        self.secondWindow = StartWindow.UI()
        self.secondWindow.show()

    def registration(self):
        self.secondWindow = registrationStudent.registrationStudent()
        self.secondWindow.show()

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

    def updateSearchMode(self):
        # Очистка полей и списка компетенций
        self.lineEdit.clear()
        self.listWidget.clear()

    def searchCompetencies(self):
        if self.radioButton_2.isChecked():
            selected_direction = self.comboBox.currentText()

            # Очистка списка компетенций
            self.listWidget.clear()

            # Подключение к базе данных
            connection = sqlite3.connect('DataBase/competencies.db')
            cursor = connection.cursor()

            # Поиск соответствующего направления
            cursor.execute('SELECT id, code FROM courses WHERE direction = ?', (selected_direction,))
            course_info = cursor.fetchone()

            if course_info is not None:
                course_id = course_info[0]
                code = course_info[1]

                # Заполнение поля ввода кода
                self.lineEdit.setText(str(code))

                # Получение связанных компетенций
                cursor.execute('SELECT name FROM competencies WHERE course_id = ?', (course_id,))
                competency_list = cursor.fetchall()

                for competency in competency_list:
                    item = QtWidgets.QListWidgetItem()
                    check_box = QtWidgets.QCheckBox(competency[0])
                    check_box.setStyleSheet("color:white")
                    self.listWidget.addItem(item)
                    self.listWidget.setItemWidget(item, check_box)

            # Закрытие соединения с базой данных
            connection.close()
        elif self.radioButton.isChecked():
            selected_code = self.lineEdit.text()

            # Подключение к базе данных
            connection = sqlite3.connect('DataBase/competencies.db')
            cursor = connection.cursor()

            # Поиск соответствующего кода
            cursor.execute('SELECT id, direction FROM courses WHERE code = ?', (selected_code,))
            course_info = cursor.fetchone()

            if course_info is not None:
                course_id = course_info[0]
                direction = course_info[1]

                # Установка выбранного направления в ComboBox
                index = self.comboBox.findText(direction)
                if index != -1:
                    self.comboBox.setCurrentIndex(index)

                # Получение связанных компетенций
                cursor.execute('SELECT name FROM competencies WHERE course_id = ?', (course_id,))
                competency_list = cursor.fetchall()

                # Очистка списка компетенций
                self.listWidget.clear()

                for competency in competency_list:
                    item = QtWidgets.QListWidgetItem()
                    check_box = QtWidgets.QCheckBox(competency[0])
                    check_box.setStyleSheet("color:white")
                    self.listWidget.addItem(item)
                    self.listWidget.setItemWidget(item, check_box)

            # Закрытие соединения с базой данных
            connection.close()

    def selectAllCheckBoxes(self):
        selected = self.checkBox.isChecked()

        for index in range(self.listWidget.count()):
            item = self.listWidget.item(index)
            check_box = self.listWidget.itemWidget(item)

            check_box.setChecked(selected)

    def parseVacancies(self):
        # Очистка списка вакансий
        self.listWidget_2.clear()

        # Получение выбранных компетенций
        selected_competencies = []
        for index in range(self.listWidget.count()):
            item = self.listWidget.item(index)
            check_box = self.listWidget.itemWidget(item)
            if check_box.isChecked():
                selected_competencies.append(check_box.text())
        print(selected_competencies)
        # Формирование параметров запроса
        search_params = {
            'text': ' OR '.join(selected_competencies),  # Объединяем компетенции с оператором OR
            'per_page': 30  # Ограничиваем количество вакансий до 10
        }
        query_string = urllib.parse.urlencode(search_params)

        # Формирование URL-адреса API HeadHunter
        url = f"https://api.hh.ru/vacancies?{query_string}"

        # Отправка HTTP-запроса и получение данных
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())

        # Обработка полученных данных
        vacancies = data.get('items', [])
        print(vacancies)
        self.listWidget_2.clear()

        # Создание стиля для элементов списка
        item_style = """
                   QLabel {
                       font-size: 16px;
                       color: white;
                   }
                   QLabel a {
                       color: white;
                       font-size: 16px;
                       text-decoration: none;
                   }
               """

        # Создание элементов списка вакансий
        for vacancy in vacancies:
            title = vacancy.get('name')
            salary = vacancy.get('salary')
            url = vacancy.get('alternate_url')

            # Получение значений from, to и currency
            from_salary = salary.get('from') if salary else ''
            to_salary = salary.get('to') if salary else ''
            currency = salary.get('currency') if salary else ''

            # Создание пользовательского виджета для элемента списка
            widget = QtWidgets.QWidget()
            layout = QtWidgets.QHBoxLayout(widget)
            layout.setContentsMargins(0, 0, 0, 0)
            label = QtWidgets.QLabel()
            label.setStyleSheet(item_style)
            layout.addWidget(label)
            widget.setLayout(layout)

            # Установка данных в элементы списка
            label.setText(f'<a href="{url}" style="color: #9966cc;">{title}</a> '
                          f'({from_salary} - {to_salary} {currency})')
            label.setOpenExternalLinks(True)

            # Создание элемента списка и добавление пользовательского виджета
            item = QtWidgets.QListWidgetItem(self.listWidget_2)
            item.setSizeHint(widget.sizeHint())
            self.listWidget_2.addItem(item)
            self.listWidget_2.setItemWidget(item, widget)

        self.listWidget_2.itemClicked.connect(self.openVacancyUrl)

    def openVacancyUrl(self, item):
        url = item.data(QtCore.Qt.UserRole)
        if url:
            webbrowser.open(url)

    def showGraph(self):
        # Получение выбранных компетенций
        try:
            selected_competencies = []
            for index in range(self.listWidget.count()):
                item = self.listWidget.item(index)
                check_box = self.listWidget.itemWidget(item)
                if check_box.isChecked():
                    selected_competencies.append(check_box.text())

            # Получение данных о востребованности с сайта HH
            vacancies_data = self.fetchVacanciesData(selected_competencies)
            print(vacancies_data)

            # Создание данных для графика
            x = range(len(selected_competencies))
            y = [vacancies_data[competency] for competency in selected_competencies]
            print(x,y)
            # Очистка графического представления
            # self.graphicsView.scene().clear()

            fig, ax = plt.subplots()
            ax.bar(x, y)
            ax.set_xticks(x)
            ax.set_xticklabels(selected_competencies, rotation=45)
            ax.set_xlabel("Компетенции")
            ax.set_ylabel("Востребованность")

            # Преобразование графика в изображение
            fig.canvas.draw()
            width, height = fig.canvas.get_width_height()
            image = QImage(fig.canvas.buffer_rgba(), width, height, QImage.Format_ARGB32)

            # Отображение изображения в элементе graphicsView
            scene = QtWidgets.QGraphicsScene()
            pixmap = QPixmap.fromImage(image)
            scene.addPixmap(pixmap)
            self.graphicsView.setScene(scene)
            self.graphicsView.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
        except Exception as e:
            msg_box = QtWidgets.QMessageBox(self)
            msg_box.setIcon(QtWidgets.QMessageBox.Warning)
            msg_box.setWindowTitle('Отсутсвует')
            msg_box.setText('Статистика по данной компетенции отсутсвует')
            msg_box.setStyleSheet("QMessageBox QLabel { color: white; }")
            msg_box.exec_()



    def fetchVacanciesData(self, competencies):
        vacancies_data = {}

        for competency in competencies:
            url = f"https://api.hh.ru/vacancies?text={competency}"
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                vacancies_data[competency] = data.get('found', 0)

        return vacancies_data

    def figure_to_scene(self, fig):
        canvas = FigureCanvas(fig)
        canvas.draw()

        scene = QtWidgets.QGraphicsScene()
        scene.setSceneRect(0, 0, fig.get_figwidth(), fig.get_figheight())

        item = QtWidgets.QGraphicsProxyWidget()
        item.setWidget(canvas)
        item.setPos(0, 0)
        scene.addItem(item)

        return scene


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Professor()
    window.show()
    app.exec_()

