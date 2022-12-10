const utils = require('../utils');

function Parser(file) {
    return utils.read(file).split('\n');
}

function findDupli(first, second) {
    for (const letter of first)
        if (second.includes(letter)) return letter;
}

function getPriority(letter) {
    if (letter == letter.toLowerCase())
        return letter.charCodeAt() - "a".charCodeAt() + 1;
    if (letter == letter.toUpperCase())
        return letter.charCodeAt() - "A".charCodeAt() + 27;
}

function sliceIntoChunks(arr, chunkSize) {
    const res = [];
    for (let i = 0; i < arr.length; i += chunkSize) {
        const chunk = arr.slice(i, i + chunkSize);
        res.push(chunk);
    }
    return res;
}

function findTripl(first, second, third) {
    for (const letter of first)
        if (second.includes(letter) && third.includes(letter)) return letter;
}

function PartOne(input) {
    var sum = 0;
    input.forEach(i => {
        var half = i.length / 2;
        var firstCompartment = i.slice(0, half);
        var secondCompartment = i.slice(half);
        var double = findDupli(firstCompartment, secondCompartment);
        sum += getPriority(double);
    })
    return sum;
}

function PartTwo(input) {
    var teams = sliceIntoChunks(input, 3);
    var sum = 0;
    teams.forEach(i => {
        var first = i[0];
        var second = i[1];
        var third = i[2];
        var badge = findTripl(first, second, third);
        sum += getPriority(badge);
    })
    return sum;
}

// TESTS
const testInput = Parser("test.txt");
utils.test("Test 1", PartOne(testInput), 157);
utils.test("Test 2", PartTwo(testInput), 70);

// ANSWER
const input = Parser("input.txt");
console.log("Part 1 solution: " + PartOne(input)); // 7878
console.log("Part 2 solution: " + PartTwo(input)); // 2760