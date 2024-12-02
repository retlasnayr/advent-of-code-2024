def load_file(input_file):
    with open(input_file, "r", encoding="UTF-8") as f:
        raw_data = f.read().split("\n")
    data = [[int(y) for y in x.split()] for x in raw_data]
    return data

def check_list_safety(line):
    safe = True
    incr = line[0] < line[1]
    for index in range(1, len(line)):
        if incr:
            safe = safe and line[index-1] < line[index] and 1 <= line[index] - line[index-1] <= 3
        else: 
            safe = safe and line[index-1] > line[index] and 1 <= line[index-1] - line[index] <= 3
    # print(safe, line)
    return safe


def part_1(input_file):
    data = load_file(input_file)
    count = 0
    for line in data:
        if check_list_safety(line):
            count += 1
    return count

def part_2(input_file):
    return None

if __name__ == "__main__":
    print(part_1("day-2/input/example.txt"))
    print(part_1("day-2/input/input.txt"))
    print(part_1("day-2/input/pf-input.txt"))
    print(part_2("day-2/input/example.txt"))
    print(part_2("day-2/input/input.txt"))
    print(part_2("day-2/input/pf-input.txt"))
