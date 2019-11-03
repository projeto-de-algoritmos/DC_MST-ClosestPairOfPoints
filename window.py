from config import *
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen, QPixmap
from PyQt5.QtCore import Qt, QPoint, QRectF, QTimer
from point import Point
from line import LineClosestPoint


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.drawing = False
        self.lastPoint = QPoint()
        self.image = QPixmap("assets/picture.jpg")
        self.setGeometry(100, 100, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.show()

        self.points = []
        self.lines = []

    def paintEvent(self, event=None):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)
        painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.DiagCrossPattern))

        for line in self.lines:
            line.draw(painter)

        for point in self.points:
            point.draw(painter)

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

    def animation_add_lines(self, lines):
        self.pendent_animation_lines = lines
        self.timer = QTimer(
            self, timeout=self.update_animation_line, interval=2000)
        self.timer.start()

    @QtCore.pyqtSlot()
    def update_animation_line(self):
        # self.m_rect_rain.moveTop(self.m_rect_rain.top() + 5)
        if len(self.pendent_animation_lines) > 0:
            self.lines.append(self.pendent_animation_lines.pop(0))
            self.update()
        else:
            self.timer.stop()
