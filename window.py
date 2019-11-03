from config import *
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen, QPixmap
from PyQt5.QtCore import Qt, QPoint, QRectF
from point import Point


class LineClosestPoint:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, painter):
        # print("point x: ", self.point1.center_x)
        painter.drawLine(self.point1.center_x, self.point1.center_y,
                         self.point2.center_x, self.point2.center_y)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.drawing = False
        self.lastPoint = QPoint()
        self.image = QPixmap("assets/picture.jpeg")
        self.setGeometry(100, 100, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.show()

        self.points = []
        self.lines = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)
        painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.white, Qt.DiagCrossPattern))

        for point in self.points:
            point.draw(painter)

        count = 1
        for line in self.lines:
            count += 1
            line.draw(painter)

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

    def add_point(self, point):
        point.width = POINT_WIDTH
        point.height = POINT_HEIGHT
        self.points.append(point)

    def add_points(self, points):

        for point in points:
            point.width = POINT_WIDTH
            point.height = POINT_HEIGHT
        self.points.extend(points)

    def add_line(self, point1, point2):
        self.lines.append(LineClosestPoint(point1, point2))
