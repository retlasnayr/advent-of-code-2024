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
    return list(list(line) for line in read_in_file(input_file).split("\n"))[::-1]

def get_val(grid: list[list[str]], coords):
    row, col = coords
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return None
    return grid[row][col]

def part_1(input_file):
    grid = load_file(input_file)
    # print(grid)
    for rnum, row in enumerate(grid):
        for cnum, col in enumerate(row):
            if col == "^":
                curr_loc = Pair(cnum, rnum)
                curr_dir = Pair(0, 1)
    visited = {curr_loc}
    while True:
        curr_loc, curr_dir = next_loc(grid, curr_loc, curr_dir)
        if curr_loc is None:
            break
        visited.add(curr_loc)
    return len(visited)

def next_loc(grid, curr_loc: Pair, curr_dir: Pair, extra_obs = None):
    loc_to_try = curr_loc + curr_dir
    new_val = get_val(grid, loc_to_try.row_col())
    if new_val == "#" or loc_to_try == extra_obs:
        return curr_loc, DIRS[curr_dir]
    if new_val is None:
        return None, curr_dir
    return loc_to_try, curr_dir

# def jump_to_next_obs(obstacles, curr_loc, curr_dir):
#     if curr_dir.x == 0:



def part_2(input_file):
    grid = load_file(input_file)
    dims = Pair(len(grid[0]), len(grid))
    obstacles = set()
    for rnum, row in enumerate(grid):
        for cnum, col in enumerate(row):
            if col == "^":
                start_loc = Pair(cnum, rnum)
                start_dir = Pair(0, 1)
            if col == "#":
                obstacles.add(Pair(cnum, rnum))
    # Run Part 1
    curr_loc, curr_dir = start_loc, start_dir
    visited = {curr_loc}
    while True:
        curr_loc, curr_dir = next_loc(grid, curr_loc, curr_dir)
        if curr_loc is None:
            break
        visited.add(curr_loc)
    
    cycles = 0
    for location in visited:
        route = {(start_loc, start_dir)}
        curr_loc, curr_dir = start_loc, start_dir
        while True:
            curr_loc, curr_dir = next_loc(grid, curr_loc, curr_dir, location)
            if curr_loc is None:
                break
            if (curr_loc, curr_dir) in route:
                cycles += 1
                break
            route.add((curr_loc, curr_dir))
    return cycles


from timeit import timeit
from time import time
if __name__ == "__main__":
    print(timeit(lambda: part_1("day-6/input/example.txt"), number = 10))
    print(part_1("day-6/input/input.txt"))
    print(part_1("day-6/input/pf-input.txt"))
    print(timeit(lambda: part_2("day-6/input/example.txt"), number = 10))
    t1 = time()
    print(part_2("day-6/input/input.txt"))
    t2 = time()
    print(f"{t2 - t1} sec")
    print(part_2("day-6/input/pf-input.txt"))
    print(f"{time() - t2} sec")