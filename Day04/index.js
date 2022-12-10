const utils = require('../utils');

function Parser(file) {
    return utils.read(file).split('\n')
        .map(i => i.split(',').map(i =>
            i.split('-').map(i => parseInt(i))
        ));
}

function PartOne(input) {
    var sum = 0;
    for (const pair of input) {
        if (pair[0][0] <= pair[1][0] && pair[1][1] <= pair[0][1])
            sum++;
        else if (pair[1][0] <= pair[0][0] && pair[0][1] <= pair[1][1])
            sum++;
    }
    return sum;
}

function PartTwo(input) {
    var sum = 0;
    for (const pair of input) {
        if (pair[0][0] < pair[1][0] && pair[0][1] < pair[1][0])
            sum++;
        else if (pair[1][0] < pair[0][0] && pair[1][1] < pair[0][0])
            sum++;
    }
    return input.length - sum;
}

// TESTS
const testInput = Parser("test.txt");
utils.test("Test 1", PartOne(testInput), 2);
utils.test("Test 2", PartTwo(testInput), 4);

// ANSWER
const input = Parser("input.txt");
console.log("Part 1 solution: " + PartOne(input)); // 464
console.log("Part 2 solution: " + PartTwo(input)); // 770