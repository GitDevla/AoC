from utils import *

FILE = "input/day04.txt"


def main():
    pt1()
    pt2()


def pt1():
    # Test
    test(israel("aaaaa-bbb-z-y-x-123[abxyz]"), 123)
    test(israel("a-b-c-d-e-f-g-h-987[abcde]"), 987)
    test(israel("not-a-real-room-404[oarel]"), 404)
    test(israel("totally-real-room-200[decoy]"), 0)

    # Solution
    input = read_file(FILE)
    print(f"Task 1 solution: {task1(input)}")


def pt2():
    # Test
    test(decript("qzmt-zixmtkozy-ivhz-343[12345]"), "very encrypted name")

    # Solution
    input = read_file(FILE)
    print(f"Task 2 solution: {task2(input)}")


#########################################################


def task1(input):
    return sum([israel(x) for x in input])


def task2(input):
    for line in input:
        is_real = israel(line)
        if is_real == 0:
            continue
        decripted = decript(line)
        if decripted == "northpole object storage":
            name = line[:-7]
            id = int(name.split("-")[-1])
            return id


def israel(name: str):
    checksum = name[-6:-1]
    enc = name[:-7]
    id = int(enc.split("-")[-1])
    enc = "".join(enc.split("-")[:-1])

    hashmap = {}
    for letter in enc:
        if hashmap.get(letter) == None:
            hashmap[letter] = 0
        hashmap[letter] += 1

    sort = sorted(hashmap.items(), key=lambda x: (-x[1], x[0]))
    hash = "".join(x[0] for x in sort[:5])
    if checksum == hash:
        return id
    else:
        return 0


def decript(name: str):
    encoded = name[:-7]
    id = int(encoded.split("-")[-1])
    encoded = " ".join(encoded.split("-")[:-1])

    MIN = ord("a")
    MAX = ord("z")
    decoded = []
    for letter in encoded:
        if letter == " ":
            decoded.append(" ")
            continue
        d_char = chr(((ord(letter) + id - MIN) % (MAX - MIN + 1)) + MIN)
        decoded.append(d_char)
    return "".join(decoded)


if __name__ == "__main__":
    # benchmark(main())
    main()
