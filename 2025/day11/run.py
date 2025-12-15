import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day11.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test_input = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""
    test_input = parse(read_test(test_input))
    test(task1(test_input), 5)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test

    test_input = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""
    test_input = parse(read_test(test_input))
    test(task2(test_input), 2)

    # Solution
    input = read_file(FILE)
    input = parse(input)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def parse(input):
    out = []
    for line in input:
        input, output = line.split(": ")
        outputs = output.split(" ")
        out.append((input, outputs))
    return out


def task1(input):
    input = {k: (v, 0) for k, v in input}
    input["out"] = ([], 1)
    start = "you"
    end = "out"
    return wayt_to_out(input, start, end)


def wayt_to_out(ways, start, end, disabled=set()):
    ways = ways.copy()
    ways[end] = (ways[end][0], 1)

    def backtrack(node):
        nexts, ways_to_out = ways[node]
        if node in disabled:
            return 0
        if ways_to_out > 0:
            return ways_to_out
        total = 0
        valid_nexts = []
        for n in nexts:
            xd = backtrack(n)
            if xd != 0:
                valid_nexts.append(n)
            total += xd
        ways[node] = (valid_nexts, total)
        return total

    return backtrack(start)


def collapse(ways, excepts=set()):
    changed = True
    while changed:
        changed = False
        for k, (nxts, ways_to_out) in list(ways.items()):
            if k in excepts:
                continue
            if ways_to_out > 0 or len(nxts) != 1:
                continue
            for kk, (nnxts, nways) in list(ways.items()):
                if k in nnxts:
                    nnxts = [x if x != k else nxts[0] for x in nnxts]
                    ways[kk] = (nnxts, nways)
                    changed = True
            del ways[k]
            if changed:
                break

    return ways


def task2(input):
    input = {k: (v, 0) for k, v in input}
    # input = collapse(input, excepts={"fft", "dac", "svr", "out"})
    input["out"] = ([], 0)
    start = "svr"
    ways_to_fft_out = wayt_to_out(input, "fft", "out", disabled={"dac"})
    ways_to_dac_out = wayt_to_out(input, "dac", "out", disabled={"fft"})

    ways_to_fft_dac = wayt_to_out(input, "fft", "dac")
    ways_to_dac_fft = wayt_to_out(input, "dac", "fft")

    ways_tp_svr_fft = wayt_to_out(input, start, "fft", disabled={"dac"})
    ways_tp_svr_dac = wayt_to_out(input, start, "dac", disabled={"fft"})
    a = ways_tp_svr_fft * ways_to_fft_dac * ways_to_dac_out
    b = ways_tp_svr_dac * ways_to_dac_fft * ways_to_fft_out
    return a + b


if __name__ == "__main__":
    # benchmark(main)
    main()
