import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day08.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    input_test = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
    test_input = read_test(input_test)
    test_input = parse(test_input)
    test(task1(test_input), 14)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    input_test = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
    test_input = read_test(input_test)
    test_input = parse(test_input)
    test(task2(test_input), 34)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    nodes, width, height = input
    groupedByNodes = {}
    for node in nodes:
        groupedByNodes[node.value] = groupedByNodes.get(node.value, [])
        groupedByNodes[node.value].append(node)
    antinodes = set()
    for value in groupedByNodes.values():
        for node in value:
            for node2 in value:
                if node == node2:
                    continue
                dx, dy = node.distance(node2)
                nx = node.x + dx
                ny = node.y + dy                
                antinodes.add((nx, ny))

    antinodes = [(x, y) for x, y in antinodes if x >= 0 and x < width and y >= 0 and y < height]
    # antinodes = [(x, y) for x, y in antinodes if (x, y) not in [(n.x, n.y) for n in nodes]] amazing explonation from AoC, keep it up boys
    return len(antinodes)


def task2(input):
    nodes, width, height = input
    groupedByNodes = {}
    for node in nodes:
        groupedByNodes[node.value] = groupedByNodes.get(node.value, [])
        groupedByNodes[node.value].append(node)
    antinodes = set()
    for value in groupedByNodes.values():
        for node in value:
            for node2 in value:
                if node == node2:
                    continue
                dx, dy = node.distance(node2)
                i=0
                while True:
                    nx = node.x + dx*i
                    ny = node.y + dy*i  
                    if nx < 0 or nx >= width or ny < 0 or ny >= height:
                        break
                    i+=1           
                    antinodes.add((nx, ny))

    return len(antinodes)

def parse(input):
    nodes = []
    for i, row in enumerate(input):
        for j, cell in enumerate(row):
            if cell != ".":
                nodes.append(Node(j, i, cell))
    width = len(input[0])
    height = len(input)
    return nodes, width, height


class Node:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    def distance(self, other):
        return (self.x - other.x,self.y - other.y)

if __name__ == "__main__":
    # benchmark(main)
    main()
