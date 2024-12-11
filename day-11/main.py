from collections import defaultdict
from functools import lru_cache

def read_in_file(file_path: str) -> str:
    with open(file_path, "r", encoding="UTF-8") as f:
        raw_data = f.read()
    return raw_data

def load_file(input_file: str) -> list[int]:
    return list(map(int, read_in_file(input_file).split()))
 
def blink_part_1(stones: list[int]) -> list[int]:
    new_sts = []
    for st in stones:
        if st == 0:
            new_sts.append(1)
        elif len(str(st)) % 2 == 0:
            l = len(str(st))
            new_sts.append(st // (10**(l//2)))
            new_sts.append(st % (10**(l//2)))
        else:
            new_sts.append(st*2024)
    return new_sts


def part_1(input_file: str) -> int:
    data = load_file(input_file)
    for i in range(25):
        # print(f"{i}: {' '.join(map(str,data))}")
        data = blink_part_1(data)
        
    return len(data)
    
def modify_stone(st: int) -> tuple[int]:
    if st == 0:
        return (1,)
    elif len(str(st)) % 2 == 0:
        l = len(str(st))
        return (st // (10**(l//2)), st % (10**(l//2)))
    else:
        return (st*2024,)

def blink_part_2(stones: dict[int, int]) -> dict[int, int]:
    new_stones = defaultdict(lambda: 0)
    for stone in stones:
        for res in modify_stone(stone):
            new_stones[res] += stones[stone]
    return new_stones

def part_2(input_file: str) -> int:
    data = load_file(input_file)
    stones = defaultdict(lambda: 0)
    for stone in data:
        stones[stone] += 1
    for _ in range(75):
        stones = blink_part_2(stones)
    return sum(stones.values())


def recursive_implementation(input_file: str, steps: int) -> int:
    data = load_file(input_file)
    tot = 0
    # start = time.time()
    for stone in data:
        # print(f"Stone from input: {stone}, Runtime so far: {time.time() - start} sec")
        tot += recurse_blink((stone,), steps)
    return tot

# Using this instead of functools.cache because that isn't implemented in pypy3
@lru_cache(maxsize=None)
def recurse_blink(stones: list[int], steps_to_go: int) -> int:
    if steps_to_go == 0:
        return len(stones)
    return sum(recurse_blink(modify_stone(stone), steps_to_go-1) for stone in stones)

from timeit import timeit
def time_and_display(funct: callable, label: str = "No Label") -> None:
    res = funct()
    n = 100
    time = timeit(stmt=funct, number=n)
    print(f"{label}: Result: {res}, Time: {time*1000/n}ms")

if __name__ == "__main__":
    # Part 1
    print("Part 1")
    print(part_1("day-11/input/example2.txt"))
    print(part_1("day-11/input/input.txt"))
    print(recursive_implementation("day-11/input/input.txt", 25))
    print(part_1("day-11/input/pf-input.txt"))
    
    # Part 2
    print("Part 2")
    print(part_2("day-11/input/example2.txt"))
    print(part_2("day-11/input/input.txt"))
    print(recursive_implementation("day-11/input/input.txt", 75))
    print(part_2("day-11/input/pf-input.txt"))
    

    time_and_display(lambda: part_1("day-11/input/input.txt"), "part_1")
    time_and_display(lambda: recursive_implementation("day-11/input/input.txt", 25), "part_1 recursive with caching")

    time_and_display(lambda: part_2("day-11/input/input.txt"), "part_2 dict")
    time_and_display(lambda: recursive_implementation("day-11/input/input.txt", 75), "part_2 recursive with caching")
    