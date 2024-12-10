import re

def read_file(input_file):
    with open(input_file, "r", encoding="UTF-8") as f:
        raw_data = f.readlines()
    left, right = [], []
    for line in raw_data:
        pair = re.match(r"(\d+) *(\d+).*", line)
        left.append(int(pair.groups()[0]))
        right.append(int(pair.groups()[1]))
    return left, right

def part_1(input_file):
    left, right = read_file(input_file)
    left.sort()
    right.sort()
    data = zip(left, right)

    distances = [x-y if x>y else y-x for x,y in data]
    return sum(distances)

def part_2(input_file):
    left, right = read_file(input_file)
    total = 0
    for item in left:
        count = len([x for x in right if x == item])
        total += item * count
    return total


if __name__ == "__main__":
    print(part_1("day-1/input/example.txt"))
    print(part_1("day-1/input/input.txt"))
    print(part_1("day-1/input/pf-input.txt"))
    print(part_2("day-1/input/example.txt"))
    print(part_2("day-1/input/input.txt"))
    print(part_2("day-1/input/pf-input.txt"))