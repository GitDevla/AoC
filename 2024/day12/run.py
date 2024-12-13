import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day12.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = """AAAA
BBCD
BBCC
EEEC"""
    test_input = parse(read_test(test_input))
    test(task1(test_input), 140)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""
    test_input = parse(read_test(test_input))
    test(task2(test_input), 236)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def count_steps(input, start):
    node = input[start[0]][start[1]]
    area = []
    circumference = []
    queue = [start]
    seen = set()
    while len(queue)>0:
        y,x = queue.pop(0)
        if y<0 or y>=len(input) or x<0 or x>=len(input[y]):
            circumference.append((y,x))
            continue

        if (y,x) in seen:
            continue
        curr = input[y][x]

        if curr != node:
            circumference.append((y,x))
            continue
        if curr == "#":
            continue
        area.append((y,x))
        input[y][x] = "#"
        seen.add((y,x))
        for d in DIRECTIONS:
            queue.append((y+d[0], x+d[1]))
    return node, area, circumference
            

def task1(input):
    all = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] != "#":
                node, area, circumference= count_steps(input, (y, x))
                all += len(area)*len(circumference)

    return all

      

def count_sides(area_positions,size):
    tempmap = [[0 for _ in range(0,size[1])] for _ in range(0,size[0])]
    for y,x in area_positions:
        tempmap[y][x] = 1
    
    threwsholded_matrix = [[0 for _ in range(0,size[1]+1)] for _ in range(0,size[0]+1)]
    for y in range(0,size[0]+1):
        for x in range(0,size[1]+1):
            threwsholded_matrix[y][x] = numberOfEdges(tempmap, (y,x))

    sum = 0
    for y in range(0,len(threwsholded_matrix)):
        for x in range(0,len(threwsholded_matrix[y])):
            sum += threwsholded_matrix[y][x]
    return sum
            
    
def numberOfEdges(matrix, pos):
    y,x = pos
    edges = 0
    for dy in range(-1,1):
        for dx in range(-1,1):
            ny = y+dy
            nx = x+dx
            if ny<0 or ny>=len(matrix) or nx<0 or nx>=len(matrix[ny]):
                continue
            if matrix[ny][nx] == 1:
                edges += 1
    if edges ==3 or edges == 1:
        return 1
    if edges == 4:
        return 0

    if y-1<0 or x-1<0 or y>=len(matrix) or x>=len(matrix[y]):
        return 0
    if matrix[y][x] == 1 and matrix[y-1][x-1] ==1:
        return 2
    if matrix[y][x-1] == 1 and matrix[y-1][x] ==1:
        return 2
    return 0
    
    
def task2(input):
    all = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] != "#":
                node, area, circumference= count_steps(input, (y, x))
                all += len(area)*count_sides(area,(len(input), len(input[0])))

    return all

def parse(input):
    return [[x for x in row] for row in input]

if __name__ == "__main__":
    # benchmark(main)
    main()
