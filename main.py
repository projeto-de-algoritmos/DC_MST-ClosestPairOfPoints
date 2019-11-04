import sys
import signal
from config import *
from window import Window
from PyQt5.QtWidgets import QApplication
from random import randint
from sort_algorithms import MergeSort
from point import Point, PointGenerator
from util import check_cycle
from copy import deepcopy

from closestPairOfPoints import ClosestPairOfPointAlg, ListClosestPoints, ClosestPoint


def print_closest_pair(pair):
    if pair.point1 != None:
        print("( ", pair.point1.index,
              ": {", pair.point1.x, ", ", pair.point1.y, "}, ", end="")
    else:
        print("(None)", end="")
    if pair.point2 != None:
        print(pair.point2.index, ": ",
              "{", pair.point2.x, ", ", pair.point2.y, "} )", end="")
    else:
        print("(None)", end="")
    print(" distance: ", pair.distance, end="")


def init_points(window):
    range_x = SCREEN_WIDTH - POINT_WIDTH
    range_y = SCREEN_HEIGHT - POINT_HEIGHT
    qtt_points = 5

    generator = PointGenerator()
    points = []
    points = generator.generate_points(qtt_points, range_x, range_y)

    sortedPoints = []
    sort = MergeSort(points)
    sortedPoints = sort.sort_x()

    window.add_points(sortedPoints)

    closest_alg = ClosestPairOfPointAlg(sortedPoints)

    # closests_points = closest_alg.generate_minimum_tree(window)

    closests_points = closest_alg.generate_minimum_tree(window)

    print("------------------------ Pares de Pontos Mais Próximos ---------------------")

    for closest_point in closests_points:
        print_closest_pair(closest_point)
        print(", ")
        # window.add_line(closest_point.point1, closest_point.point2)
    print()


def test():
    points = []
    point1 = Point(1, 6)
    point2 = Point(3, 4)
    point3 = Point(5, 2)
    point4 = Point(7, 8)
    points.append(point2)
    points.append(point4)
    points.append(point1)
    points.append(point3)

    sort = MergeSort(points)
    points = sort.sort_x()

    for point in points:
        print("%s, " % (point.index), end="")
    print()


def main():
    App = QApplication(sys.argv)
    window = Window()

    init_points(window)
    # test()

    window.show()
    sys.exit(App.exec_())


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
