DIRS = [(x,y) for x in (-1, 0, 1) for y in (-1, 0, 1) if not (x == 0 and y == 0)]

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

def part_1(input_file):
    grid = load_file(input_file)
    count = 0
    for row_num, row_data in enumerate(grid):
        for col_num, col_data in enumerate(row_data):
            if col_data != "X":
                continue
            for dir in DIRS:
                if (
                    col_data,
                    get_val(grid, (row_num + dir[0], col_num + dir[1])),
                    get_val(grid, (row_num + 2 * dir[0], col_num + 2 * dir[1])),
                    get_val(grid, (row_num + 3 * dir[0], col_num + 3 * dir[1]))
                ) == ("X", "M", "A", "S"):
                    count += 1
    return count


def part_2(input_file):
    grid = load_file(input_file)
    count = 0
    for row_num, row_data in enumerate(grid):
        for col_num, col_data in enumerate(row_data):
            if col_data != "A":
                continue
            nbrs = [
                get_val(grid, (row_num - 1, col_num - 1)),
                get_val(grid, (row_num - 1, col_num + 1)),
                get_val(grid, (row_num + 1, col_num + 1)),
                get_val(grid, (row_num + 1, col_num - 1))
            ]
            if "S" in nbrs and "M" in nbrs and ((nbrs[0] == nbrs[1] and nbrs[2] == nbrs[3]) or (nbrs[0] == nbrs[3] and nbrs[1] == nbrs[2])) and len(set(nbrs)) == 2:
                count += 1
            # else:
            #     print(nbrs)
    return count

if __name__ == "__main__":
    print(part_1("day-4/input/example.txt"))
    print(part_1("day-4/input/input.txt"))
    print(part_1("day-4/input/pf-input.txt"))
    print(part_2("day-4/input/example.txt"))
    print(part_2("day-4/input/input.txt"))
    print(part_2("day-4/input/pf-input.txt"))
