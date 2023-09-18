import re
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day07.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Testt
    test_input = read_test(
        """ pbga (66)
            xhth (57)
            ebii (61)
            havc (66)
            ktlj (57)
            fwft (72) -> ktlj, cntj, xhth
            qoyq (66)
            padx (45) -> pbga, havc, qoyq
            tknk (41) -> ugml, padx, fwft
            jptl (61)
            ugml (68) -> gyxo, ebii, jptl
            gyxo (61)
            cntj (57)"""
    )
    test_input = parse(test_input)
    test(task1(test_input), "tknk")

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Testt
    test_input = read_test(
        """ pbga (66)
            xhth (57)
            ebii (61)
            havc (66)
            ktlj (57)
            fwft (72) -> ktlj, cntj, xhth
            qoyq (66)
            padx (45) -> pbga, havc, qoyq
            tknk (41) -> ugml, padx, fwft
            jptl (61)
            ugml (68) -> gyxo, ebii, jptl
            gyxo (61)
            cntj (57)"""
    )
    test_input = parse(test_input)
    test(task2(test_input), 60)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def parse(input):
    nodes = []
    regex = re.compile(r"(\w+) \((\d+)\)(?: -> )*(.*)")
    for l in input:
        f = regex.search(l)
        (name, weight, next_neighb) = f.groups()
        new_node = Node(name, weight)
        if next_neighb != "":
            new_node.next = next_neighb.split(", ")
        nodes.append(new_node)
    for n in nodes:
        new_next = []
        for asd in n.next:
            new_next.append(next(x for x in nodes if x.name == asd))
        n.next = new_next
    return nodes


def task1(input):
    return max(input, key=lambda x: x.true_weight()).name


def task2(input):
    bottom = max(input, key=lambda x: x.true_weight())
    desired_weight = 0
    while True:
        weights = [x.true_weight() for x in bottom.next]
        dic = {}
        for w in weights:
            if dic.get(w):
                dic[w] += 1
            else:
                dic[w] = 1
        if len(dic) == 1:
            return desired_weight - bottom.true_weight() + bottom.weight
        odd_one_out = min(dic.items(), key=lambda x: x[1])
        desired_weight = max(dic.items(), key=lambda x: x[1])[0]

        odd_one_out = next(x for x in bottom.next if x.true_weight() == odd_one_out[0])
        bottom = odd_one_out


class Node:
    def __init__(self, name, weight) -> None:
        self.name = name
        self.weight = int(weight)
        self.next = []

    def __repr__(self) -> str:
        return f"{self.name} ({self.weight}) -> {self.next}"

    def true_weight(self):
        sum = self.weight
        for x in self.next:
            sum += x.true_weight()
        return sum


if __name__ == "__main__":
    benchmark(main)
    # main()
