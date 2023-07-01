const utils = require('../utils');

class Cord {
    constructor(y, x) {
        this.y = y;
        this.x = x;
    }

    add(cord) {
        return new Cord(this.y + cord.y, this.x + cord.x);
    }

    is(cord) {
        return this.y == cord.y && this.x == cord.x;
    }

    stringify() {
        return `${this.y},${this.x}`
    }
}

var dirs = [
    up = new Cord(-1, 0),
    down = new Cord(1, 0),
    left = new Cord(0, -1),
    right = new Cord(0, 1),
]


function getHeight(char) {
    return char.charCodeAt() - "a".charCodeAt();
}

function Parser(file) {
    let map = utils.read(file).split('\n').map(i => i.split(""));
    let start;
    let end;
    for (let y = 0; y < map.length; y++) {
        for (let x = 0; x < map[0].length; x++) {
            if (map[y][x] == "S") {
                start = new Cord(y, x);
                map[y][x] = "a"
            }
            else if (map[y][x] == "E") {
                end = new Cord(y, x);
                map[y][x] = "z";
            }
            map[y][x] = getHeight(map[y][x]);
        }
    }
    return { map: map, start: start, end: end };
}

function getNeighbors(map, cord) {
    var neigbors = [];
    for (const dir of dirs) {
        let next = cord.add(dir)
        if (map[next.y] == undefined) continue;
        if (map[next.y][next.x] == undefined) continue;
        neigbors.push(next);
    }
    return neigbors;
}

function setAdd(set, objects) {
    return objects.map(i => i.stringify()).forEach(i => set.add(i));
}

function PartOne({ map, start, end }) {
    let visited = new Set();
    let queue = getNeighbors(map, start);
    queue = queue.filter(i => !(map[start.y][start.x] < map[i.y][i.x] - 1))
    setAdd(visited, queue);
    let i = 1;
    while (true) {
        i++;
        let tempQue = []
        while (queue.length != 0) {
            let next = queue.shift(1);
            let cords = getNeighbors(map, next);
            cords = cords.filter(i => !visited.has(i.stringify()))
            cords = cords.filter(i => !(map[next.y][next.x] < map[i.y][i.x] - 1))
            tempQue.push(...cords)
            setAdd(visited, tempQue);
            if (cords.find(i => end.is(i))) return i;
        }
        queue.push(...tempQue)
        if (queue.length == 0) return -1;
    }
}

function PartTwo({ map, end }) {
    let start = end;
    let visited = new Set();
    let queue = getNeighbors(map, start);
    queue = queue.filter(i => !(map[start.y][start.x] > map[i.y][i.x] + 1))
    setAdd(visited, queue);
    let i = 1;
    while (true) {
        i++;
        let tempQue = []
        while (queue.length != 0) {
            let next = queue.shift(1);
            let cords = getNeighbors(map, next);
            cords = cords.filter(i => !visited.has(i.stringify()))
            cords = cords.filter(i => !(map[next.y][next.x] > map[i.y][i.x] + 1))
            tempQue.push(...cords)
            setAdd(visited, tempQue);
            if (cords.find(i => map[i.y][i.x] == 0)) return i;
        }
        queue.push(...tempQue)
        if (queue.length == 0) return -1;
    }
}

// TESTS
let testInput = Parser("test.txt");
utils.test("Test 1", PartOne(testInput), 31);
testInput = Parser("test.txt");
utils.test("Test 2", PartTwo(testInput), 29);

// ANSWER
let input = Parser("input.txt");
console.log("Part 1 solution: " + PartOne(input)); // 481
input = Parser("input.txt");
console.log("Part 2 solution: " + PartTwo(input)); // 480