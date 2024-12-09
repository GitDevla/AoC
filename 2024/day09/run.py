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
    test(convert_to_fs(parse("12345")), ['0', '.', '.', '1', '1', '1', '.', '.', '.', '.', '2', '2', '2', '2', '2'])
    test(convert_to_fs(parse("2333133121414131402")), ['0', '0', '.', '.', '.', '1', '1', '1', '.', '.', '.', '2', '.', '.', '.', '3', '3', '3', '.', '4', '4', '.', '5', '5', '5', '5', '.', '6', '6', '6', '6', '.', '7', '7', '7', '.', '8', '8', '8', '8', '9', '9'])
    test(task1(parse("2333133121414131402")), 1928)

    # Solution
    input = read_file(FILE)[0]
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(task2(parse("2333133121414131402")), 2858)


    # Solution
    input = read_file(FILE)
    input = parse(input[0])
    print(f"Task 2 solution: {task2(input)}")


#########################################################

def convert_to_fs(input):
    isFile = True
    ret = []
    idx = -1
    for i in input:
        if isFile:
            idx +=1
        
        if not isFile:
            ret.extend(["."]*int(i))
        else:
            ret.extend([str(idx)]*int(i))
        isFile = not isFile
    return ret

def checkValidity(input):
    isFile = True
    for i in input:
        if not isFile:
            if i != ".":
                return False
        if i == ".":
            isFile = False
    return True

def findRightmostNumber(input):
    for i in range(len(input)-1, -1, -1):
        if input[i].isdigit():
            return i
    return -1


def task1(input):
    fs = convert_to_fs(input)
    checksum = 0;
    idx  = 0
    while len(fs) > 0:
        first = fs.pop(0)
        if first == ".":
            last = "."
            while last == ".":
                last = fs.pop()
            first = last
        checksum += int(first)*idx
        idx += 1
    return checksum

def convert_to_cluster_fs(input):
    isFile = True
    ret = []
    idx = -1
    for i in input:
        if isFile:
            idx +=1

        if not isFile:
            ret.append((-1, int(i)))
        else:
            ret.append((idx,int(i)))
        isFile = not isFile
    return ret

def findEmptyCluster(fs,size):
    for i in range(len(fs)):
        if fs[i][0] == -1:
            if fs[i][1] >= size:
                return i
    return -1

def task2(input):
    fs = convert_to_cluster_fs(input)
   
    for i in range(len(fs)-1,0,-1):
        curr = fs[i]
        if curr[0] == -1:
            continue
        possible = findEmptyCluster(fs[:i],curr[1])
        if possible != -1:
            leftoverSpace = fs[possible][1] - curr[1]
            fs[possible] = (curr[0],curr[1])
            fs[i] = (-1,curr[1])
            fs.insert(possible+1,(-1,leftoverSpace))
     

    checksum = 0
    i= 0
    for v in fs:
        if v[0] != -1:
            for j in range(v[1]):
                checksum += v[0]*i
                i += 1
        else:
            i+=v[1]
    return checksum


def toString(fs):
    return "".join([("."*i[1]) if i[0]==-1 else (str(i[0])*i[1]) for i in fs])

def parse(input):
    return [*input]

if __name__ == "__main__":
    benchmark(main)
    # main()
