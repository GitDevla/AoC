import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day15.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""
    test_input = read_test(test_input)
    test_input = parse(test_input)
    test(task1(test_input), 2028)
    test_input = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""
    test_input = read_test(test_input)
    test_input = parse(test_input)
    test(task1(test_input), 10092)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""
    test_input = read_test(test_input)
    test_input = parse(test_input)
    test(task2(test_input), 9021)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################

def find_player(map):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "@":
                return (x, y)

def move_box(map, boxpos,dir):
    lookahead = (boxpos[0] + dir[0], boxpos[1] + dir[1])
    if map[lookahead[1]][lookahead[0]] == "#":
        return False
    if map[lookahead[1]][lookahead[0]] in "O":
        if not move_box(map, lookahead, dir):
            return False
    map[lookahead[1]][lookahead[0]] = "O"
    map[boxpos[1]][boxpos[0]] = "."
    return True

def move_wide_box(map, boxpos,dir):
    current_box = map[boxpos[1]][boxpos[0]]
    other_box = None
    box_pos = [(boxpos[0], boxpos[1])]
    if current_box == "[":
        box_pos.append((boxpos[0]+1, boxpos[1]))
        other_box = "]"
    elif current_box == "]":
        box_pos.append((boxpos[0]-1, boxpos[1]))
        other_box = "["
    lookahead = []
    for pos in box_pos:
        lookahead.append((pos[0] + dir[0], pos[1] + dir[1]))
    for pos in lookahead:
        if map[pos[1]][pos[0]] == "#":
            return False
    
    for pos in lookahead:
        if pos in box_pos:
            continue
        if map[pos[1]][pos[0]] in "[]":
            if not move_wide_box(map, pos, dir):
                return False
    for i in range(len(box_pos)):
        map[box_pos[i][1]][box_pos[i][0]] = "."

    map[lookahead[0][1]][lookahead[0][0]] = current_box
    map[lookahead[1][1]][lookahead[1][0]] = other_box
    return True


def task1(input):
    map, moves = input
    player = find_player(map)
    map[player[1]][player[0]] = "."
    while len(moves)>0:
        move = moves.pop(0)
        lookahead = (player[0] + move[0], player[1] + move[1])
        if map[lookahead[1]][lookahead[0]] == "#":
            continue
        if map[lookahead[1]][lookahead[0]] == "O":
            if not move_box(map, lookahead, move):
                continue
        if map[lookahead[1]][lookahead[0]] in "[]":
            copymap = [x[:] for x in map]
            if not move_wide_box(map, lookahead, move):
                map = copymap
                continue
        player = lookahead

    
    sum = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] in "O[":
                sum += 100*y+x
    return sum

def widen_map(map):
    newmap = []
    for y in range(len(map)):
        newmap.append([])
        for x in range(len(map[y])):
            if map[y][x] == "#":
                newmap[-1].extend("##")
            elif map[y][x] == "O":
                newmap[-1].extend("[]")
            elif map[y][x] == "@":
                newmap[-1].extend("@.")
            else:
                newmap[-1].extend("..")
    return newmap

def task2(input):
    map, moves = input
    map = widen_map(map)
    return task1((map, moves))

def parse(input):
    joined = "\n".join(input)
    split = joined.split("\n\n")
    map = [[x for x in l] for l in split[0].split("\n")]
    moves = [convert_movement(x) for x in "".join(split[1].split("\n"))]
    return map, moves

def convert_movement(char):
    if char == "^":
        return (0, -1)
    if char == "v":
        return (0, 1)
    if char == "<":
        return (-1, 0)
    if char == ">":
        return (1, 0)


if __name__ == "__main__":
    # benchmark(main)
    main()
