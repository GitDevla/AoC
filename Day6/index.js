const utils = require('../utils');


function Parser(file) {
    return utils.read(file);
}

function findPacket(text, length) {
    for (let i = 0; i < text.length; i++) {
        var seen = new Set();
        for (let j = 0 + i; j < length + i; j++)
            seen.add(text[j]);
        if (seen.size == length) return i + length;
    }
}
const PartTwo = (text) => findPacket(text, 14)

const PartOne = (text) => findPacket(text, 4)

// TESTS
let testInput0 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
let testInput1 = "bvwbjplbgvbhsrlpgdmjqwftvncz";
let testInput2 = "nppdvjthqldpwncqszvftbrmjlhg";
let testInput3 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg";
let testInput4 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw";
utils.test("Test 1", PartOne(testInput0), 7);
utils.test("Test 1", PartOne(testInput1), 5);
utils.test("Test 1", PartOne(testInput2), 6);
utils.test("Test 1", PartOne(testInput3), 10);
utils.test("Test 1", PartOne(testInput4), 11);
// testInput = Parser("test.txt");
utils.test("Test 2", PartTwo(testInput0), 19);
utils.test("Test 2", PartTwo(testInput1), 23);
utils.test("Test 2", PartTwo(testInput2), 23);
utils.test("Test 2", PartTwo(testInput3), 29);
utils.test("Test 2", PartTwo(testInput4), 26);

// ANSWER
let input = Parser("input.txt");
console.log("Part 1 solution: " + PartOne(input)); // 1140
console.log("Part 2 solution: " + PartTwo(input)); // 3495