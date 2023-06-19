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


class SecondWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(SecondWindow, self).__init__()
        uic.loadUi("UIStartWindows/StartWindowProfeccor.ui", self)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.init_UI()

    def init_UI(self):
        self.pushButton.clicked.connect(self.returnMain)
        self.pushButton_2.clicked.connect(self.close)
        self.process_2.clicked.connect(self.login)

    def close(self):
        sys.exit()
    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if username == 'professor' and password == 'professor123':
            self.hide()
            self.MainWindowP = MainWindowProfessor.Professor()
            self.MainWindowP.show()
        else:
            msg_box = QtWidgets.QMessageBox(self)
            msg_box.setIcon(QtWidgets.QMessageBox.Warning)
            msg_box.setWindowTitle('Ошибка входа')
            msg_box.setText('Неправильный логин или пароль')
            msg_box.setStyleSheet("QMessageBox QLabel { color: white; }")
            msg_box.exec_()

    def returnMain(self):
        self.hide()
        self.secondWindow = StartWindow.UI()
        self.secondWindow.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = SecondWindow()
    window.show()
    app.exec_()
