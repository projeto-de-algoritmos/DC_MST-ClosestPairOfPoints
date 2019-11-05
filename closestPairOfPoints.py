import math
import time
from copy import deepcopy
from util import check_cycle
from line import LineClosestPoint
from sort_algorithms import MergeSort


def euclideanDistance(point1, point2): return math.sqrt(
    abs(point1.x - point2.x)**2 + abs(point1.y - point2.y)**2)


class ClosestPoint:
    def __init__(self, point1, point2, distance):
        self.point1 = point1
        self.point2 = point2
        self.distance = distance


class ListClosestPoints:
    def __init__(self, list, closestPoints):
        self.list = list
        self.closestPoints = closestPoints


class ClosestPairOfPointAlg:
    def __init__(self, list):
        self.sorted_list_x = list

    def search(self, window):
        sortedList = deepcopy(self.sorted_list_x)

        result = self.__closest_pair(sortedList)
        lines = [LineClosestPoint(
            result.point1,
            result.point2)]

        window.animation_add_lines(lines)
        return result

    def generate_minimum_tree(self, window):
        sortedList = deepcopy(self.sorted_list_x)

        self.black_list = []
        tree = []
        lines = []

        for index in range(len(sortedList) - 1):
            self.__print_blacklist()

            result = self.__closest_pair(sortedList)
            tree.append(result)
            self.black_list.append(result)

            if result.point1 is not None and result.point2 is not None:
                lines.append(LineClosestPoint(result.point1,
                                              result.point2))

        window.animation_add_lines(lines)

        return tree

    def __closest_pair(self, list):
        if len(list) <= 1:
            return ClosestPoint(None, None, math.inf)

        line = list[int(len(list)/2)]

        closest1 = self.__closest_pair(list[0:int(len(list)/2)])
        closest2 = self.__closest_pair(list[int(len(list)/2):len(list)])
        closest = self.__min_closest(closest1, closest2)

        self.__delete_points(list, line, closest)

        sort = MergeSort(list)
        list_sorted_y = sort.sort_y()
        self.print_list(list_sorted_y)

        print("\nInit Compare Next 7\n")
        for i in range(len(list_sorted_y) - 1):
            closest_t = self.compare_next_seven_points(
                i, list_sorted_y, closest)
            if closest_t.distance < closest.distance:
                if self.__verify_black_list(closest_t.point1, closest_t.point2):
                    closest = closest_t
        print("\nEnd Compare Next 7\n")

        return closest

    def print_list(self, list):
        print("\nOrdered List Y")

        print("[ ", end="")
        for point in list:
            print("{%s: %s, %s}, " % (point.index, point.x, point.y), end="")
        print(" ]\n")

    def __delete_points(self, list, line, closest):
        for point in list:
            if abs(point.x - line.x) > closest.distance:
                list.remove(point)

    def __min_closest(self, closest1, closest2):
        if closest2.distance < closest1.distance:
            if self.__verify_black_list(closest2.point1, closest2.point2):
                return closest2
        if self.__verify_black_list(closest1.point1, closest1.point2):
            return closest1

        return ClosestPoint(None, None, math.inf)

    def __verify_black_list(self, point1, point2):
        if point1 is None or point2 is None:
            return False

        print("verify blacklist {%s, %s}" % (point1.index, point2.index))
        for elem in self.black_list:
            if ((point1.index == elem.point1.index and point2.index == elem.point2.index) or
                    (point2.index == elem.point1.index and point1.index == elem.point2.index)):
                print("Já na BlackList")
                return False
        print("Livre")
        return True

    def compare_next_seven_points(self, index, list, current_closest):

        possibleRange = index + 8 if index + 8 <= len(list) else len(list)

        for indexCount in range(index + 1, possibleRange):
            distance = euclideanDistance(list[index], list[indexCount])
            print("current: ", distance)
            print("min: ", distance)
            if distance < current_closest.distance:
                print("add")
                if self.__verify_black_list(list[index], list[indexCount]):
                    current_closest.point1 = list[index]
                    current_closest.point2 = list[indexCount]
                    current_closest.distance = distance

        return current_closest

    def __print_blacklist(self):
        print("\n---------------------------------------------------")
        print("black_list")

        print("[ ", end="")
        for pair in self.black_list:
            print("( ", end="")
            print("%s: { %s, %s}, " % (pair.point1.index,
                                       pair.point1.x, pair.point1.y), end="")
            print("%s: { %s, %s}, " % (pair.point2.index,
                                       pair.point2.x, pair.point2.y), end="")
            print(" ), ", end="")
        print(" ]")
