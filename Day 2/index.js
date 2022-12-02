function rps(input) {
    var list = input.split('\n');
    var score = 0;
    list.forEach(i => {
        var [enemyPick, userPick] = i.split(' ');
        if (userPick == "X") score += 1;
        if (userPick == "Y") score += 2;
        if (userPick == "Z") score += 3;
        if ((userPick == "X" & enemyPick == "C")
            || (userPick == "Y" & enemyPick == "A")
            || (userPick == "Z" & enemyPick == "B"))
            score += 6;
        else if ((userPick == "X" & enemyPick == "A")
            || (userPick == "Y" & enemyPick == "B")
            || (userPick == "Z" & enemyPick == "C"))
            score += 3;

    });
    return score;
}

var ASD = [1, 2, 3];

function mod(n, m) {
    return ((n % m) + m) % m;
}

function rps2(input) {
    var list = input.split('\n');
    var score = 0;
    list.forEach(i => {
        var [enemyPick, userPick] = i.split(' ');
        if (userPick == "X") {
            score += ASD[mod((enemyPick.charCodeAt(0) - "A".charCodeAt(0) - 1), 3)];
        }
        if (userPick == "Y") {
            score += 3;
            score += ASD[(enemyPick.charCodeAt(0) - "A".charCodeAt(0)) % 3];
        }
        if (userPick == "Z") {
            score += 6;
            score += ASD[(enemyPick.charCodeAt(0) - "A".charCodeAt(0) + 1) % 3];
        }
        if (isNaN(score)) debugger;
    });
    return score;
}
