// --- Day 1: Calorie Counting ---
function calorie(input) {
    var list = input.split('\n');
    let mostCal = 0;
    let currentCal = 0;
    list.forEach(i => {
        if (!i) {
            if (mostCal < currentCal) mostCal = currentCal;
            currentCal = 0;
        }
        else currentCal += parseInt(i);
    });
    if (mostCal < currentCal) mostCal = currentCal;
    return mostCal;
}

// --- Part Two ---

function calorieSum(input) {
    var list = input.split('\n');
    let currentCal = 0;
    let sums = [];
    list.forEach(i => {
        if (!i) {
            sums.push(parseInt(currentCal));
            currentCal = 0;
        }
        else currentCal += parseInt(i);
    });
    sums.push(parseInt(currentCal));
    let sorted = sums.sort((a, b) => b - a);
    let sum = 0;

    for (const value of sorted.splice(0, 3)) {
        sum += value;
    }
    return sum;
}   
