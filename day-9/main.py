import re
from collections import defaultdict
from itertools import product

def read_in_file(file_path):
    with open(file_path, "r", encoding="UTF-8") as f:
        raw_data = f.read()
    return raw_data

def parse_input(data):
    files = []
    for id in range(len(data)//2):
        files.extend([id]*int(data[2*id]))
        files.extend(["."] * int(data[2*id + 1]))
    files.extend([id+1]*int(data[-1]))
    return files

def defrag(files):
    for index in range(1, len(files)):
        val = files[len(files)-index]
        if val != ".":
            try:
                replacement_index = files.index(".")
            except ValueError:
                break
            if replacement_index >= len(files) - index:
                break
            files[replacement_index] = val
            files[len(files)-index] = "."
    return files

def checksum(files):
    return sum(int(x) * y if x != "." else 0 for x, y in zip(files, range(len(files))))

def part_1(input_file):
    data = read_in_file(input_file)
    files = parse_input(data)
    files = defrag(files)
    return checksum(files)

def part_2(input_file):
    return None

import timeit

if __name__ == "__main__":
    print(part_1("day-9/input/example.txt"))
    print(part_1("day-9/input/input.txt"))
    print(part_1("day-9/input/pf-input.txt"))
    # p1 = timeit.timeit(lambda: part_1("day-9/input/input.txt"), number=1000)
    # print(f"Part 1: {p1}ms")
    # print(part_1("day-9/input/pf-input.txt"))
    # print(part_2("day-9/input/example.txt"))
    # p2 = timeit.timeit(lambda: part_2("day-9/input/input.txt"), number=1000)
    # print(f"Part 2: {p2}ms")
    # print(part_2("day-9/input/pf-input.txt"))
