const utils = require('../utils');

class elements {
    static lava = "🌋";
    static air = " ";
    static water = "💧";
}

function Parser(file) {
    var drops = utils.read(file).split('\n').map(row => row.split(",").map(i => parseInt(i)));
    return drops;
}

let dirs = [
    [0, 0, 1],
    [0, 0, -1],
    [0, 1, 0],
    [0, -1, 0],
    [1, 0, 0],
    [-1, 0, 0],
]

function PartOne(drops) {
    let sum = 0;
    for (const drop of drops) {
        let [x, y, z] = drop;
        let sides = 6;
        for (const dir of dirs) {
            let [dx, dy, dz] = dir;
            let fx = x + dx, fy = y + dy, fz = z + dz;
            if (drops.some(i => i[0] == fx && i[1] == fy && i[2] == fz))
                sides--;
        }
        sum += sides;
    }
    return sum;
}

function PartTwo(drops) {
    drops = drops.map(i => i.map(i => i + 1));
    var x = Math.max(...drops.flatMap(i => i[0])) + 2;
    var y = Math.max(...drops.flatMap(i => i[1])) + 2;
    var z = Math.max(...drops.flatMap(i => i[2])) + 2;
    let map = Array(x).fill().map(() => Array(y).fill().map(() => Array(z).fill(elements.air)));
    for (const lava of drops) {
        let [x, y, z] = lava;
        map[x][y][z] = elements.lava;
    }

    let queue = [[0, 0, 0]];
    while (queue.length > 0) {
        let [x, y, z] = queue.shift(1);
        for (const dir of dirs) {
            let [dx, dy, dz] = dir;
            let fx = x + dx, fy = y + dy, fz = z + dz;
            if (map[fx] == undefined) continue;
            if (map[fx][fy] == undefined) continue;
            if (map[fx][fy][fz] == elements.air) {
                queue.push([fx, fy, fz]);
                map[fx][fy][fz] = elements.water;
            }
        }
    }

    let sum = 0;
    for (const drop of drops) {
        let [x, y, z] = drop;
        let sides = 6;
        for (const dir of dirs) {
            let [dx, dy, dz] = dir;
            let fx = x + dx, fy = y + dy, fz = z + dz;
            if (map[fx] == undefined) continue;
            if (map[fx][fy] == undefined) continue;
            if (map[fx][fy][fz] == elements.air || map[fx][fy][fz] == elements.lava)
                sides--;
        }
        sum += sides;
    }
    return sum;
}

// TESTS
let testInput = Parser("test.txt");
utils.test("Test 1", PartOne(testInput), 64);
testInput = Parser("test.txt");
utils.test("Test 2", PartTwo(testInput), 58);

// ANSWER
let input = Parser("input.txt");
console.log("Part 1 solution: " + PartOne(input)); // 4400
input = Parser("input.txt");
console.log("Part 2 solution: " + PartTwo(input)); // 2522