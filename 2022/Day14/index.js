const utils = require('../utils');

class elements {
    static air = ".";
    static rock = "#";
    static sand = "o";
}

function pointsBetween(one, two) {
    let points = [];
    let higherX = Math.max(one[0], two[0])
    let lowerX = Math.min(one[0], two[0])
    for (let i = lowerX; i <= higherX; i++)
        points.push([i, one[1]]);

    let higherY = Math.max(one[1], two[1])
    let lowerY = Math.min(one[1], two[1])
    for (let i = lowerY; i <= higherY; i++)
        points.push([one[0], i]);
    return points
}

function Parser(file) {
    let data = utils.read(file).split('\n').map(row => row.split(" -> ").map(i => i.split(",").map(i => parseInt(i))));
    let height = Math.max(...data.flatMap(i => i.flatMap(i => i[1]))) + 2;
    let filler = height * 2;
    let start = Math.min(...data.flatMap(i => i.flatMap(i => i[0]))) - filler;
    data = data.map(i => i.map(i => [i[0] - start, i[1]]));
    let width = Math.max(...data.flatMap(i => i.flatMap(i => i[0]))) + filler;

    let map = Array(height).fill().map(() => Array(width).fill(elements.air));
    for (const row of data) {
        for (let i = 0; i < row.length - 1; i++) {
            let curr = row[i];
            let next = row[i + 1];
            for (const point of pointsBetween(curr, next)) {
                map[point[1]][point[0]] = elements.rock;
            }
        }
    }
    return { map: map, start: start };
}

function sandSimulate(map, pos, stopOnFloor) {
    let rest = false;
    let [x, y] = pos;
    if (map[y][x] != elements.air) return true;
    while (!rest) {
        if (map[y + 1] == undefined)
            if (stopOnFloor)
                return true;
            else break;
        if (map[y + 1][x] == elements.air) {
            y++;
            continue;
        } else if (map[y + 1][x - 1] == elements.air) {
            x--;
            y++;
            continue;
        }
        else if (map[y + 1][x + 1] == elements.air) {
            x++;
            y++;
            continue;
        }
        rest = true;
    }
    map[y][x] = elements.sand;
}

function PartOne({ map, start }) {
    let i = 0;
    while (!sandSimulate(map, [500 - start, 0], true)) i++;
    return i;
}

function PartTwo({ map, start }) {
    let i = 0;
    while (!sandSimulate(map, [500 - start, 0], false)) i++;
    return i;
}

// TESTS
let testInput = Parser("test.txt");
utils.test("Test 1", PartOne(testInput), 24);
testInput = Parser("test.txt");
utils.test("Test 2", PartTwo(testInput), 93);

// ANSWER
let input = Parser("input.txt");
console.log("Part 1 solution: " + PartOne(input)); // 885
input = Parser("input.txt");
console.log("Part 2 solution: " + PartTwo(input)); // 28691