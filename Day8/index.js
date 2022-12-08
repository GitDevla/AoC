const utils = require('../utils');

/*dont read this*/
function Parser(file) {
    return utils.read(file).split('\n').map(i => i.split('').map(i => parseInt(i)));

}

function PartTwo(forest) {
    let rows = forest.length;
    let columns = forest[1].length;
    let trees = Array(rows).fill().map(() => Array(columns).fill(0));
    for (let y = 1; y < rows - 1; y++) {
        for (let x = 1; x < columns - 1; x++) {
            trees[y][x] = lookAround(forest, y, x);
        }
    }
    let a = trees.map(i => Math.max(...i));
    return Math.max(...a);
}

function lookAround(forest, y, x) {
    let point = 1;
    let tree = forest[y][x];
    let up = y;
    let trees = 0;
    do {
        up--;
        trees++;
    } while (up > 0 && tree > forest[up][x]);
    point *= trees;
    let down = y;
    trees = 0;
    do {
        down++;
        trees++;
    } while (down < forest.length - 1 && tree > forest[down][x]);
    point *= trees;
    let left = x;
    trees = 0;
    do {
        left--;
        trees++;
    } while (left > 0 && tree > forest[y][left]);
    point *= trees;
    let right = x;
    trees = 0;
    do {
        right++;
        trees++;
    } while (right < forest[0].length - 1 && tree > forest[y][right]);
    point *= trees;
    return point;
}

function PartOne(forest) {
    let rows = forest.length;
    let columns = forest[1].length;
    let trees = Array(rows).fill().map(() => Array(columns).fill(false));
    for (let y = 1; y < rows - 1; y++) {
        const row = forest[y];
        let tallest = row[0];
        for (let x = 1; x < columns - 1; x++) {
            const tree = row[x];
            if (tallest >= tree) continue;
            tallest = tree
            trees[y][x] = true;
        }
    }

    for (let y = 1; y < rows - 1; y++) {
        const row = forest[y];
        let tallest = row[columns - 1];
        for (let x = columns - 2; x > 0; x--) {
            const tree = row[x];
            if (tallest >= tree) continue;
            tallest = tree
            trees[y][x] = true;

        }
    }

    for (let x = 1; x < columns - 1; x++) {
        let tallest = forest[0][x];
        for (let y = 1; y < rows - 1; y++) {
            const tree = forest[y][x];
            if (tallest >= tree) continue;
            tallest = tree
            trees[y][x] = true;

        }
    }

    for (let x = 1; x < columns - 1; x++) {
        let tallest = forest[rows - 1][x];
        for (let y = rows - 2; y > 0; y--) {
            const tree = forest[y][x];
            if (tallest >= tree) continue;
            tallest = tree
            trees[y][x] = true;

        }
    }

    var sum = rows * 2 + (columns - 2) * 2;
    for (const row of trees) {
        for (const i of row) {
            sum += i;
        }
    }
    return sum;
}

// TESTS
let testInput = Parser("test.txt");
utils.test("Test 1", PartOne(testInput), 21);
testInput = Parser("test.txt");
utils.test("Test 2", PartTwo(testInput), 8);

// ANSWER
let input = Parser("input.txt");
console.log("Part 1 solution: " + PartOne(input)); // 1736
input = Parser("input.txt");
console.log("Part 2 solution: " + PartTwo(input)); // 268800