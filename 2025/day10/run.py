import sys
from pathlib import Path
import numpy as np
from scipy.optimize import linprog

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day10.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""
    test_input = parse(read_test(test_input))
    test(task1(test_input), 7)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test

    test_input = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""
    test_input = parse(read_test(test_input))
    test(task2(test_input), 33)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def parse(input):
    out = []
    for line in input:
        asd = line.split(" ")
        raw_lights = asd[0]
        lights = []
        for i in range(1, len(raw_lights) - 1):
            if raw_lights[i] == "#":
                lights.append(True)
            else:
                lights.append(False)
        raw_wiring = asd[1:-1]
        wiring = []
        for w in raw_wiring:
            w = w.strip("()").split(",")
            w = list(map(int, w))
            wiring.append(w)
        raw_joltage = asd[-1]
        joltage = []
        for j in raw_joltage.strip("{}").split(","):
            joltage.append(int(j))
        out.append((lights, wiring, joltage))
    return out


def solve_machine(x):
    curr, target, wiring = x
    start = (curr, 0)
    queue = [start]
    visited = set()
    while queue:
        state, steps = queue.pop(0)
        state_tuple = tuple(state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        if state == target:
            return steps
        for i in range(len(wiring)):
            new_state = state[:]
            for j in wiring[i]:
                new_state[j] = not new_state[j]
            queue.append((new_state, steps + 1))
    return -1


def solve_machine2(x):
    curr, target, wiring = x
    c = np.ones(len(wiring))
    A_eq = np.zeros((len(curr), len(wiring)))
    b_eq = np.array(target) - np.array(curr)
    for j in range(len(wiring)):
        for i in wiring[j]:
            A_eq[i][j] = 1
    res = linprog(
        c,
        A_eq=A_eq,
        b_eq=b_eq,
        bounds=(0, None),
        method="highs",
        integrality=np.ones(len(wiring)),
    )
    if res.success:
        return int(sum(res.x))
    return -1


def task1(input):
    input = [(([False] * len(lights), lights, wiring)) for (lights, wiring, _) in input]
    res = 0
    for i in input:
        res += solve_machine(i)
    return res


def task2(input):
    input = [(([0] * len(joltage), joltage, wiring)) for (_, wiring, joltage) in input]
    res = 0
    for i in input:
        res += solve_machine2(i)
    return res


if __name__ == "__main__":
    # benchmark(main)
    main()
