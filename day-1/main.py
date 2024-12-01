import re

def main(input_file):
    with open(input_file, "r", encoding="UTF-8") as f:
        raw_data = f.readlines()
    left, right = [], []
    for line in raw_data:
        pair = re.match(r"(\d+) *(\d+).*", line)
        left.append(int(pair.groups()[0]))
        right.append(int(pair.groups()[1]))
    # print(left)
    # print(right)
    left.sort()
    right.sort()
    data = zip(left, right)

    distances = [x-y if x>y else y-x for x,y in data]
    return sum(distances)


if __name__ == "__main__":
    print(main("day-1/input/example.txt"))
    print(main("day-1/input/input.txt"))