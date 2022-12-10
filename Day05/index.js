const utils = require('../utils');


function Parser(file) {
    var file = utils.read(file).split('\n\n');
    // crates
    var list = file[0].split("\n");
    list.pop();
    list.reverse();
    var crates = [];
    list.forEach(i => {
        var index = 1;
        while (i[index] != undefined) {
            if (i[index] != " ") {
                var col = (index - 1) / 4;
                if (crates[col] == undefined) crates[col] = [];
                crates[col].push(i[index]);
            }
            index += 4;
        }
    })
    // moves
    let moves = [];
    list = file[1].split("\n");
    for (const move of list) {
        var temp = move.split(" ");
        moves.push([parseInt(temp[1]), parseInt(temp[3] - 1), parseInt(temp[5] - 1)]);
    }
    return [crates, moves];
}

function PartTwo([creates, moves]) {
    for (const move of moves) {
        var [times, from, to] = move;
        var spliced = creates[from].splice(times * -1)
        creates[to].push(...spliced);
    }
    return creates.reduce((a, b) => a + b.pop());
}

function PartOne([creates, moves]) {
    for (const move of moves) {
        var [times, from, to] = move;
        for (let i = 0; i < times; i++) {
            var pop = creates[from].pop();
            creates[to].push(pop);
        }
    }
    return creates.reduce((a, b) => a + b.pop());
}

// TESTS
let testInput = Parser("test.txt");
utils.test("Test 1", PartOne(testInput), "CMZ");
testInput = Parser("test.txt");
utils.test("Test 2", PartTwo(testInput), "MCD");

// ANSWER
let input = Parser("input.txt");
console.log("Part 1 solution: " + PartOne(input)); // ZRLJGSCTR
input = Parser("input.txt");
console.log("Part 2 solution: " + PartTwo(input)); // PRTTGRFPB