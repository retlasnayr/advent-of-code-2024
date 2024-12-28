from collections import defaultdict
from functools import lru_cache

def read_in_file(file_path: str) -> str:
    with open(file_path, "r", encoding="UTF-8") as f:
        raw_data = f.read()
    return raw_data

def load_file(input_file: str) -> list[int]:
    return list(list(line) for line in read_in_file(input_file).split("\n"))

def adj4(x, y):
    return [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]

def get_val(grid: list[list[str]], coords):
    row, col = coords
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return None
    return grid[row][col]

class Region:
    def __init__(self, letter):
        self.letter = letter
        self.cells = set()
        self.perim = 0

    def add_cell(self, coords: tuple[int, int]):
        self.cells.add(coords)
        
def add_to_region(data, region, coords, seen):
    if coords in seen:
        return seen, region
    seen.add(coords)
    region.cells.add(coords)
    for nbr in adj4(coords[0], coords[1]):
        if get_val(data, nbr) is None:
            region.perim += 1
            continue
        if get_val(data, nbr) == region.letter:
            seen, region = add_to_region(data, region, nbr, seen)
        else:
            region.perim += 1
    return seen, region


def find_regions(data):
    regions = set()
    seen = set()
    for r_num, row in enumerate(data):
        for col_num, col in enumerate(row):
            if (r_num, col_num) not in seen:
                region = Region(col)
                seen, region = add_to_region(data, region, (r_num, col_num), seen)
                regions.add(region)
    return regions


def part_1(input_file):
    data = load_file(input_file)
    regions = find_regions(data)
    return sum(r.perim*len(r.cells) for r in regions)


def sides(region):
    # convert to lattice points by multiplying by 2 then putting edges in to connect points
    # get edge components and a path along them
    # count corners when walking along edges
    # num corners = num straight sides
    pass


def part_2(input_file):
    data = load_file(input_file)
    regions = find_regions(data)


from timeit import timeit
def time_and_display(funct: callable, label: str = "No Label") -> None:
    res = funct()
    n = 100
    time = timeit(stmt=funct, number=n)
    print(f"{label}: Result: {res}, Time: {time*1000/n}ms")

if __name__ == "__main__":
    # Part 1
    print("Part 1")
    print(part_1("day-12/input/example.txt"))
    print(part_1("day-12/input/input.txt"))
    print(part_1("day-12/input/pf-input.txt"))
    
    # Part 2
    print("Part 2")
    print(part_2("day-12/input/example.txt"))
    print(part_2("day-12/input/input.txt"))
    print(part_2("day-12/input/pf-input.txt"))
    

    time_and_display(lambda: part_1("day-12/input/input.txt"), "part_1")

    time_and_display(lambda: part_2("day-12/input/input.txt"), "part_2 dict")
    