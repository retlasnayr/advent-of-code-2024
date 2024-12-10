from collections import defaultdict
from functools import cmp_to_key
DIRS = [(x,y) for x in (-1, 0, 1) for y in (-1, 0, 1) if not (x == 0 and y == 0)]


def read_in_file(file_path):
    with open(file_path, "r", encoding="UTF-8") as f:
        raw_data = f.read()
    return raw_data

def load_file(input_file):
    return map(lambda x: x.split("\n"), read_in_file(input_file).split("\n\n"))


def parse_rules(rules):
    befores = defaultdict(list)
    afters = defaultdict(list)
    for rule in rules:
        before, after = rule
        befores[before].append(after)
        afters[after].append(before)
    return befores, afters

def check_update(update, befores, afters):
    for index, num in enumerate(update):
        for b in update[:index]:
            if b in befores.get(num, []):
                return False
        for a in update[index+1:]:
            if a in afters.get(num, []):
                return False
    return True
        

def part_1(input_file):
    rules, updates = load_file(input_file)
    rules = [x.split("|") for x in rules]
    updates = [x.split(",") for x in updates]
    
    befores, afters = parse_rules(rules)
    total = 0
    for update in updates:
        if check_update(update, befores, afters):
            total += int(update[(len(update) - 1) // 2])
    return total

def compare(x, y):
    if y in BEF[x]:
        return -1
    if x in BEF[y]:
        return 1
    if y in AFT[x]:
        return 1
    if x in AFT[y]:
        return -1
    return 0

def part_2(input_file):
    rules, updates = load_file(input_file)
    rules = [x.split("|") for x in rules]
    updates = [x.split(",") for x in updates]
    global BEF
    global AFT
    BEF, AFT = parse_rules(rules)
    total = 0
    for update in updates:
        sorted_update = sorted(update, key=cmp_to_key(compare))
        if update != sorted_update:
            total += int(sorted_update[(len(sorted_update) - 1) // 2])
    return total



if __name__ == "__main__":
    print(part_1("day-5/input/example.txt"))
    print(part_1("day-5/input/input.txt"))
    print(part_1("day-5/input/pf-input.txt"))
    print(part_2("day-5/input/example.txt"))
    print(part_2("day-5/input/input.txt"))
    print(part_2("day-5/input/pf-input.txt"))
