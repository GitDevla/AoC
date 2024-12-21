from collections import deque
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day21.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test(1, 1)
    test(complexity("029A"),68 * 29)
    test(complexity("980A"),60 * 980)
    test(complexity("179A"),68 * 179)
    test(complexity("456A"),64 * 456)
    test(complexity("379A"),64 * 379)

    # Solution
    input = read_file(FILE)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(1, 1)

    # Solution
    input = read_file(FILE)
    print(f"Task 2 solution: {task2(input)}")


#########################################################

def movement_changes(movements):
    changes = 0
    for i in range(1,len(movements)):
        if movements[i] != movements[i-1]:
            changes+=1
    return changes


def find_moves(map,start_pos,end_pos):
    robot = (start_pos,"")
    queue = deque([robot])
    best_moves = []
    while queue:
        robot = queue.popleft()
        pos,moves = robot
        x,y = pos
        if len(best_moves) > 0 and len(best_moves[0]) < len(moves):
            continue
        if pos == end_pos:
            best_moves.append(moves)
            continue
        dirs = [(0,-1),(1,0),(0,1),(-1,0)]
        for i,(dx,dy) in enumerate(dirs):
            nx = x+dx
            ny = y+dy
            if nx < 0 or ny < 0:
                continue
            if nx >= len(map[0]) or ny >= len(map):
                continue
            if map[ny][nx] == "#":
                continue
            new_moves = moves + "^>v<"[i]
            queue.append(((nx,ny),new_moves))
    sorted_moves = sorted(best_moves,key=lambda x: (-movement_changes(x)))
    return sorted_moves[-1]

def convert_dirs_to_sequence(dirs):
    sequence = []
    for i in range(4):
        for _ in range(dirs[i]):
            sequence.append("<v>^"[i])
    return sequence

def find_sequence(map,sequence):
    new_sequence = []
    start_pos = None
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "A":
                start_pos = (x,y)
    while len(sequence) > 0:
        end_char = sequence.pop(0)
        end_pos = None
        for y in range(len(map)):
            for x in range(len(map[0])):
                if map[y][x] == end_char:
                    end_pos = (x,y)
        robot = find_moves(map,start_pos,end_pos)
        start_pos = end_pos
        new_sequence += robot
        new_sequence += ["A"]
    return new_sequence

def generate_code_sequence(start_seqence):
    keypad = [
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        ["#", "0", "A"]
    ]
    robotmap = [
        ["#","^","A"],
        ["<","v",">"]
    ]
    sequence = list(start_seqence)
    sequence = find_sequence(keypad,sequence)
    for _ in range(2):
        sequence = find_sequence(robotmap,sequence)


    return "".join(sequence)

def code_to_num(code):
    num = ""
    for char in code:
        if char.isdigit():
            num += char
    return int(num)

def task1(input):
    sum = 0

    for seq in input:
        n = generate_code_sequence(seq)
        c = code_to_num(seq)
        sum += c * len(n)  
    
    return sum
        
def complexity(sequence):
    n = generate_code_sequence(sequence)
    c = code_to_num(sequence)
    return c * len(n)

def task2(input):
    pass


if __name__ == "__main__":
    # benchmark(main)
    main()


