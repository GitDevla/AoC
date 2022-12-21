const utils = require('../utils');

function Parser(file) {
    return utils.read(file).split('\n').map(i => parseInt(i));
}

function decrypt(sequence, original) {
    for (let i = 0; i < original.length; i++) {
        let offset = original[i];
        let currIndex = sequence.findIndex(x => x.index === i);
        sequence.splice(currIndex, 1);
        sequence.splice(utils.mod((offset + currIndex), sequence.length), 0, { index: i, num: offset });
    }
    return sequence;
}

function getSolution(list) {
    let zeroPos = list.findIndex(x => x.num === 0);
    return [1000, 2000, 3000].reduce((a, b) => a + list[(b + zeroPos) % list.length].num, 0);
}

function PartOne(sequence) {
    let list = sequence.map((n, i) => ({ index: i, num: n }));
    decrypt(list, sequence)
    return getSolution(list);
}

function PartTwo(sequence) {
    sequence = sequence.map(i => i * 811589153)
    let list = sequence.map((n, i) => ({ index: i, num: n }));
    for (let i = 0; i < 10; i++)
        decrypt(list, sequence)
    return getSolution(list);
}

// TESTS
let testInput = Parser("test.txt");
utils.test("Test 1", PartOne(testInput), 3);
testInput = Parser("test.txt");
utils.test("Test 2", PartTwo(testInput), 1623178306);

// ANSWER
let input = Parser("input.txt");
console.log("Part 1 solution: " + PartOne(input)); // 4151
input = Parser("input.txt");
console.log("Part 2 solution: " + PartTwo(input)); // 7848878698663