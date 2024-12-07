import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day06.txt"
DIRECTIONS = [(0,-1),(1,0),(0,1),(-1,0)]

def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
    test_input = parse(read_test(test_input))
    test(task1(test_input), 41)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
    test_input = parse(read_test(test_input))
    test(task2(test_input), 6)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################

def getPlayersPosition(map):
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell == "^":
                return (x, y)

def getSeenSquares(map,playersPos,playersDir):
    seenSquares = set()
    
    while True:
        nextPos = (playersPos[0]+playersDir[0],playersPos[1]+playersDir[1])
        if nextPos[0] < 0 or nextPos[1] < 0 or nextPos[0] >= len(map[0]) or nextPos[1] >= len(map):
            break

        if map[nextPos[1]][nextPos[0]]:
            playersDir = DIRECTIONS[(DIRECTIONS.index(playersDir)+1)%4]
        else:
            seenSquares.add(playersPos)
            playersPos = nextPos
    seenSquares.add(playersPos)
    return seenSquares


def task1(input):
    playersPosition = getPlayersPosition(input)
    map = convertMap(input)
    seenSquares = getSeenSquares(map,playersPosition,DIRECTIONS[0])
    return len(seenSquares)


def convertMap(map):
    return [[x == "#" for x in row] for row in map]

def isInLoop(obtuctionPositions,ySize,xSize,playersPos,playersDir):
    turningPos = set()
    while True:
        nextPos = (playersPos[0]+playersDir[0],playersPos[1]+playersDir[1])
        if nextPos[0] < 0 or nextPos[1] < 0 or nextPos[0] >= xSize or nextPos[1] >= ySize:
            return False        
        if nextPos in obtuctionPositions:
            playersDir = DIRECTIONS[(DIRECTIONS.index(playersDir)+1)%4]
            if (playersPos,playersDir) in turningPos:
                return True
            turningPos.add((playersPos,playersDir))
        else:
            playersPos = nextPos

def task2(input):
    count = 0
    playersPosition = getPlayersPosition(input)
    playersDir = DIRECTIONS[0]
    map = convertMap(input)
    possibleObstructionSpots = getSeenSquares(map,playersPosition,playersDir)

    obtuctionPositionsSet = {(x, y) for y in range(len(map)) for x in range(len(map[y])) if map[y][x]}

    for x,y in possibleObstructionSpots:
        copymap = obtuctionPositionsSet.copy()
        copymap.add((x,y))
        if isInLoop(copymap,len(map),len(map[0]),playersPosition,playersDir):
            count += 1
    return count


def parse(input):
    return [list(line.strip()) for line in input]

if __name__ == "__main__":
    benchmark(main)
    # main()
