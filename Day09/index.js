const utils = require('../utils');

class Cord {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
}

class Rope {
    Knots = [];
    constructor(length) {
        for (let i = 0; i < length; i++)
            this.Knots.push(new Cord(0, 0));
        this.Head = this.Knots[0];
    }

    moveUp() {
        this.Head.y++;
        this.tailLogic(this.Head);
    }
    moveDown() {
        this.Head.y--;
        this.tailLogic(this.Head);
    }
    moveRigth() {
        this.Head.x++;
        this.tailLogic(this.Head);
    }
    moveLeft() {
        this.Head.x--;
        this.tailLogic(this.Head);
    }

    tailLogic(before, currI = 1) {
        let curr = this.Knots[currI];
        if (curr == undefined) return;
        let diff = Math.max(Math.abs(before.y - curr.y), Math.abs(before.x - curr.x));
        if (diff < 2) return;
        let dirX = before.x - curr.x;
        let dirY = before.y - curr.y;
        curr.x += Math.abs(dirX) === 2 ? dirX / 2 : dirX;
        curr.y += Math.abs(dirY) === 2 ? dirY / 2 : dirY;
        this.tailLogic(curr, currI + 1);
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
            let last = rope.Knots.at(-1);
            tiles.add(`${last.y},${last.x} `);
        }
    }
    return tiles.size;
}

function PartTwo(moves) {
    return Task(moves, 10);
}
function PartOne(moves) {
    return Task(moves, 2);
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