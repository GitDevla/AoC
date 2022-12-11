const utils = require('../utils');

class Monkey {
    static Monkeys = [];
    inspectedTimes = 0;

    constructor(items, operation, test, iftrue, iffalse) {
        this.items = items;
        this.operation = operation;
        this.test = test;
        this.iftrue = iftrue;
        this.iffalse = iffalse;
    }

    inspectAll(amIACoward = false) {
        while (this.items.length > 0) {
            this.inspect(amIACoward);
        }
    }

    inspect(amIACoward) {
        this.inspectedTimes++;
        let item = this.items.shift();
        item = this.operation(item);
        if (!amIACoward)
            item = Math.floor(item / 3);

        this.throw(item);
    }

    throw(item) {
        if (item % this.test == 0)
            this.throwToMonkey(this.iftrue, item);
        else
            this.throwToMonkey(this.iffalse, item);
    }

    throwToMonkey(index, item) {
        Monkey.Monkeys[index].catch(item);
    }

    catch(item) {
        this.items.push(item % Monkey.fuckBigInt);
    }
}

function Parser(file) {
    let DataMonkey = utils.read(file).split('\n\n');
    let monkeys = [];
    for (const data of DataMonkey) {
        let lines = data.split("\n");
        let items = lines[1].split(":")[1].split(",").map(i => parseInt(i));
        let operations = lines[2].split(" ").splice(-2);
        let operationSign = operations[0];
        let operationNum = operations[1];
        let operation = (num) => {
            return eval(`${num} ${operationSign} ${operationNum == "old" ? num : operationNum} `)
        }
        let testNum = parseInt(lines[3].split(" ").at(-1));
        let ifTure = parseInt(lines[4].split(" ").at(-1));
        let ifFalse = parseInt(lines[5].split(" ").at(-1));
        monkeys.push(new Monkey(items, operation, testNum, ifTure, ifFalse));
    }
    return monkeys;
}

function Task(monkeys, amIACoward, times) {
    Monkey.fuckBigInt = monkeys.map(monkey => monkey.test).reduce((a, x) => a * x); // I dont know what kind of dark magic is this 
    Monkey.Monkeys = monkeys;
    for (let i = 0; i < times; i++) {
        for (const monkey of Monkey.Monkeys)
            monkey.inspectAll(amIACoward);
    }
    let top2 = Monkey.Monkeys.sort((a, b) => b.inspectedTimes - a.inspectedTimes).splice(0, 2);
    return top2[0].inspectedTimes * top2[1].inspectedTimes;
}

function PartOne(monkeys) {
    return Task(monkeys, false, 20);
}

function PartTwo(monkeys) {
    return Task(monkeys, true, 10000);
}

// TESTS
let testInput = Parser("test.txt", false);
utils.test("Test 1", PartOne(testInput), 10605);
testInput = Parser("test.txt", true);
utils.test("Test 2", PartTwo(testInput), 2713310158);

// ANSWER
let input = Parser("input.txt");
console.log("Part 1 solution: " + PartOne(input)); // 121450
input = Parser("input.txt");
console.log("Part 2 solution: " + PartTwo(input)); // 28244037010