from collections import Counter
import heapq
import re
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
    test_input = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""
    test_input = parse(read_test(test_input))
    test(task1(test_input, 10), 40)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test

    test_input = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""
    test_input = parse(read_test(test_input))
    test(task2(test_input), 25272)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def parse(input):
    out = []
    for line in input:
        out.append([list(map(int, line.split(",")))])
    return out


import math


def dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)


def task1(input, n=1000):
    input = [(a, 0) for a in input]
    no_of_circuits = 0

    dists = []
    connection_sawn = set()
    for aIdx, aJunk in enumerate(input):
        a, ac = aJunk
        for bIdx, bJunk in enumerate(input):
            b, bc = bJunk
            if a != b:
                if (aIdx, bIdx) in connection_sawn or (bIdx, aIdx) in connection_sawn:
                    continue
                connection_sawn.add((aIdx, bIdx))
                heapq.heappush(dists, (dist(a[0], b[0]), aIdx, bIdx))

    round = 0
    # for _ in range(n + 1):
    while round < (n):
        shortest_combo = heapq.heappop(dists)
        _, aIdx, bIdx = shortest_combo
        if input[aIdx][1] == input[bIdx][1] and input[aIdx][1] != 0:
            round += 1
            continue
        curcuit = max(input[aIdx][1], input[bIdx][1])
        other = min(input[aIdx][1], input[bIdx][1])
        if curcuit == 0:
            no_of_circuits += 1
            curcuit = no_of_circuits
        input[aIdx] = (input[aIdx][0], curcuit)
        input[bIdx] = (input[bIdx][0], curcuit)
        if other != 0:
            for i in range(len(input)):
                if input[i][1] == other:
                    input[i] = (input[i][0], curcuit)
        round += 1

    count = Counter()
    for _, circuit in input:
        if circuit != 0:
            count[circuit] += 1
    res = 1
    for _, v in count.most_common(3):
        res *= v
    return res


def task2(input):
    input = [(a, 0) for a in input]
    no_of_circuits = 0

    dists = []
    connection_sawn = set()
    for aIdx, aJunk in enumerate(input):
        a, ac = aJunk
        for bIdx, bJunk in enumerate(input):
            b, bc = bJunk
            if a != b:
                if (aIdx, bIdx) in connection_sawn or (bIdx, aIdx) in connection_sawn:
                    continue
                connection_sawn.add((aIdx, bIdx))
                heapq.heappush(dists, (dist(a[0], b[0]), aIdx, bIdx))

    round = 0
    res = 0
    # for _ in range(n + 1):
    while dists:
        shortest_combo = heapq.heappop(dists)
        _, aIdx, bIdx = shortest_combo
        if input[aIdx][1] == input[bIdx][1] and input[aIdx][1] != 0:
            round += 1
            continue
        res = input[aIdx][0][0][0] * input[bIdx][0][0][0]

        curcuit = max(input[aIdx][1], input[bIdx][1])
        other = min(input[aIdx][1], input[bIdx][1])
        if curcuit == 0:
            no_of_circuits += 1
            curcuit = no_of_circuits
        input[aIdx] = (input[aIdx][0], curcuit)
        input[bIdx] = (input[bIdx][0], curcuit)
        if other != 0:
            for i in range(len(input)):
                if input[i][1] == other:
                    input[i] = (input[i][0], curcuit)
        round += 1
    return res


if __name__ == "__main__":
    # benchmark(main)
    main()
