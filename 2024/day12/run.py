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

def floodfill(input, start):
    node = input[start[0]][start[1]]
    area = set()
    circumference = 0
    queue = [start]
    while len(queue)>0:
        y,x = queue.pop(0)
        if y<0 or y>=len(input) or x<0 or x>=len(input[y]):
            circumference+=1
            continue

        if (y,x) in area:
            continue
        curr = input[y][x]

        if curr != node:
            circumference+=1
            continue
        if curr == "#":
            continue
        area.add((y,x))
        input[y][x] = "#"
        for d in DIRECTIONS:
            queue.append((y+d[0], x+d[1]))
    return area, circumference
            

def task1(input):
    all = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] != "#":
                area, circumference= floodfill(input, (y, x))
                all += len(area)*circumference

    return all

      

def count_sides(area_positions):
    min_size = (min([y for y,_ in area_positions]), min([x for _,x in area_positions]))
    size = (max([y for y,_ in area_positions])+1, max([x for _,x in area_positions])+1)
    size = (size[0]-min_size[0], size[1]-min_size[1])
    tempmap = [[False for _ in range(0,size[1])] for _ in range(0,size[0])]
    for y,x in area_positions:
        y -= min_size[0]
        x -= min_size[1]
        tempmap[y][x] = True
        
    sum = 0
    for y in range(0,size[0]+1):
        for x in range(0,size[1]+1):
            sum += numberOfEdges(tempmap, (y,x))

    return sum
            
    
def numberOfEdges(matrix, pos):
    y,x = pos
    blocks = 0
    for dy in range(-1,1):
        for dx in range(-1,1):
            ny = y+dy
            nx = x+dx
            if ny<0 or ny>=len(matrix) or nx<0 or nx>=len(matrix[ny]):
                continue
            if matrix[ny][nx]:
                blocks += 1
    if blocks ==3 or blocks == 1:
        return 1
    if blocks == 4:
        return 0

    if y-1<0 or x-1<0 or y>=len(matrix) or x>=len(matrix[y]):
        return 0
    if matrix[y][x] and matrix[y-1][x-1]:
        return 2
    if matrix[y][x-1] and matrix[y-1][x]:
        return 2
    return 0
    
    
def task2(input):
    all = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] != "#":
                area, _= floodfill(input, (y, x))
                all += len(area)*count_sides(area)

    return all

def parse(input):
    return [[x for x in row] for row in input]

if __name__ == "__main__":
    benchmark(main)
    # main()
