import sys
import signal
from config import *
from window import Window
from PyQt5.QtWidgets import QApplication
from random import randint
from sort_algorithms import MergeSort
from point import Point, PointGenerator

from closestPairOfPoints import ClosestPairOfPointAlg, ListClosestPoints, ClosestPoint


def print_closest_pair(pair):
    print("( {", pair.point1.x, ", ", pair.point1.y, "}", end="")
    print("{", pair.point2.x, ", ", pair.point2.y, "} )", end="")


def main():
    App = QApplication(sys.argv)
    window = Window()

    range_x = SCREEN_WIDTH - POINT_WIDTH
    range_y = SCREEN_HEIGHT - POINT_HEIGHT
    qtt_points = 20

    generator = PointGenerator()
    points = generator.generate_points(qtt_points, range_x, range_y)

    sortedPoints = []
    sort = MergeSort(points)
    sortedPoints = sort.sort_in_x()

    window.add_points(sortedPoints)

    closest_alg = ClosestPairOfPointAlg(sortedPoints)

    print("------------------------ Pares de Pontos Mais Próximos ---------------------")
    closests_points = closest_alg.generate_minimum_tree()

    for closest_point in closests_points:
        print_closest_pair(closest_point)
        print(", ")
        window.add_line(closest_point.point1, closest_point.point2)
    print()

    sys.exit(App.exec_())


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
