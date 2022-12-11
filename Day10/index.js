const utils = require('../utils');

class CPU {
    x = 1;
    cycles = 0;
    signalStregth = 0

    addx(num) {
        this.incrementCycle(1);
        this.incrementCycle(1);
        this.x += parseInt(num);
    }

    noop() {
        this.incrementCycle(1);
    }

    incrementCycle(times) {
        for (let i = 0; i < times; i++) {
            this.draw();
            this.cycles++;
            this.calculateSignalStregth();
        }
    }

    draw() {
        var row = this.cycles % 40;
        if (row == 0) process.stdout.write("\n");
        if (this.x - 1 == row) process.stdout.write("█");
        else if (this.x == row) process.stdout.write("█");
        else if (this.x + 1 == row) process.stdout.write("█");
        else process.stdout.write(" ");
    }

    calculateSignalStregth() {
        if (this.cycles == 20)
            this.signalStregth += this.cycles * this.x;
        if (this.cycles == 60)
            this.signalStregth += this.cycles * this.x;
        if (this.cycles == 100)
            this.signalStregth += this.cycles * this.x;
        if (this.cycles == 140)
            this.signalStregth += this.cycles * this.x;
        if (this.cycles == 180)
            this.signalStregth += this.cycles * this.x;
        if (this.cycles == 220)
            this.signalStregth += this.cycles * this.x;
    }
}

function Parser(file) {
    return utils.read(file).split('\n').map(i => i.split(' '));
}

function PartOne(ops) {
    let cpu = new CPU();
    for (const op of ops) {
        switch (op[0]) {
            case "addx":
                cpu.addx(op[1]);
                break;
            case "noop":
                cpu.noop();
                break;
        }
    }
    console.log();
    return cpu.signalStregth;
}

// TESTS
let testInput = Parser("test.txt");
utils.test("Test 1+2", PartOne(testInput), 13140);

// ANSWER
let input = Parser("input.txt");
console.log("Part 1+2 solution: " + PartOne(input)); //15360 + PHLHJGZA
