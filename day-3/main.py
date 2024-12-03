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
    data = load_file(input_file)
    sum = 0
    mult_val = 0
    enable = True
    while True:
        if enable:
            sum += mult_val
        en, mv, data = get_next_instruction(data)
        if en is not None:
            enable = en
            mult_val = 0
        elif mv is not None:
            mult_val = mv
        else:
            break
    return sum


def get_next_instruction(string):
    enable = re.search(r"do\(\)", string)
    disable = re.search(r"don't\(\)", string)
    mult = re.search(r"mul\((\d+),(\d+)\)", string)
    options = [enable, disable, mult]
    if all(x is None for x in options):
        return None, None, None
    next = min(options, key=lambda x: x.start() if x is not None else 10**10)
    if next == enable:
        return True, None, string[next.end():]
    if next == disable:
        return False, None, string[next.end():]
    if next == mult:
        return None, int(mult.group(1)) * int(mult.group(2)), string[next.end():]

if __name__ == "__main__":
    print(part_1("day-3/input/example.txt"))
    print(part_1("day-3/input/input.txt"))
    print(part_1("day-3/input/pf-input.txt"))
    print(part_2("day-3/input/example2.txt"))
    print(part_2("day-3/input/input.txt"))
    print(part_2("day-3/input/pf-input.txt"))
