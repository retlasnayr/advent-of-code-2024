import re

def read_in_file(file_path):
    with open(file_path, "r", encoding="UTF-8") as f:
        raw_data = f.read()
    return raw_data

def load_file(input_file):
    return read_in_file(input_file)

def part_1(input_file):
    return sum(int(match[1]) * int(match[2]) for match in re.findall(r"(mul\((\d+),(\d+)\))", load_file(input_file)))

def part_2(input_file):
    data = load_file(input_file)
    commands = re.findall(r"(mul\((\d+),(\d+)\))|(don't\(\))|(do\(\))", data)
    enable = True
    total = 0
    for com in commands:
        if com[4] == "do()":
            enable = True
        elif com[3] == "don't()":
            enable = False
        else:
            if enable:
                total += int(com[1]) * int(com[2])
    return total

if __name__ == "__main__":
    print(part_1("day-3/input/example.txt"))
    print(part_1("day-3/input/input.txt"))
    print(part_1("day-3/input/pf-input.txt"))
    print(part_2("day-3/input/example2.txt"))
    print(part_2("day-3/input/input.txt"))
    print(part_2("day-3/input/pf-input.txt"))
