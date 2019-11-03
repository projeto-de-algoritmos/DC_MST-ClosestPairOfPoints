from config import *
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen, QPixmap
from PyQt5.QtCore import Qt, QPoint


class Point:
    def __init__(self, panel):
        painter = QPainter(panel)
        painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.white, Qt.DiagCrossPattern))
        painter.drawEllipse(100, 150, 80, 80)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.drawing = False
        self.lastPoint = QPoint()
        self.image = QPixmap("assets/picture.jpeg")
        self.setGeometry(100, 100, SCREEN_WIDTH, SCREEN_HEIGHT)
        # self.resize(self.image.width(), self.image.height())
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        # painter.drawPixmap(self.rect(), self.image)
        self.arcTest = Point(self)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        painter = QPainter(self.image)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        if event.buttons() and Qt.LeftButton and self.drawing:
            painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False
