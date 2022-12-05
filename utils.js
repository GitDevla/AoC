const path = require('path');
const fs = require('fs');

exports.test = (text, result, expected) => {
    if (result == expected) {
        console.error(`\x1b[32m${text}: SUCCESS \x1b[0m`);
    } else {
        console.error(`\x1b[31m${text}: FAIL\nResult: ${result}\nExpected: ${expected}\x1b[0m`);
    }
}

exports.read = path => fs.readFileSync(path, 'utf-8');

exports.sum = (arr) => arr.reduce((a, b) => parseInt(a) + parseInt(b))
