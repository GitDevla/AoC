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

    isOpposite(cord) {
        return this.y == cord.y * -1 && this.x == cord.x * -1;
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
// var foundPaths = [35]
// function Seek(map, location, end, prev = new Cord(0, 0), oldheight = 0) {
//     if (map[location.y] == undefined) return null;
//     if (map[location.y][location.x] == undefined) return null;
//     if (map[location.y][location.x] - 1 > oldheight) return null;
//     if (location.is(end)) return 0;
//     let seekMap = JSON.parse(JSON.stringify(map));
//     seekMap[location.y][location.x] = null;
//     // console.table(map);
//     for (const dir of dirs) {
//         if (!prev.isOpposite(dir)) {
//             let res = Seek(seekMap, location.add(dir), end, dir, map[location.y][location.x]);
//             if (res == null) continue;
//             if (Math.min(...foundPaths) < 1 + res) continue;
//             if (!location.is(new Cord(0, 0)))
//                 return 1 + res;
//             foundPaths.push(1 + parseInt(res))

//         }
//     }
// }

function neigbors(map, cord, visited) {
    var neigbors = [];
    for (const dir of dirs) {
        let next = cord.add(dir)
        if (map[next.y] == undefined) continue
        if (map[next.y][next.x] == undefined) continue
        if (visited.has(next.stringify())) continue;
        if (map[cord.y][cord.x] < map[next.y][next.x] - 1) continue;
        neigbors.push(next);
    }
    return neigbors;
}

function bfs(map, start, end) {
    let visited = new Set();
    let queue = neigbors(map, start, visited);
    queue.map(i => i.stringify()).forEach(i => visited.add(i));
    let i = 1;
    let found = false;
    while (!found) {
        i++;
        let tempQue = []
        while (queue.length != 0) {
            let next = queue.shift(1);
            let cords = neigbors(map, next, visited);
            if (cords == null) continue;
            if (cords.find(i => i.is(end))) found = true;
            tempQue.push(...cords)
            tempQue.map(i => i.stringify()).forEach(i => visited.add(i));
        }
        queue.push(...tempQue)
    }
    return i;
}



function PartOne({ map, start, end }) {
    return bfs(map, start, end);
    // return Math.min(...foundPaths);
}

function neigbors2(map, cord, visited) {
    var neigbors = [];
    for (const dir of dirs) {
        let next = cord.add(dir)
        if (map[next.y] == undefined) continue
        if (map[next.y][next.x] == undefined) continue
        if (visited.has(next.stringify())) continue;
        if (map[cord.y][cord.x] > map[next.y][next.x] + 1) continue;
        neigbors.push(next);
    }
    return neigbors;
}


function PartTwo({ map, end }) {
    let start = end;
    let visited = new Set();
    let queue = neigbors2(map, start, visited);
    queue.map(i => i.stringify()).forEach(i => visited.add(i));
    let i = 1;
    let found = false;
    while (!found) {
        i++;
        let tempQue = []
        while (queue.length != 0) {
            let next = queue.shift(1);
            let cords = neigbors2(map, next, visited);
            if (cords == null) continue;
            if (cords.find(i => map[i.y][i.x] == 0)) found = true;
            tempQue.push(...cords)
            tempQue.map(i => i.stringify()).forEach(i => visited.add(i));
        }
        queue.push(...tempQue)
    }
    return i;
}

// TESTS
let testInput = Parser("test.txt");
utils.test("Test 1", PartOne(testInput), 31);
testInput = Parser("test.txt", true);
utils.test("Test 2", PartTwo(testInput), 29);

// ANSWER
let input = Parser("input.txt");
console.log("Part 1 solution: " + PartOne(input)); // 481
input = Parser("input.txt");
console.log("Part 2 solution: " + PartTwo(input)); // 480