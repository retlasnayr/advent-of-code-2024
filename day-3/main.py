import re

def read_in_file(file_path):
    with open(file_path, "r", encoding="UTF-8") as f:
        raw_data = f.read()
    return raw_data

def load_file(input_file):
    return read_in_file(input_file)

def part_1(input_file):
    data = load_file(input_file)
    sum = 0
    mult_val = 0
    while mult_val is not None:
        sum += mult_val
        mult_val, data = get_first_mul(data)
    return sum

def get_first_mul(string):
    match = re.search(r"mul\((\d+),(\d+)\)", string)
    if match is not None:
        return int(match.group(1)) * int(match.group(2)), string[match.end():]
    return None, string

def part_2(input_file):
    return None


if __name__ == "__main__":
    print(part_1("day-3/input/example.txt"))
    print(part_1("day-3/input/input.txt"))
    print(part_1("day-3/input/pf-input.txt"))
    print(part_2("day-3/input/example.txt"))
    print(part_2("day-3/input/input.txt"))
    print(part_2("day-3/input/pf-input.txt"))
