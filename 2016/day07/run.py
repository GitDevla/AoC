import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day07.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test(support_TLS("abba[mnop]qrst"), True)
    test(support_TLS("abcd[bddb]xyyx"), False)
    test(support_TLS("aaaa[qwer]tyui"), False)
    test(support_TLS("ioxxoj[asdfgh]zxcvbn"), True)

    # Solution
    input = read_file(FILE)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(support_SSL("aba[bab]xyz"), True)
    test(support_SSL("xyx[xyx]xyx"), False)
    test(support_SSL("aaa[kek]eke"), True)
    test(support_SSL("zazbz[bzb]cdb"), True)

    # Solution
    input = read_file(FILE)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    return sum([support_TLS(x) for x in input])


def task2(input):
    return sum([support_SSL(x) for x in input])


def support_SSL(input: str):
    hypernets = get_hypernets(input)
    hypernet_ABAs = []
    for x in hypernets:
        hypernet_ABAs.extend(find_aba(x))
    if len(hypernet_ABAs) == 0:
        return False
    supernet = get_supernet(input)

    return any(supernet.find(ABA_to_BAB(x)) >= 0 for x in hypernet_ABAs)


def support_TLS(input: str):
    hypernets = get_hypernets(input)
    if any(len(find_abba(x)) > 0 for x in hypernets):
        return False

    supernet = get_supernet(input)
    abbas = find_abba(supernet)
    return len(abbas) > 0


def get_hypernets(input):
    starts = []
    ends = []
    for i, c in enumerate(input):
        if c == "[":
            starts.append(i)
        elif c == "]":
            ends.append(i)
    hypernets = []
    for x in range(len(starts)):
        hypernets.append(input[starts[x] + 1 : ends[x]])
    return hypernets


def get_supernet(input):
    supernet = input
    hypernets = get_hypernets(input)
    for x in hypernets:
        supernet = supernet.replace(x, "")
    return supernet


def find_aba(input):
    temp = []
    for c in range(len(input)):
        slice = input[c : 3 + c]
        if len(slice) < 3:
            continue
        if slice[0] != slice[2]:  # XaX
            continue
        if slice[0] == slice[1]:  # XAx
            continue
        temp.append(slice)
    return temp


def find_abba(input):
    temp = []
    for c in range(len(input)):
        slice = input[c : 4 + c]
        if len(slice) < 4:
            continue
        if slice[0] != slice[3]:  # XaaX
            continue
        if slice[1] != slice[2]:  # xAAx
            continue
        if slice[0] == slice[1]:  # XAax
            continue
        temp.append(slice)
    return temp


def ABA_to_BAB(input):
    a = input[0]
    b = input[1]
    return f"{b}{a}{b}"


if __name__ == "__main__":
    # benchmark(main)
    main()
