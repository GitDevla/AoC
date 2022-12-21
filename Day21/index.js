const utils = require('../utils');

function Parser(file) {
    let data = utils.read(file).split('\n');
    let monkeys = [];
    for (const line of data) {
        let [name, other] = line.split(":");
        other = other.trim().split(" ");
        let num = parseInt(other[0])
        if (!isNaN(num))
            monkeys.push(new Monkey(name, num, null));
        else
            monkeys.push(new Monkey(name, null, other));
    }
    for (const monkey of monkeys) {
        if (monkey.operation == null) continue;
        let leftName = monkey.operation[0];
        let rightName = monkey.operation[2];
        let left = monkeys.find(i => i.name == leftName);
        let right = monkeys.find(i => i.name == rightName);
        monkey.operation[0] = left;
        monkey.operation[2] = right;
    }
    return monkeys.find(i => i.name == "root")
}

class Monkey {
    name;
    operation;
    value;
    constructor(name, value, operation) {
        this.name = name;
        this.value = value;
        this.operation = operation;
    }

    getValue() {
        if (this.value != null) return this.value;
        let leftValue = this.operation[0].getValue();
        let rightValue = this.operation[2].getValue();
        if (this.operation[1] == "=") return this.isEqual(leftValue, rightValue);
        return eval(`leftValue ${this.operation[1]} rightValue`);
    }

    isEqual(leftValue, rightValue) {
        return [leftValue, rightValue];
    }
}


function PartOne(root) {
    return root.getValue();
}

function find(root, name) {
    if (root.name == name) return root;
    if (root.value != null) return;
    let left = find(root.operation[0], name);
    if (left != undefined) return left;
    let right = find(root.operation[2], name);
    return right;
}

function PartTwo(root) {
    root.operation[1] = "=";
    let human = find(root, "humn");

    // Bruteforce
    let lowest = 0;
    let highest = 999999999999999;
    for (let i = 0; i < 1000; i++) {
        let mid = Math.round((highest + lowest) / 2);
        human.value = mid;
        let last = root.getValue();
        if (last[0] < last[1]) lowest = mid;
        if (last[0] > last[1]) highest = mid;
        if (last[0] == last[1]) return mid;
        if (lowest == highest) break;
    }
    lowest = 0;
    highest = 999999999999999;
    for (let i = 0; i < 1000; i++) {
        let mid = Math.round((highest + lowest) / 2);
        human.value = mid;
        let last = root.getValue();
        if (last[0] < last[1]) highest = mid;
        if (last[0] > last[1]) lowest = mid;
        if (last[0] == last[1]) return mid;
        if (lowest == highest) break;
    }

    return;

}

// TESTS
let testInput = Parser("test.txt");
utils.test("Test 1", PartOne(testInput), 152);
testInput = Parser("test.txt");
utils.test("Test 2", PartTwo(testInput), 301);

// ANSWER
let input = Parser("input.txt");
console.log("Part 1 solution: " + PartOne(input)); // 104272990112064
input = Parser("input.txt");
console.log("Part 2 solution: " + PartTwo(input)); // 