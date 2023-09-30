import re
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day20.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = read_test(
        """ p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>
            p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>"""
    )
    test_input = parse(test_input)
    test(task1(test_input), 0)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    test_input = read_test(
        """ p=<-6,0,0>, v=<3,0,0>, a=<0,0,0>
            p=<-4,0,0>, v=<2,0,0>, a=<0,0,0>
            p=<-2,0,0>, v=<1,0,0>, a=<0,0,0>
            p=<3,0,0>, v=<-1,0,0>, a=<0,0,0>"""
    )
    test_input = parse(test_input)
    test(task2(test_input), 1)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    for l in input:
        l.warp(400)
    return min(enumerate(input), key=lambda x: x[1].pos.len())[0]


def task2(input):
    for _ in range(400):
        for l in input:
            l.step()

        hashmap = {}
        for l in input:
            if hashmap.get(l.pos.hash()):
                hashmap[l.pos.hash()].append(l)
            else:
                hashmap[l.pos.hash()] = [l]
        for l in [b for b in hashmap.items() if len(b[1]) > 1]:
            for b in l[1]:
                input.remove(b)
    return len(input)


def parse(input):
    particles = []
    regex = re.compile(
        r"p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>"
    )
    for l in input:
        (px, py, pz, vx, vy, vz, ax, ay, az) = [
            int(x) for x in regex.search(l).groups()
        ]
        pos = Vec(px, py, pz)
        vel = Vec(vx, vy, vz)
        acc = Vec(ax, ay, az)
        particles.append(Particle(pos, vel, acc))
    return particles


class Particle:
    def __init__(self, pos, vel, acc) -> None:
        self.pos = pos
        self.vel = vel
        self.acc = acc

    def step(self):
        self.vel += self.acc
        self.pos += self.vel

    def warp(self, time):
        for _ in range(time):
            self.step()

    def __repr__(self) -> str:
        return f"p={self.pos}, v={self.vel}, a={self.acc}"


class Vec:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def len(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def __iadd__(self, other):
        return Vec(self.x + other.x, self.y + other.y, self.z + other.z)

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y, self.z + other.z)

    def hash(self):
        return f"({self.x}x, {self.y}y, {self.z}z)"

    def __repr__(self) -> str:
        return f"({self.x}x, {self.y}y, {self.z}z)"


if __name__ == "__main__":
    # benchmark(main)
    main()
