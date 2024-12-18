import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day18.txt"

TEST_INPUT ="""5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""

def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = parse(read_test(TEST_INPUT))
    test(task1(test_input), 22)

    # # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input,71,1024)}")


def pt2():
    # Test
    test_input = parse(read_test(TEST_INPUT))
    test(task2(test_input), "6,1")

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input,71)}")


#########################################################

def bfs(start,end,blocks):
    playarea = end[0]+1
    queue = []
    queue.append((start,0))
    visited = set()
    while len(queue) > 0:
        node,steps = queue.pop(0)
        if node == end:
            return steps
        if node in visited:
            continue
        visited.add(node)
        for d in [(-1,0),(1,0),(0,-1),(0,1)]:
            x,y = node
            nx = x+ d[0]
            ny = y+d[1]
            if nx < 0 or ny < 0 or ny >= playarea or nx >= playarea:
                continue
            if (nx,ny) in blocks:
                continue
            queue.append(((nx,ny),steps+1))
    return -1


def task1(input,size=7,limit=12):
    start = (0,0)
    end = (size-1,size-1)
    end = bfs(start,end,set(input[0:limit]))
    return end


def task2(input,size=7):
    start = (0,0)
    end = (size-1,size-1)
    range = [0,len(input)]
    while range[0] < range[1]:
        l = (range[0]+range[1])//2
        if bfs(start,end,set(input[:l])) == -1:
            range[1] = l
        else:
            range[0] = l+1
    return ",".join(map(str,input[range[0]-1]))

def parse(input):
    blocks = []
    for line in input:
        cords = line.split(",")
        x = int(cords[0])
        y = int(cords[1])
        blocks.append((x,y))
    return blocks

if __name__ == "__main__":
    benchmark(main)
    # main()
