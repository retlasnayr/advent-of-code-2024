def read_in_file(file_path):
    with open(file_path, "r", encoding="UTF-8") as f:
        raw_data = f.read().split("\n")
    return raw_data

def load_file(input_file):
    return [[int(y) for y in x.split()] for x in read_in_file(input_file)]

def check_list_safety(line):
    incr = line[0] < line[1]
    return all(line[index-incr] < line[index+incr-1] and 1 <= line[index+incr-1] - line[index-incr] <= 3 for index in range(1, len(line)))

def part_1(input_file):
    return sum(check_list_safety(line) for line in load_file(input_file))

def problem_dampener(line):
    return any(check_list_safety(line[:index] + line[index+1:]) for index in range(len(line)))

def part_2(input_file):
    return sum(problem_dampener(line) for line in load_file(input_file))


if __name__ == "__main__":
    print(part_1("day-2/input/example.txt"))
    print(part_1("day-2/input/input.txt"))
    print(part_1("day-2/input/pf-input.txt"))
    print(part_2("day-2/input/example.txt"))
    print(part_2("day-2/input/input.txt"))
    print(part_2("day-2/input/pf-input.txt"))
