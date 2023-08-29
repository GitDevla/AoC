import re
import sys
from pathlib import Path
from hashlib import md5 as hashlib_md5

sys.path.append(str(Path(__file__).resolve().parents[1]))
from utils.utils import *

FILE = "input/day14.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test(task1("abc"), 22728)

    # Solution
    input = read_file(FILE)[0]
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(task2("abc"), 22551)

    # Solution
    input = read_file(FILE)[0]
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    idx = 0
    answers = []
    cache = {}
    while len(answers) < 64:
        hash = cache[idx] if cache.get(idx) else md5(f"{input}{idx}")
        has_triplet = contains_triplet(hash)

        if has_triplet != None:
            for x in range(1, 1000):
                next = cache[idx + x] if cache.get(idx + x) else md5(f"{input}{idx+x}")
                cache[idx + x] = next
                if contains_fifthlet_with(next, has_triplet):
                    answers.append(idx)
                    break
        idx += 1
    return answers[63]


def task2(input):
    idx = 0
    answers = []
    cache = {}
    while len(answers) < 64:
        hash = strech(f"{input}{idx}", cache)
        has_triplet = contains_triplet(hash)

        if has_triplet != None:
            for x in range(1, 1001):
                next = strech(f"{input}{idx+x}", cache)
                if contains_fifthlet_with(next, has_triplet):
                    answers.append(idx)
                    break
        idx += 1
    return answers[63]


def md5(input):
    md5_hash = hashlib_md5()
    md5_hash.update(input.encode("utf-8"))
    return md5_hash.hexdigest()


regex = re.compile(r"(.)\1{2}")


def contains_triplet(input):
    found = regex.search(input)
    if not found:
        return None
    return found.group(0)[0]


def contains_fifthlet_with(input: str, withh):
    return (withh * 5) in input


def strech(input, cache={}):
    if cache.get(input):
        return cache[input]
    hash = input
    for _ in range(2017):
        hash = md5(hash)

    cache[input] = hash
    return hash


if __name__ == "__main__":
    # benchmark(main)
    main()
