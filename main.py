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
    print("( ", pair.point1.index,
          ": {", pair.point1.x, ", ", pair.point1.y, "}, ", end="")
    print(pair.point2.index, ": ",
          "{", pair.point2.x, ", ", pair.point2.y, "} )", end="")
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
    sortedPoints = sort.sort_in_x()

    window.add_points(sortedPoints)

    closest_alg = ClosestPairOfPointAlg(sortedPoints)

    closests_points = closest_alg.generate_minimum_tree(window)

    print("------------------------ Pares de Pontos Mais Próximos ---------------------")
    for closest_point in closests_points:
        print_closest_pair(closest_point)
        print(", ")
        # window.add_line(closest_point.point1, closest_point.point2)
    print()


def test():
    points = []
    point1 = Point(1, 2)
    point2 = Point(3, 4)
    point3 = Point(5, 6)
    point4 = Point(7, 8)
    points.append(point1)
    points.append(point2)
    points.append(point3)
    points.append(point4)

    point1.add_neighbor(point2)
    point2.add_neighbor(point1)

    point1.add_neighbor(point4)
    point4.add_neighbor(point1)

    # point1.add_neighbor(point3)
    # point3.add_neighbor(point1)

    point2.add_neighbor(point3)
    point3.add_neighbor(point2)

    # point2.add_neighbor(point4)
    # point4.add_neighbor(point2)

    # cycle
    point3.add_neighbor(point4)
    point4.add_neighbor(point3)

    check_cycle(deepcopy(point1), None)
    for point in points:
        print(point.visited)


def main():
    App = QApplication(sys.argv)
    window = Window()

    init_points(window)

    window.show()
    sys.exit(App.exec_())
    # test()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
