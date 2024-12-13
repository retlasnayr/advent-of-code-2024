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
    cost = 0
    for machine in data:
        for a in range(100):
            for b in range(100):
                dest = (a * machine[0][0] + b * machine[1][0], a * machine[0][1] + b * machine[1][1])
                if dest == machine[2]:
                    cost += 3 * a + b
    
    return cost
    


def part_2(input_file: str) -> int:
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
    