import re
from enum import Enum

class Dir(Enum):
    E = (0, 1)
    S = (1, 0)
    W = (0, -1)
    N = (-1, 0)

def rotate(direction: Dir):
    if not isinstance(direction, Dir):
        raise TypeError("Can only rotate a direction")
    if direction in (Dir.E, Dir.W):
        return (Dir.N, Dir.S)
    return (Dir.E, Dir.W)

def read_in_file(file_path):
    with open(file_path, "r", encoding="UTF-8") as f:
        raw_data = f.read()
    return raw_data


def load_file(input_file):
    return [list(row) for row in read_in_file(input_file).split("\n")]


def find_s_e(grid):
    s, e = None, None
    for r_ind, r in enumerate(grid):
        for c_ind, cell in enumerate(row):
            if cell == "S":
                s = (r_ind, c_ind)
            elif cell == "E":
                e = (r_ind, c_ind)
    if s is None or e is None:
        raise ValueError("no start or end position found in grid")
    return s, e

def part_1(input_file):
    grid = load_file(input_file)
    start, end = find_s_e(grid)
    rd_pos = start
    rd_dir = Dir.E


def part_2(input_file):
    return None


from timeit import timeit
def time_and_display(funct: callable, label: str = "No Label") -> None:
    res = funct()
    n = 100
    time = timeit(stmt=funct, number=n)
    print(f"{label}: Result: {res}, Time: {time*1000/n}ms")


if __name__ == "__main__":
    # Part 1
    print("Part 1")
    print(part_1("day-13/input/example.txt"))
    print(part_1("day-13/input/input.txt"))
    print(part_1("day-13/input/pf-input.txt"))
    
    # Part 2
    print("Part 2")
    print(part_2("day-13/input/example.txt"))
    print(part_2("day-13/input/input.txt"))
    print(part_2("day-13/input/pf-input.txt"))
    

    time_and_display(lambda: part_1("day-13/input/input.txt"), "part_1")

    time_and_display(lambda: part_2("day-13/input/input.txt"), "part_2")
    