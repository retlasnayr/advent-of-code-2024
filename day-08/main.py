DIRS = [(x,y) for x in (-1, 0, 1) for y in (-1, 0, 1) if not (x == 0 and y == 0)]
from collections import defaultdict
from itertools import product

def read_in_file(file_path):
    with open(file_path, "r", encoding="UTF-8") as f:
        raw_data = f.read()
    return raw_data

def load_file(input_file):
    return list(list(line) for line in read_in_file(input_file).split("\n"))

def get_val(grid: list[list[str]], coords):
    row, col = coords
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return None
    return grid[row][col]

def get_antennae(grid):
    antennae = defaultdict(list)
    for r_num, row in enumerate(grid):
        for c_num, col in enumerate(row):
            if col != ".":
                antennae[col].append((r_num, c_num))
    return antennae


def find_antinodes(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    a1 = (p1[0]+dx, p1[1]+dy)
    a2 = (p2[0]-dx, p2[1]-dy)
    return a1, a2

def part_1(input_file):
    grid = load_file(input_file)
    height = len(grid)
    width = len(grid[0])
    antennae = get_antennae(grid)
    locs = set()
    for label, ants in antennae.items():
        pairs = product(ants, repeat=2)
        for n1, n2 in pairs:
            if n1 == n2:
                continue
            a1, a2 = find_antinodes(n1, n2)
            if get_val(grid, a1) is not None:
                locs.add(a1)
            if get_val(grid, a2) is not None:
                locs.add(a2)
    return len(locs)

def find_antinodes2(p1, p2, h, w):
    ans = set()
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    for i in range(max(h, w)):
        ans.add((p1[0]+i*dx, p1[1]+i*dy))
        ans.add((p2[0]-i*dx, p2[1]-i*dy))
    return ans

def part_2(input_file):
    grid = load_file(input_file)
    height = len(grid)
    width = len(grid[0])
    antennae = get_antennae(grid)
    locs = set()
    for label, ants in antennae.items():
        pairs = product(ants, repeat=2)
        for n1, n2 in pairs:
            if n1 == n2:
                continue
            ans = find_antinodes2(n1, n2, height, width)
            locs.update({x for x in ans if get_val(grid, x) is not None})
    return len(locs)

import timeit

if __name__ == "__main__":
    print(part_1("day-8/input/example.txt"))
    p1 = timeit.timeit(lambda: part_1("day-8/input/input.txt"), number=1000)
    print(f"Part 1: {p1}ms")
    print(part_1("day-8/input/pf-input.txt"))
    print(part_2("day-8/input/example.txt"))
    p2 = timeit.timeit(lambda: part_2("day-8/input/input.txt"), number=1000)
    print(f"Part 2: {p2}ms")
    print(part_2("day-8/input/pf-input.txt"))
