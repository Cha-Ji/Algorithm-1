from functools import reduce


class CustomList:
    def __init__(self, elements = []) -> None:
        # 생성자에 깊은복사가 필요하다니
        self.elements = elements[:]
    
    def __add__(self, other):
        return CustomList(self.elements + (other - self).elements)

    def __sub__(self, other):
        sorted_max_list, sorted_min_list = self.__sort_self_and_other(other)

        while sorted_min_list:
            element_self = sorted_max_list.pop()
            element_other = sorted_min_list.pop()

            if element_self != element_other:
                return CustomList([element_self])

        return CustomList([sorted_max_list.pop()])
    
    def __sort_self_and_other(self, other):
        key= lambda a: len(a) 
        sorted_list = [sorted(self.elements), sorted(other.elements)]

        return max(sorted_list, key= key), min(sorted_list, key= key)
    
    def append(self, char):
        self.elements.append(char)

def solution(s):
    # sum -> TypeError: unsupported operand type(s) for +: 'int' and 'CustomList'
    return reduce(lambda acc, cur : acc + cur, parse(s)).elements

def parse(str):
    splited_list = str[2:-2].split("},{")
    customList = lambda splited: CustomList(list(map(int, splited.split(","))))

    return sorted([customList(splited) for splited in splited_list], key = lambda x: len(x.elements))