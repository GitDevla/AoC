import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day16.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""
    test_input = parse(read_test(test_input))
    test(task1(test_input), 7036)
    test_input = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""
    test_input = parse(read_test(test_input))
    test(task1(test_input), 11048)
    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""
    test_input = parse(read_test(test_input))
    test(task2(test_input), 45)
    test_input = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""
    test_input = parse(read_test(test_input))
    test(task2(test_input), 64)

    # # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################

def findPlayer(map):
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell == "S":
                return (x, y)
            
def findEnd(map):
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell == "E":
                return (x, y)

from queue import PriorityQueue
def findPath(map, playerPos, end):
    DIRS = [(0,1),(0,-1),(1,0),(-1,0)]
    player = (0,playerPos,(1,0))
    queue = PriorityQueue()
    queue.put(player)
    seen = {}
    while not queue.empty():
        score,pos,dir = queue.get()
        if (pos,dir) in seen.keys():
            if seen[pos,dir] <= score:
                continue
        seen[pos,dir] = score
        if pos == end:
            return score
        lookahead = (pos[0]+dir[0],pos[1]+dir[1])
        if map[lookahead[1]][lookahead[0]] != "#":
            queue.put((score+1,lookahead,dir))
        for d in DIRS:
            if [x*-1 for x in d] == list(dir):
                continue
            if d == dir:
                continue
            queue.put((score+1000,pos,d))
    return -1


def task1(input):
    player = findPlayer(input)
    end = findEnd(input)
    return findPath(input,player,end)

import math
from collections import defaultdict
def findPathSquares(map, playerPos, end):
    player = (0,playerPos,(1,0),(None,None,None,None))
    queue = PriorityQueue()
    backtrack = defaultdict(set)
    queue.put(player)
    seen = {}
    limit = math.inf
    while not queue.empty():
        score,pos,dir,prev = queue.get()
        if score > limit:
            continue
        px,py,pdx,pdy = prev
        if seen.get((pos,dir),math.inf) < score: continue
        if seen.get((pos,dir),score) != score:
            backtrack[pos,dir].clear()
        seen[pos,dir] = score

        backtrack[pos,dir].add(((px,py),(pdx,pdy)))

        if pos == end:
            limit = score
            continue
        lookahead = (pos[0]+dir[0],pos[1]+dir[1])
        if map[lookahead[1]][lookahead[0]] != "#":
            queue.put((score+1,lookahead,dir,(pos[0],pos[1],dir[0],dir[1])))
        turnDir = (dir[1],dir[0])
        oppositeDir = (turnDir[0]*-1,turnDir[1]*-1)
        for d in [turnDir,oppositeDir]:
            if seen.get((pos,d),math.inf) < score+1000: continue
            queue.put((score+1000,pos,d,(pos[0],pos[1],dir[0],dir[1])))

    curr = set()
    for d in [(1,0),(0,1),(-1,0),(0,-1)]:
        curr.add(((end[0],end[1]),(d[0],d[1])))
    visited_squares = set()
    while len(curr)>0:
        new_curr = set()
        for p,d in curr:
            if p[0] is None:
                continue
            if not (p,d) in backtrack: continue
            new_curr.update(backtrack.get((p,d)))
            visited_squares.add(p)
        curr = new_curr

    return len(visited_squares)

def task2(input):
    player = findPlayer(input)
    end = findEnd(input)
    return findPathSquares(input,player,end)

def parse(input):
    return [[x for x in line]for line in input]

if __name__ == "__main__":
    benchmark(main)
    # main()
