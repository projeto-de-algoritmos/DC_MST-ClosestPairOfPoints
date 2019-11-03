from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QPen, QPixmap


class LineClosestPoint:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, painter):
        painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))
        painter.drawLine(self.point1.center_x, self.point1.center_y,
                         self.point2.center_x, self.point2.center_y)
