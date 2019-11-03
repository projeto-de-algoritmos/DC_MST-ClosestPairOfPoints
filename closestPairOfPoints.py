import math
from copy import deepcopy


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
        self.sortedListX = list

    def search(self):
        sortedList = deepcopy(self.sortedListX)

        result = self.__merge_in_x(0, len(sortedList) - 1, sortedList)
        return result.closestPoints

    def __print_blacklist(self, black_list):
        print("black_list")

        print("[ ", end="")
        for pair in black_list:
            print("( ", end="")
            print("{", pair.point1.x, ", ", pair.point1.y, "}", end="")
            print("{", pair.point2.x, ", ", pair.point2.y, "}", end="")
            print(" ), ", end="")
        print(" ]")

    def generate_minimum_tree(self):
        sortedList = deepcopy(self.sortedListX)

        tree = []

        for index in range(len(sortedList) - 1):
            result = self.__merge_in_x(
                0, len(sortedList) - 1, sortedList, tree)
            tree.append(result.closestPoints)

        return tree

    def __off_black_list(self, point1, point2, black_list=[]):

        for pair in black_list:
            if (point1.x == pair.point1.x and point1.y == pair.point1.y and
                    point2.x == pair.point2.x and point2.y == pair.point2.y):
                return False

        return True

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
                    if self.__off_black_list(list1[count1], list2[count2], black_list):
                        closestPoint.point1 = list1[count1]
                        closestPoint.point2 = list2[count2]
                        closestPoint.distance = distance

                if count2 < len(list2):
                    count2 += 1
            else:
                resultList.list.append(list1[count1])

                distance = euclideanDistance(list1[count1], list2[count2])
                if distance < closestPoint.distance:
                    if self.__off_black_list(list1[count1], list2[count2], black_list):
                        closestPoint.point1 = list1[count1]
                        closestPoint.point2 = list2[count2]
                        closestPoint.distance = distance

                if count1 < len(list1):
                    count1 += 1

        return resultList

    def __merge_in_x(self, begin, end, sortList: list, black_list=[]) -> ListClosestPoints:
        part1 = []
        part2 = []
        partialList = []

        closestPoint = ClosestPoint(None, None, math.inf)

        if (begin < end):
            part1 = self.__merge_in_x(
                begin, int((begin + end) / 2), sortList)
            part2 = self.__merge_in_x(
                int((begin + end) / 2) + 1, end, sortList)
            partialList = self.__merge_list_in_y(part1, part2, black_list)

            testList = partialList.list
            closestPoint = partialList.closestPoints

            for indexPoint in range(len(testList)):
                closestPointTest = self.compare_next_seven_points(
                    indexPoint, testList)

                if closestPointTest.distance < closestPoint.distance:
                    if self.__off_black_list(closestPointTest.point1, closestPointTest.point2, black_list):
                        closestPoint = closestPointTest

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
