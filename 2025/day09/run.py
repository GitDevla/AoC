import heapq
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day09.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""
    test_input = parse(read_test(test_input))
    test(task1(test_input), 50)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test

    test_input = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""
    test_input = parse(read_test(test_input))
    test(task2(test_input), 24)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def parse(input):
    out = []
    for line in input:
        out.append(list(map(int, line.split(","))))
    return out


def size(x, y):
    return (abs(x[0] - y[0]) + 1) * (abs(x[1] - y[1]) + 1)


def task1(input):
    best = 0
    for a in input:
        for b in input:
            if a == b:
                continue
            best = max(best, size(a, b))
    return best


def task2(input):
    maxHeap = []
    seen = set()
    for a in input:
        for b in input:
            if a == b:
                continue
            if (tuple(a), tuple(b)) in seen or (tuple(b), tuple(a)) in seen:
                continue
            seen.add((tuple(a), tuple(b)))
            heapq.heappush(maxHeap, (-size(a, b), (a, b)))

    while maxHeap:
        area, (a, b) = heapq.heappop(maxHeap)
        area = -area
        Xmin = min(a[0], b[0])
        Xmax = max(a[0], b[0])
        Ymin = min(a[1], b[1])
        Ymax = max(a[1], b[1])
        polygon = [
            (Xmin + 0.1, Ymin + 0.1),
            (Xmax - 0.1, Ymin + 0.1),
            (Xmax - 0.1, Ymax + 0.1),
            (Xmin + 0.1, Ymax + 0.1),
        ]
        if polygon_intersect(polygon, input):
            continue

        return area
    return 0


def ccw(A, B, C):
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])


def intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


def polygon_intersect(poly1, poly2):
    n1 = len(poly1)
    n2 = len(poly2)
    for i in range(n1):
        for j in range(n2):
            if intersect(
                poly1[i],
                poly1[(i + 1) % n1],
                poly2[j],
                poly2[(j + 1) % n2],
            ):
                return True
    return False


if __name__ == "__main__":
    benchmark(main)
    # main()
