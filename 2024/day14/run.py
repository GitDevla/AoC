import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day14.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""
    test_input = parse(read_test(test_input))
    test(calulate_pos(test_input[-2],5,(11,7)),(1,3))
    # test(task1(test_input), 12)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(1, 1)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    task2(input)
    print(f"Task 2 solution: fuck you")


#########################################################

def calulate_pos(robot, t,size=(101,103)):
    pos, vel = robot
    return ((pos[0] + t * vel[0])%size[0], (pos[1] + t * vel[1])%size[1])

def task1(input):
    size = (101,103)
    after_sim = []

    for r in input:
        after_sim.append(calulate_pos(r, 100, size))

    hx = size[0]//2
    hy = size[1]//2
    quadrants = [(0,0, hx, hy), (hx+1,0, size[0], hy), (0, hy+1, hx, size[1]), (hx+1, hy+1, size[0], size[1])]
    sum = 1
    for sx,sy,ex,ey in quadrants:
        count = 0
        for y in range(sy, ey):
            for x in range(sx, ex):
                count += len([i for i in after_sim if i == (x,y)])
        sum *= count
    return sum


def task2(inputt):
    size = (101,103)
    after_sim = []

    for t in range(5000,10000):
        for r in inputt:
            after_sim.append(calulate_pos(r, t, size))
        display = [[0 for x in range(size[0])] for y in range(size[1])]
        for x in range(size[0]):
            for y in range(size[1]):
                if (x,y) in after_sim:
                    display[y][x] = 1
        
        ## save the matrix as an image
        from PIL import Image
        img = Image.new('RGB', (size[0], size[1]), color = 'white')
        for x in range(size[0]):
            for y in range(size[1]):
                if display[y][x] == 1:
                    img.putpixel((x,y), (0,0,0))
        img.save(f"day14/output/{t}.png")

        after_sim = []

import re
def parse(input):
    robots = []
    regex = re.compile(r"p=(-?\d+,-?\d+) v=(-?\d+,-?\d+)")
    for line in input:
        pos, vel = regex.match(line).groups()
        pos = list(map(int, pos.split(",")))
        vel = list(map(int, vel.split(",")))
        robots.append((pos, vel))
    return robots



if __name__ == "__main__":
    # benchmark(main)
    main()
