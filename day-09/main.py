import re
import copy
from collections import defaultdict
from itertools import product

def read_in_file(file_path):
    with open(file_path, "r", encoding="UTF-8") as f:
        raw_data = f.read()
    return raw_data

def parse_input(data):
    files = []
    for id in range(len(data)//2):
        files.extend([id]*int(data[2*id]))
        files.extend(["."] * int(data[2*id + 1]))
    files.extend([id+1]*int(data[-1]))
    return files

def defrag(files):
    for index in range(1, len(files)):
        val = files[len(files)-index]
        if val != ".":
            try:
                replacement_index = files.index(".")
            except ValueError:
                break
            if replacement_index >= len(files) - index:
                break
            files[replacement_index] = val
            files[len(files)-index] = "."
    return files

def checksum(files):
    return sum(int(x) * y if x != "." else 0 for x, y in zip(files, range(len(files))))

def part_1(input_file):
    data = read_in_file(input_file)
    files = parse_input(data)
    files = defrag(files)
    return checksum(files)

class File:
    def __init__(self, start_index, len, id=None, blank=False):
        self.start = start_index
        self.end = start_index + int(len)
        self.length = self.end - self.start
        self.id = int(id) if id is not None else None
        self.blank_space = blank
    
    def checksum(self):
        return sum(self.id * (self.start + x) for x in range(self.length))
    
    def move(self, new_start):
        self.start = new_start
        self.end = new_start + self.length
        return self
    
    def shrink(self, new_start):
        self.start = new_start
        self.length = self.end - new_start
        return self
    

def parse_input2(data):
    files = []
    spaces = []
    nxt = 0
    for id in range(len(data)//2):
        files.append(File(nxt, data[2*id], id))
        nxt += int(data[2*id])
        spaces.append(File(nxt, data[2*id+1], None, True))
        nxt += int(data[2*id+1])
    files.append(File(nxt, data[2*id+2], id+1))
    return {x.id: x for x in files}, {x.start: x for x in spaces}

def output(files: list, spaces: dict):
    res = []
    files = list(ordered_files(files))
    while len(files) > 0 or len(spaces) > 0:
        space_keys = sorted(list(spaces.keys()))
        if (len(space_keys) == 0) or (len(files) > 0 and files[0].start < spaces[space_keys[0]].start):
            res.extend([str(files[0].id)]*files[0].length)
            files.pop(0)
        else:
            res.extend(["."]*spaces[space_keys[0]].length)
            spaces.pop(space_keys[0])
    return "".join(res)+"\n"+"".join(str(x)[-1] for x in range(len(res)))


def ordered_files(files):
    return sorted(files.values(), key=lambda x: x.start)

def part_2(input_file):
    data = read_in_file(input_file)
    files, spaces = parse_input2(data)
    file_ids = sorted(files.keys(), reverse=True)
    for file in file_ids:
        # print(output(copy.copy(files), copy.copy(spaces)))
        for idx in sorted(spaces.keys()):
            if spaces[idx].length >= files[file].length and spaces[idx].start < files[file].start:
                spaces[files[file].start] = File(files[file].start, files[file].length, None, True)
                files[file] = files[file].move(idx)
                spaces[idx].shrink(idx + files[file].length)
                spaces[idx + files[file].length] = spaces.pop(idx)
                break
    ans = 0
    for file in ordered_files(files):
        ans += file.checksum()
    return ans

if __name__ == "__main__":
    print(part_1("day-9/input/example.txt"))
    print(part_1("day-9/input/input.txt"))
    print(part_1("day-9/input/pf-input.txt"))
    print(part_2("day-9/input/example.txt"))
    print(part_2("day-9/input/input.txt"))
    print(part_2("day-9/input/pf-input.txt"))