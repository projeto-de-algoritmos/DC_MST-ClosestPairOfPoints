from random import randint
from config import *


class Point:
    def __init__(self, x, y, width=0, height=0):
        self.x = x
        self.y = y
        self.__width = width
        self.__height = height
        self.center_x = width / 2 + x
        self.center_y = height / 2 + y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width
        self.center_x = width / 2 + self.x

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height
        self.center_y = height / 2 + self.y

    def draw(self, painter):
        painter.drawEllipse(self.x, self.y, self.__width, self.__height)


class PointGenerator:
    def __init__(self):
        self.points = []

    def create_point(self, range_x=0, range_y=0, points=[]):
        valid = False
        count = 0
        while(valid is False):
            x = randint(0, range_x)
            y = randint(0, range_y)

            if len(points) == 0:
                valid = True
                break

            for point in points:
                if abs(x - point.x) <= POINT_WIDTH and abs(y - point.y) <= POINT_HEIGHT:
                    valid = False
                    break
                valid = True
            count += 1

            if count >= 100:
                print("Número de pontos é muito grande para o espaço")
                exit()

        return Point(x, y)

    def generate_points(self, qtt_points, range_x, range_y):
        self.points = []

        for i in range(qtt_points):
            self.points.append(self.create_point(
                range_x, range_y, self.points))

        return self.points
