import math
import time
from copy import deepcopy
from util import check_cycle
from line import LineClosestPoint


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

    def search(self):
        sortedList = deepcopy(self.sorted_list_x)

        result = self.__merge_in_x(0, len(sortedList) - 1, sortedList)
        return result.closestPoints

    def __print_blacklist(self, black_list):
        print("\n-------------------------------")
        print("black_list")

        print("[ ", end="")
        for pair in black_list:
            print("( ", end="")
            print("%s: { %s, %s}, " % (pair.point1.index,
                                       pair.point1.x, pair.point1.y), end="")
            print("%s: { %s, %s}, " % (pair.point2.index,
                                       pair.point2.x, pair.point2.y), end="")
            print(" ), ", end="")
        print(" ]")

    def generate_minimum_tree(self, window):
        sortedList = deepcopy(self.sorted_list_x)

        tree = []
        lines = []

        for index in range(len(sortedList) - 1):
            result = self.__merge_in_x(
                0, len(sortedList) - 1, sortedList, tree)
            tree.append(result.closestPoints)

            lines.append(LineClosestPoint(result.closestPoints.point1,
                                          result.closestPoints.point2))

            self.__print_blacklist(tree)

        window.animation_add_lines(lines)
        # check_cycle(deepcopy(tree[0].point1), None)

        return tree

    def __off_black_list(self, point1, point2, distance, black_list=[]):
        print('( %s: {%s, %s}, ' % (point1.index, point1.x, point1.y), end="")
        print('%s: {%s, %s} ) = %s' %
              (point2.index, point2.x, point2.y, distance))

        for pair in black_list:
            if ((point1.index == pair.point1.index and point2.index == pair.point2.index) or
                    (point2.index == pair.point1.index and point1.index == pair.point2.index)):
                print("Já está na black list")
                return False
        print("Livre")
        return True

    def new_closest_pair(self, point1, point2, distance):
        closestPoint = ClosestPoint(point1, point2, distance)
        point1.add_neighbor(point2)
        point2.add_neighbor(point1)
        return closestPoint

    def check_cycle_on_add_closest_pair(self, point1, point2, distance):
        test_points = deepcopy(self.sorted_list_x)
        test_point1 = deepcopy(point1)
        test_point2 = deepcopy(point2)

        closest = self.new_closest_pair(point1, point2, distance)
        check_cycle(test_point1, None)
        pass

    def __merge_list_in_y(self, list_closest_points1: list,
                          list_closest_points2: list, black_list=[]) -> list:
        count1 = 0
        count2 = 0

        list1 = list_closest_points1.list
        list2 = list_closest_points2.list

        closestPoint = ClosestPoint(None, None, math.inf)
        resultList = ListClosestPoints([], closestPoint)

        while(count1 < len(list1) or count2 < len(list2)):
            if count1 >= len(list1):
                resultList.list.extend(list2[count2:])
                break
            elif count2 >= len(list2):
                resultList.list.extend(list1[count1:])
                break
            elif (list2[count2].y < list1[count1].y):
                resultList.list.append(list2[count2])

                distance = euclideanDistance(list1[count1], list2[count2])

                if (distance < closestPoint.distance):
                    if self.__off_black_list(list1[count1], list2[count2], distance, black_list):
                        closestPoint = self.new_closest_pair(
                            list1[count1], list2[count2], distance)

                if count2 < len(list2):
                    count2 += 1
            else:
                resultList.list.append(list1[count1])

                distance = euclideanDistance(list1[count1], list2[count2])
                if distance < closestPoint.distance:
                    if self.__off_black_list(list1[count1], list2[count2], distance, black_list):
                        closestPoint = self.new_closest_pair(
                            list1[count1], list2[count2], distance)

                if count1 < len(list1):
                    count1 += 1

        return resultList

    def __merge_in_x(self, begin, end, sortList: list, black_list=[]) -> ListClosestPoints:
        part1 = []
        part2 = []
        partialList = []

        closestPoint = ClosestPoint(None, None, math.inf)

        if (begin < end):
            print("\nIn Compare In Merge")
            part1 = self.__merge_in_x(
                begin, int((begin + end) / 2), sortList)
            part2 = self.__merge_in_x(
                int((begin + end) / 2) + 1, end, sortList)
            partialList = self.__merge_list_in_y(part1, part2, black_list)

            testList = partialList.list
            closestPoint = partialList.closestPoints

            print("\nIn Compare Next Seven")
            for indexPoint in range(len(testList)):
                closestPointTest = self.compare_next_seven_points(
                    indexPoint, testList)

                if closestPointTest.distance < closestPoint.distance:
                    if self.__off_black_list(
                            closestPointTest.point1, closestPointTest.point2,
                            closestPointTest.distance, black_list):

                        closestPoint = self.new_closest_pair(
                            closestPointTest.point1, closestPointTest.point2, closestPointTest.distance)

            print
            return ListClosestPoints(partialList.list, closestPoint)

        return ListClosestPoints(sortList[begin: begin+1], ClosestPoint(sortList[begin], None, math.inf))

    def compare_next_seven_points(self, index, list):
        closestPoint = ClosestPoint(None, None, math.inf)

        possibleRange = index + 8 if index + \
            8 <= len(list) else len(list)

        for indexCount in range(index + 1, possibleRange):
            distance = euclideanDistance(list[index], list[indexCount])
            if distance < closestPoint.distance:
                closestPoint.point1 = list[index]
                closestPoint.point2 = list[indexCount]
                closestPoint.distance = distance

        return closestPoint
