from functools import cache
import itertools
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day23.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""
    test_input = parse(read_test(test_input))
    test(task1(test_input), 7)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""
    test_input = parse(read_test(test_input))
    test(task2(test_input), "co,de,ka,ta")

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################

def find_set_of_three(nodes):
    interconnected = set()
    for node in nodes:
        for a in nodes[node]:
            for b in nodes[a]:
                if b in nodes[node]:
                    interconnected.add(tuple(sorted([node, a, b])))

    return interconnected

def any_starts_with(nodes, letter):
    for node in nodes:
        if node.startswith(letter):
            return True
    return False

def task1(input):
    nodes = input
    interconnected = find_set_of_three(nodes)
    starts_with_t = list(filter(lambda x: any_starts_with(x, "t"), interconnected))
    
    return len(starts_with_t)


def find_connected_nodes(nodes, curr, req=[], sets=None):
    if sets is None:
        sets = set()
    key = tuple(sorted(req))
    if key in sets:
        return sets
    sets.add(key)
    for node in nodes[curr]:
        if node in req:
            continue
        if not all([node in nodes[x] for x in req]):
            continue
        copy = req.copy()
        copy.append(node)
        find_connected_nodes(nodes, node, copy, sets)
    return sets

def task2(input):
    found = set()
    for x in input:
        found = found.union(find_connected_nodes(input, x, [x]))
    found = sorted(list(found),key=len)
    return ",".join(found[-1])


def parse(input):
    nodes = {}
    for line in input:
        left, right = line.split("-")
        if left not in nodes:
            nodes[left] = []
        nodes[left].append(right)
        if right not in nodes:
            nodes[right] = []
        nodes[right].append(left)
    return nodes



if __name__ == "__main__":
    # benchmark(main)
    main()
