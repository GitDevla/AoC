const utils = require('../utils');

function Parser(file) {
    return utils.read(file).split('\n').map(i => i.split(' '));
}

function PartOne(input) {
    let score = 0;
    input.forEach(i => {
        let [enemyPick, userPick] = i;
        if (userPick == "X") score += 1;
        if (userPick == "Y") score += 2;
        if (userPick == "Z") score += 3;
        if ((userPick == "X" & enemyPick == "C")
            || (userPick == "Y" & enemyPick == "A")
            || (userPick == "Z" & enemyPick == "B"))
            score += 6;
        else if ((userPick == "X" & enemyPick == "A")
            || (userPick == "Y" & enemyPick == "B")
            || (userPick == "Z" & enemyPick == "C"))
            score += 3;

    });
    return score;
}

let ASD = [1, 2, 3];

function PartTwo(input) {
    let score = 0;
    input.forEach(i => {
        let [enemyPick, userPick] = i;
        if (userPick == "X") {
            score += ASD[utils.mod((enemyPick.charCodeAt(0) - "A".charCodeAt(0) - 1), 3)];
        }
        if (userPick == "Y") {
            score += 3;
            score += ASD[(enemyPick.charCodeAt(0) - "A".charCodeAt(0)) % 3];
        }
        if (userPick == "Z") {
            score += 6;
            score += ASD[(enemyPick.charCodeAt(0) - "A".charCodeAt(0) + 1) % 3];
        }
    });
    return score;
}

// TESTS
const testInput = Parser("test.txt");
utils.test("Test 1", PartOne(testInput), 15);
utils.test("Test 2", PartTwo(testInput), 12);

// ANSWER
const input = Parser("input.txt");
console.log("Part 1 solution: " + PartOne(input)); // 14163
console.log("Part 2 solution: " + PartTwo(input)); // 12091