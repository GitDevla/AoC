import sys
from pathlib import Path
import itertools

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day11.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test(task1([("HM", 0), ("LM", 0), ("HG", 1), ("LG", 2)]), 11)

    ## race condition fiesta, rerun until desired value
    # Solution
    input = eval(f"{read_file(FILE)[0]}")  # cry about it
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Solution
    input = eval(f"{read_file(FILE)[0]}")
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    start = Facility(input)
    return solve(start)


def task2(input):
    input.extend(
        [
            ("8G", 0),
            ("8M", 0),
            ("9G", 0),
            ("9M", 0),
        ]
    )
    start = Facility(input)
    return solve(start)


def solve(start):
    queue = [[start, 0]]
    cache = []
    while len(queue):
        pop = max(queue, key=lambda x: x[0].happiness_index())
        queue.remove(pop)
        (curr, steps) = pop
        if curr.hash() in cache:
            continue
        if curr.is_done():
            return steps
        cache.append(curr.hash())

        pos = curr.generate_possible_realities()
        queue.extend([[x, steps + 1] for x in pos])


class Facility:
    def __init__(self, objects, elevator=0):
        self.floors = 4
        self.objects = objects  # [(what, floor)]
        self.elevator = elevator

    @staticmethod
    def copy(copy):
        return Facility([x for x in copy.objects], copy.elevator)

    def is_valid(self) -> bool:
        for f in range(self.floors):
            floor = list(filter(lambda x: x[1] == f, self.objects))
            if not Facility.is_valid_floor([x[0] for x in floor]):
                return False
        return True

    @staticmethod
    def is_valid_floor(floor):
        chips = list(filter(lambda x: x[1] == "M", floor))
        if not len(chips):  # no chips
            return True
        gens = list(filter(lambda x: x[1] == "G", floor))
        if not len(gens):
            return True  # no gens

        for c in chips:
            if not f"{c[0]}G" in gens:
                return False  # if chip with no gen
        return True

    def generate_possible_realities(self):
        curr_floor = list(filter(lambda x: x[1] == self.elevator, self.objects))
        curr_floor.append(None)
        combinations = set(itertools.combinations(curr_floor, 2))

        valid = []
        for direction in [-1, 1]:
            if self.elevator + direction < 0 or self.elevator + direction > 3:
                continue
            for elevator in combinations:
                copy = Facility.copy(self)
                copy.elevator += direction
                for package in elevator:
                    if not package:
                        continue
                    copy.objects.remove(package)
                    new = (package[0], package[1] + direction)
                    copy.objects.append(new)
                if copy.is_valid():
                    valid.append(copy)

        return valid

    def is_done(self):
        return all([x[1] == self.floors - 1 for x in self.objects])

    def hash(self):
        h = f"{self.elevator}"
        sort = sorted(self.objects)
        for i in sort:
            h += i[0] + str(i[1])
        return h

    def happiness_index(self):
        return sum([x[1] for x in self.objects])


if __name__ == "__main__":
    benchmark(main)
    # main()
