const utils = require('../utils');

function parser(file) {
    return utils.read(file).split('\n\n')
}

function Task1(input) {
    var sums = input.map(group =>
        utils.sum(group.split("\n"))
    );
    return Math.max(...sums);
}

function Task2(input) {
    var sums = input.map(group =>
        utils.sum(group.split("\n"))
    );
    let sorted = sums.sort((a, b) => b - a);
    return utils.sum(sorted.splice(0, 3));
}

// TESTS
const testInput = parser("testInput.txt");
utils.test("Test 1", Task1(testInput), 24000);
utils.test("Test 2", Task2(testInput), 45000);

// ANSWER
const input = parser("input.txt");
console.log("Task 1 solution: " + Task1(input));
console.log("Task 2 solution: " + Task2(input));