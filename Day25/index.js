const utils = require('../utils');

function Parser(file) {
    return utils.read(file).split('\n');
}

var SNAFUDigits = [
    0, 1, 2
]
SNAFUDigits["-"] = -1;
SNAFUDigits["="] = -2;

function convertToDecimal(SNAFU) {
    let num = 0;
    for (let i = 0; i < SNAFU.length; i++) {
        let place = Math.pow(5, SNAFU.length - i - 1);
        num += place * SNAFUDigits[SNAFU[i]];
    }
    return num;
}

function convertToSNAFU(decimal) {
    decimal = parseInt(decimal);
    let num = "";
    while (decimal > 0) {
        let rem = (decimal % 5).toString();
        if (rem > 2) {
            let minus = 5 - rem;
            rem = minus == 1 ? "-" : "="
            decimal += minus;
        }
        num += rem;
        decimal = Math.floor(decimal / 5);
    }
    return num.split("").reverse().join("");
}

function PartOne(nums) {
    return convertToSNAFU(nums.reduce((a, b) => a + convertToDecimal(b), 0));
}

function PartTwo(nums) {
    // Got cock blocked
}

// TESTS
let testInput = Parser("test.txt");
utils.test("Test 1", PartOne(testInput), "2=-1=0");
// testInput = Parser("test.txt");
// utils.test("Test 2", PartTwo(testInput), 301);

// ANSWER
let input = Parser("input.txt");
console.log("Part 1 solution: " + PartOne(input)); // 2---1010-0=1220-=010
// input = Parser("input.txt");
// console.log("Part 2 solution: " + PartTwo(input)); // 