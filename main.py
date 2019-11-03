import sys
import signal
from config import *
from window import Window
from PyQt5.QtWidgets import QApplication
from random import randint


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def create_point(range_x=0, range_y=0, points=[]):

    while(True):
        x = randint(0, range_x)
        y = randint(0, range_y)
        invalid = False
        for point in points:
            if x == point.x:
                invalid = True
                break
            if y == point.y:
                invalid = True
                break

        if invalid is False:
            return Point(x, y)


def main():
    App = QApplication(sys.argv)
    window = Window()

    points = []

    range_x = SCREEN_WIDTH - POINT_WIDTH
    range_y = SCREEN_HEIGHT - POINT_HEIGHT
    qtt_points = 10

    for i in range(qtt_points):
        points.append(create_point(range_x, range_y, points))

    window.add_points(points)

    sys.exit(App.exec_())


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
