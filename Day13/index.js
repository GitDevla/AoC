const utils = require('../utils');

class PairPacket {
    constructor(left, right) {
        this.left = left;
        this.right = right;
    }
    compare() {
        return comparePacket(this.left, this.right);
    }
}

function comparePacket(left, right) {
    left = [...left];
    right = [...right]; // copy array
    for (let i = 0; i < Math.max(left.length, right.length); i++) {
        if (left[i] == undefined) return true;
        if (right[i] == undefined) return false;

        if (Array.isArray(left[i]) || Array.isArray(right[i])) {
            if (!Array.isArray(left[i]))
                left[i] = [left[i]];
            if (!Array.isArray(right[i]))
                right[i] = [right[i]];
            let res = comparePacket(left[i], right[i]);
            if (res != undefined) return res;
        }

        if (Number.isInteger(left[i]) && Number.isInteger(right[i])) {
            if (left[i] == right[i]) continue;
            return left[i] < right[i];
        }
    }
}


function Parser(file) {
    let data = utils.read(file).split('\n\n');
    let packets = [];
    for (const block of data) {
        let line = block.split("\n");
        packets.push(new PairPacket(eval(line[0]), eval(line[1])))
    }
    return packets;
}


function PartOne(pairs) {
    let sum = 0;
    for (let i = 0; i < pairs.length; i++)
        if (pairs[i].compare()) sum += i + 1;
    return sum;
}

function PartTwo(pairs) {
    let packets = pairs.flatMap(i => [i.left, i.right]);
    packets.push([[2]])
    packets.push([[6]])
    packets.sort((a, b) => comparePacket(b, a) - comparePacket(a, b));
    let a = packets.map(i => JSON.stringify(i)).indexOf(JSON.stringify([[2]])) + 1;
    let b = packets.map(i => JSON.stringify(i)).indexOf(JSON.stringify([[6]])) + 1;
    return a * b;
}

// TESTS
let testInput = Parser("test.txt");
utils.test("Test 1", PartOne(testInput), 13);
testInput = Parser("test.txt");
utils.test("Test 2", PartTwo(testInput), 140);

// ANSWER
let input = Parser("input.txt");
console.log("Part 1 solution: " + PartOne(input)); // 5013
input = Parser("input.txt");
console.log("Part 2 solution: " + PartTwo(input)); // 25038