import copy
import re
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day13.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = read_test(
        """ 0: 3
            1: 2
            4: 4
            6: 4"""
    )
    test_input = parse(test_input)
    test(task1(test_input), 24)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test_input = read_test(
        """ 0: 3
            1: 2
            4: 4
            6: 4"""
    )
    test_input = parse(test_input)
    test(task2(test_input), 10)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(firewall):
    packet_location = 0
    caught_in = []
    for _ in range(max(firewall.keys()) + 1):
        if not firewall.get(packet_location):
            packet_location += 1
            for layer in firewall.values():
                layer.tick()
            continue
        if firewall[packet_location].current == 0:
            caught_in.append((packet_location, firewall[packet_location]))
        for layer in firewall.values():
            layer.tick()

        packet_location += 1
    return sum([x[0] * x[1].range for x in caught_in])


def task2(input):
    """I'm Semi I stay automatic
    Money add then multiply
    I call that mathe-mat-a-matics"""
    rules = []
    for x in input.items():
        rules.append(((x[1].range - 1) * 2, x[0]))  ## (divided by, offset)
    start = 0
    while True:
        valid = check(rules, start)
        if valid:
            return start
        start += 1


def check(rules, num):
    for r in rules:
        if (num + r[1]) % r[0] == 0:
            return False
    return True


def parse(input):
    firewall = {}
    for l in input:
        (layer, range) = [int(x) for x in l.split(":")]
        firewall[layer] = Layer(range)
    return firewall


class Layer:
    def __init__(self, range) -> None:
        self.range = range
        self.current = 0
        self.going_up = True

    def tick(self, tick=1):
        for _ in range(tick):
            if self.going_up:
                self.current += 1
            else:
                self.current -= 1
            if self.current == self.range - 1 or self.current == 0:
                self.going_up = not self.going_up

    def reset(self):
        self.current = 0
        self.going_up = True

    def __repr__(self) -> str:
        return f"{self.range}/{self.current}"


if __name__ == "__main__":
    benchmark(main)
    # main()
