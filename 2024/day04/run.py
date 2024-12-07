import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day04.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
    test_input = parse(read_test(test_input))
    test(task1(test_input), 18)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
    test_input = parse(read_test(test_input))
    test(task2(test_input), 9)

    # Solution
    input = read_file(FILE)
    print(f"Task 2 solution: {task2(input)}")


#########################################################

def searchWordInDirection(map,word,currentPos,direction):
    x,y = currentPos
    dx,dy = direction
    length = len(word)-1
    if y+length*dy < 0 or y+length*dy >= len(map) or x+length*dx < 0 or x+length*dx >= len(map[0]):
            return False
    for i in range(1,len(word)):
        if map[y+i*dy][x+i*dx] != word[i]:
            return False
    return True

def task1(input):
    sum = 0;
    word = "XMAS"
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] != "X":
                continue
            for dx in range(-1,2):
                for dy in range(-1,2):
                    if dx == 0 and dy == 0:
                        continue
                    if searchWordInDirection(input,word,(x,y),(dx,dy)):
                        sum += 1
    return sum

def rotateMatrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0])-1,-1,-1)]


def isX_MAS(matrix,cx,cy):
    if cy - 1 < 0 or cy + 1 >= len(matrix) or cx - 1 < 0 or cx + 1 >= len(matrix[0]):
        return False

    submatrixAround = [row[cx-1:cx+2] for row in matrix[cy-1:cy+2]]

    for _ in range(3):
        if submatrixAround[0][0]=='M' and submatrixAround[0][2] == "M":
            break
        submatrixAround = rotateMatrix(submatrixAround)

    diognalOne = "".join([submatrixAround[0][0],submatrixAround[1][1],submatrixAround[2][2]])
    diognalTwo = "".join([submatrixAround[0][2],submatrixAround[1][1],submatrixAround[2][0]])

    return diognalOne == "MAS" and diognalTwo == "MAS"

def task2(input):
    sum = 0;
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] != "A":
                continue
            if isX_MAS(input,x,y):
                sum += 1
    return sum

def parse(input):
    return [list(line) for line in input]

if __name__ == "__main__":
    benchmark(main)
    # main()
