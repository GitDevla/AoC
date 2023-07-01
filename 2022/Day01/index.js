const utils = require('../utils');

function Parser(file) {
    return utils.read(file).split('\n\n')
}

function PartOne(input) {
    var sums = input.map(group =>
        utils.sum(group.split("\n"))
    );
    return Math.max(...sums);
}

function PartTwo(input) {
    var sums = input.map(group =>
        utils.sum(group.split("\n"))
    );
    let sorted = sums.sort((a, b) => b - a);
    return utils.sum(sorted.splice(0, 3));
}

// TESTS
const testInput = Parser("test.txt");
utils.test("Test 1", PartOne(testInput), 24000);
utils.test("Test 2", PartTwo(testInput), 45000);

// ANSWER
const input = Parser("input.txt");
console.log("Part 1 solution: " + PartOne(input)); // 68775
console.log("Part 2 solution: " + PartTwo(input)); // 202585