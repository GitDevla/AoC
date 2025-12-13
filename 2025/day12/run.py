import heapq
import sys
from pathlib import Path
import numpy as np
from scipy.optimize import linprog

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day12.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""
    test_input = parse(read_test(test_input))
    # test(task1(test_input), 2)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test

    test_input = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""
    test_input = parse(read_test(test_input))
    test(task2(test_input), 2)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def parse(input):
    tiles = []
    maps = []
    i = 0
    while i < len(input):
        line = input[i]
        if line.endswith(":"):
            tile = []
            i += 1
            while i < len(input) and input[i] != "":
                tile.append(input[i])
                i += 1
            tiles.append(tile)
        elif "x" in line:
            parts = line.split(":")
            size_part = parts[0].strip()
            counts_part = parts[1].strip()
            size = tuple(map(int, size_part.split("x")))
            counts = list(map(int, counts_part.split()))
            maps.append((size, counts))
            i += 1
        else:
            i += 1
    return (tiles, maps)


def is_possible_tile(tile, grid, top_left):
    tile_height = len(tile)
    tile_width = len(tile[0])
    for r in range(tile_height):
        for c in range(tile_width):
            if tile[r][c] == "#":
                grid_r = top_left[0] + r
                grid_c = top_left[1] + c
                if grid[grid_r][grid_c] == 1:
                    return False
    return True


def is_possible_placement(tiles, grid_size, tile_counts):
    grid = [[0 for _ in range(grid_size[1])] for _ in range(grid_size[0])]
    needed_space = 0
    for i in range(len(tiles)):
        tile = tiles[i]
        tile_height = len(tile)
        tile_width = len(tile[0])
        count = tile_counts[i]
        for r in range(tile_height):
            for c in range(tile_width):
                if tile[r][c] == "#":
                    needed_space += count
    total_space = grid_size[0] * grid_size[1]
    if needed_space > total_space:
        return False
    return total_space >= 9 * sum(tile_counts)

    def backtrack():
        for i in range(len(tile_counts)):
            for _ in range(tile_counts[i]):
                tile = tiles[i]
                tile_height = len(tile)
                tile_width = len(tile[0])
                for r in range(grid_size[0] - tile_height + 1):
                    for c in range(grid_size[1] - tile_width + 1):
                        if grid[r][c] == 1:
                            continue
                        if is_possible_tile(tile, grid, (r, c)):
                            for tr in range(tile_height):
                                for tc in range(tile_width):
                                    if tile[tr][tc] == "#":
                                        grid[r + tr][c + tc] = 1
                            if backtrack():
                                return True
                            for tr in range(tile_height):
                                for tc in range(tile_width):
                                    if tile[tr][tc] == "#":
                                        grid[r + tr][c + tc] = 0

    print(grid)

    return backtrack()


def task1(input):
    tiles, maps = input
    total = 0
    for grid_size, tile_counts in maps:
        if is_possible_placement(tiles, grid_size, tile_counts):
            total += 1
    return total


def task2(input):
    pass


if __name__ == "__main__":
    # benchmark(main)
    main()
