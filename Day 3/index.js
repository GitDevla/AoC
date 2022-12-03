function task(input) {
    var list = input.split('\n');
    var sum = 0;
    list.forEach(i => {
        var half = i.length / 2;
        var firstCompartment = i.slice(0, half);
        var secondCompartment = i.slice(half);
        var double = findDupli(firstCompartment, secondCompartment);
        sum += getPriority(double);
    })
    return sum;
}

function findDupli(first, second) {
    var letters = [];
    for (const letter of first) {
        letters[letter] = true;
    }
    for (const letter of second) {
        if (letters[letter]) return letter;
    }
    return null;
}

function getPriority(letter) {
    if (letter == letter.toLowerCase())
        return letter.charCodeAt() - "a".charCodeAt() + 1;
    if (letter == letter.toUpperCase())
        return letter.charCodeAt() - "A".charCodeAt() + 27;
}

var test = `vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw`;
console.log(task(test) == 157);

function task2(input) {
    var list = input.split('\n');
    var teams = sliceIntoChunks(list, 3);
    var sum = 0;
    teams.forEach(i => {
        var first = i[0];
        var second = i[1];
        var third = i[2];
        var badge = findTripl(first, second, third);
        if (badge == null) debugger;
        sum += getPriority(badge);
    })
    return sum;
}

function sliceIntoChunks(arr, chunkSize) {
    const res = [];
    for (let i = 0; i < arr.length; i += chunkSize) {
        const chunk = arr.slice(i, i + chunkSize);
        res.push(chunk);
    }
    return res;
}

function findTripl(first, second, third) {
    var letters = [];
    for (const letter of first) {
        if (letters[letter]) letters[letter].add(1);
        else letters[letter] = new Set([1]);
    }
    for (const letter of second) {
        if (letters[letter]) letters[letter].add(2);
        else letters[letter] = new Set([2]);
    }
    for (const letter of third) {
        if (letters[letter]) letters[letter].add(3);
        else letters[letter] = new Set([3]);
    }
    for (const i in letters) {
        if (Object.hasOwnProperty.call(letters, i)) {
            const element = letters[i];
            if (element.size == 3) return i;
        }
    }
    return null;
}
console.log(task2(test) == 70);