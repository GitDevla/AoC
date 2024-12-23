from collections import deque
from functools import cache
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
    test(task2(["029A"]), 2379451789590)

    # Solution
    input = read_file(FILE)
    print(f"Task 2 solution: {task2(input)}")


#########################################################

def find_moves2(map,start_pos,end_pos):
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
        dirs = [(0,-1),(0,1),(-1,0),(1,0)]
        for i,(dx,dy) in enumerate(dirs):
            nx = x+dx
            ny = y+dy
            if nx < 0 or ny < 0:
                continue
            if nx >= len(map[0]) or ny >= len(map):
                continue
            if map[ny][nx] == "#":
                continue
            new_moves = moves + "^v<>"[i]
            queue.append(((nx,ny),new_moves))
    return best_moves

def generate_code_sequence(start_seqence,depth):
    return recursive_move_count("".join(start_seqence),depth+1)

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

@cache
def recursive_move_count(seq, depth):
    map = keypad
    if any([c in seq for c in "<^>v"]):
        map = robotmap
    if depth == 0:
        return len(seq)
    summa =0
    for a,b in zip("A"+seq,seq):
        start=None
        end=None
        for y in range(len(map)):
            for x in range(len(map[0])):
                if map[y][x] == a:
                    start = (x,y)
                if map[y][x] == b:
                    end = (x,y)
        ms = find_moves2(map,start,end)
        optimal = float("inf")
        for m in ms:
            v = recursive_move_count(m+"A",depth-1)
            optimal = min(optimal,v)
        summa += optimal
    return summa


def code_to_num(code):
    num = ""
    for char in code:
        if char.isdigit():
            num += char
    return int(num)

def task1(input):
    sum = 0
    for seq in input:
        sum += complexity(seq,2)
    return sum
        
def complexity(sequence,depth=2):
    n = generate_code_sequence(sequence,depth)
    c = code_to_num(sequence)
    return c * n

def task2(input):
    sum = 0
    for seq in input:
        sum += complexity(seq,25)
    return sum


if __name__ == "__main__":
    benchmark(main)
    # main()


