from itertools import cycle
from copy import deepcopy
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if not isinstance(other, Pair):
            raise TypeError("Wrong type")
        return Pair(self.x + other.x, self.y + other.y)
    
    def row_col(self):
        return self.y, self.x
    
    def __eq__(self, other):
        if not isinstance(other, Pair):
            return False
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return self.row_col().__hash__()

DIRS = {Pair(0, 1): Pair(1, 0),Pair(1, 0): Pair(0, -1),Pair(0, -1): Pair(-1, 0), Pair(-1, 0): Pair(0,1)}

def read_in_file(file_path):
    with open(file_path, "r", encoding="UTF-8") as f:
        raw_data = f.read()
    return raw_data

def load_file(input_file):
    return list((int(line.split(": ")[0]), list(map(int, line.split(": ")[1].split()))) for line in read_in_file(input_file).split("\n"))


def test_list(target, items):
    if len(items) == 1:
        return items[0] == target
        
    return test_list(target, [items[0] + items[1]] + items[2:]) or test_list(target, [items[0] * items[1]] + items[2:])

def part_1(input_file):
    data = load_file(input_file)
    # print(data)
    count = 0
    for item in data:
        if test_list(item[0], item[1]):
            count += item[0]
    return count

def test_list2(target, items):
    if len(items) == 1:
        return items[0] == target
        
    return test_list2(target, [items[0] + items[1]] + items[2:]) or test_list2(target, [items[0] * items[1]] + items[2:]) or test_list2(target, [int(str(items[0]) + str(items[1]))] + items[2:])


def part_2(input_file):
    data = load_file(input_file)
    # print(data)
    count = 0
    for item in data:
        if test_list2(item[0], item[1]):
            count += item[0]
    return count

from timeit import timeit
from time import time
if __name__ == "__main__":
    print(timeit(lambda: part_1("day-7/input/example.txt"), number = 10))
    print(part_1("day-7/input/input.txt"))
    print(part_1("day-7/input/pf-input.txt"))
    print(timeit(lambda: part_2("day-7/input/example.txt"), number = 10))
    t1 = time()
    print(part_2("day-7/input/input.txt"))
    t2 = time()
    print(f"{t2 - t1} sec")
    print(part_2("day-7/input/pf-input.txt"))
    print(f"{time() - t2} sec")