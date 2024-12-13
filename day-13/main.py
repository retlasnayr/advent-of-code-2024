from collections import defaultdict
from functools import lru_cache
import re

def read_in_file(file_path: str) -> str:
    with open(file_path, "r", encoding="UTF-8") as f:
        raw_data = f.read()
    return raw_data

def load_file(input_file: str) -> list[int]:
    return list(map(parse_machine, list(read_in_file(input_file).split("\n\n"))))

def parse_machine(machine):
    return [tuple(int(z) for z in item) for item in re.findall(r".*: X.(\d+), Y.(\d+)", machine) ]
    


def part_1(input_file: str) -> int:
    data = load_file(input_file)
    
    return sum(linear_algebra(m) for m in data)
    


def part_2(input_file: str) -> int:
    data = load_file(input_file)
    cost = 0
    for machine in data:
        machine[2] = (machine[2][0] + 10000000000000, machine[2][1] + 10000000000000)
        cost += linear_algebra(machine)
    return cost

def linear_algebra(machine):
    det = (machine[0][0] * machine[1][1] - machine[1][0] * machine[0][1])  # = (x0 y1 - x1 y0)
    a = (machine[1][1] * machine[2][0] - machine[1][0] * machine[2][1])/det  # = (y1 x2 - x1 y2) / det
    b = (machine[0][0] * machine[2][1] - machine[0][1] * machine[2][0])/det  # = (x0 y2 - y0 x2) / det
    if a % 1 < 10**-5 and b % 1 < 10**-5:
        return int(3*a + b)
    return 0

"""
ax0 + bx1 = x2
ay0 + by1 = y2
_      _ _ _    _  _
|x0, x1| |a|  = |x2|
|y0, y1| |b|  = |y2|
-      - - -    -  -

|a|  = 1/(x0 y1 - y0 x1)  | y1  -x1| |x2|
|b|                       |-y0  x0 | |y2|

"""

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
    