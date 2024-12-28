
from itertools import chain

def read_in_file(file_path):
    with open(file_path, "r", encoding="UTF-8") as f:
        raw_data = f.read()
    return raw_data

def load_file(input_file):
    return list(list(map(int, line)) for line in read_in_file(input_file).split("\n"))

def get_val(grid: list[list[str]], coords):
    row, col = coords
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return None
    return grid[row][col]

def adj4(x, y):
    return [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]


def find_paths(grid, cur_row, cur_col):
    cur_val = get_val(grid, (cur_row, cur_col))
    if cur_val == 9:
        return {(cur_row, cur_col)}
    return {p for f in (find_paths(grid, nbr[0], nbr[1]) for nbr in adj4(cur_row, cur_col) if get_val(grid, nbr) is not None and get_val(grid, nbr) - cur_val == 1) for p in f}
    

def part_1(input_file):
    data = load_file(input_file)
    scores = 0
    for row_num, row_data in enumerate(data):
        for col_num, col_data in enumerate(row_data):
            if col_data != 0:
                continue
            path = find_paths(data, row_num, col_num)
            # print(f"{row_num=}, {col_num=}, {len(path)=}, ends={path}")
            scores += len(path)
    return scores
    

def find_path2(grid, cur_row, cur_col):
    trail_ends = 0
    cur_val = get_val(grid, (cur_row, cur_col))
    for nbr in adj4(cur_row, cur_col):
        nbr_val = get_val(grid, nbr)
        if cur_val == 8 and nbr_val == 9:
            trail_ends += 1
        elif nbr_val is not None:
            if nbr_val - cur_val == 1:
                trail_ends += find_path2(grid, nbr[0], nbr[1])
    return trail_ends


def part_2(input_file):
    data = load_file(input_file)
    scores = 0
    for row_num, row_data in enumerate(data):
        for col_num, col_data in enumerate(row_data):
            if col_data != 0:
                continue
            path = find_path2(data, row_num, col_num)
            # print(f"{row_num=}, {col_num=}, {len(path)=}, ends={path}")
            scores += path
    return scores


if __name__ == "__main__":
    print(part_1("day-10/input/example.txt"))
    print(part_1("day-10/input/input.txt"))
    print(part_1("day-10/input/pf-input.txt"))
    print(part_2("day-10/input/example.txt"))
    print(part_2("day-10/input/input.txt"))
    print(part_2("day-10/input/pf-input.txt"))