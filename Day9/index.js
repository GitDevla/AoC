const utils = require('../utils');

class Cord {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
}

class Rope {
    Head = new Cord(0, 0);
    Tails = [];

    constructor(length = 1) {
        for (let i = 0; i < length; i++) {
            this.Tails.push(new Cord(0, 0));
        }
    }

    moveUp() {
        this.Head.y++;
        this.tailLogic(0, 1);
    }
    moveDown() {
        this.Head.y--;
        this.tailLogic(0, -1);
    }
    moveRigth() {
        this.Head.x++;
        this.tailLogic(1, 0);
    }
    moveLeft() {
        this.Head.x--;
        this.tailLogic(-1, 0);
    }


    tailLogic(x = 0, y = 0, before = this.Head, currI = 0) {
        let curr = this.Tails[currI];
        if (curr == undefined) return;
        let diff = Math.max(Math.abs(before.y - curr.y), Math.abs(before.x - curr.x));
        if (diff < 2) return;
        curr.x += x;
        curr.y += y;
        let rowDiff = 0;
        let colDiff = 0;
        if (Math.abs(x) == Math.abs(y)) {

        }
        else if (x != 0) {
            rowDiff = before.y - curr.y;
            curr.y += rowDiff;
        }
        else if (y != 0) {
            colDiff = before.x - curr.x;
            curr.x += colDiff;
        }
        this.tailLogic(x + colDiff, y + rowDiff, curr, currI + 1);
    }
}

function Parser(file) {
    return utils.read(file).split('\n').map(i => i.split(' '));
}

function Task(moves, length) {
    let rope = new Rope(length);
    let tiles = new Set();
    for (const move of moves) {
        let times = move[1];
        let dir = move[0];
        for (let i = 0; i < times; i++) {
            switch (dir) {
                case "U":
                    rope.moveUp();
                    break;
                case "D":
                    rope.moveDown();
                    break;
                case "L":
                    rope.moveLeft();
                    break;
                case "R":
                    rope.moveRigth();
                    break;
            }
            let last = rope.Tails.at(-1);
            tiles.add(`${last.y},${last.x} `);
        }
    }
    return tiles.size;
}

function PartTwo(moves) {
    return Task(moves, 10);
}
function PartOne(moves) {
    return Task(moves, 1);
}

// TESTS
let testInput = Parser("test.txt");
utils.test("Test 1", PartOne(testInput), 13);
testInput = Parser("test.txt");
utils.test("Test 2/1", PartTwo(testInput), 1);
testInput = Parser("test2.txt");
utils.test("Test 2/2", PartTwo(testInput), 36);

// ANSWER
let input = Parser("input.txt");
console.log("Part 1 solution: " + PartOne(input)); // 5619
input = Parser("input.txt");
console.log("Part 2 solution: " + PartTwo(input)); // 2376