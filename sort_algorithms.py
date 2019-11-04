from copy import deepcopy


class MergeSort:
    def __init__(self, list=[]):
        self.__list: list = list

    def add_elem(self, elem):
        self.__list.append(elem)

    def remove_elem(self, elem):
        self.__list.remove(elem)

    def sort_x(self) -> list:
        sortList = deepcopy(self.__list)

        return self.__merge_sort(0, len(sortList) - 1, sortList, self.__compare_x)

    def sort_y(self) -> list:
        sortList = deepcopy(self.__list)

        return self.__merge_sort(0, len(sortList) - 1, sortList, self.__compare_y)

    def __compare_x(self, point1, point2):
        if point1.x < point2.x:
            return True
        return False

    def __compare_y(self, point1, point2):
        if point1.y < point2.y:
            return True
        return False

    def __merge_sort(self, begin, end, sortList: list, compare_func) -> list:
        part1 = []
        part2 = []

        if (begin < end):
            part1 = self.__merge_sort(
                begin, int((begin + end) / 2), sortList, compare_func)
            part2 = self.__merge_sort(
                int((begin + end) / 2) + 1, end, sortList, compare_func)
            return self.__merge_list_in_x(part1, part2, compare_func)

        return sortList[begin: begin+1]

    def __merge_list_in_x(self, list1: list, list2: list, compare_func) -> list:
        count1 = 0
        count2 = 0

        resultList = []

        while(count1 < len(list1) or count2 < len(list2)):
            if count1 >= len(list1):
                resultList.extend(list2[count2:])
                break
            elif count2 >= len(list2):
                resultList.extend(list1[count1:])
                break
            elif compare_func(list2[count2], list1[count1]):
                resultList.append(list2[count2])
                if count2 < len(list2):
                    count2 += 1
            else:
                resultList.append(list1[count1])
                if count1 < len(list1):
                    count1 += 1
        return resultList
