use common::{self, AOCInput};
const DAY: &str = env!("CARGO_PKG_NAME");
fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    AOCInput::test(
        r#"0 3 6 9 12 15
        1 3 6 10 15 21
        10 13 16 21 30 45"#,
    )
    .convert(parse)
    .solve(task1)
    .check(114);

    // Solution
    let ans = AOCInput::input(DAY).convert(parse).solve(task1).unwrap();
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test
    AOCInput::test(
        r#"0 3 6 9 12 15
        1 3 6 10 15 21
        10 13 16 21 30 45"#,
    )
    .convert(parse)
    .solve(task2)
    .check(2);

    // Solution
    let ans = AOCInput::input(DAY).convert(parse).solve(task2).unwrap();
    println!("Task 2 solution: {ans}");
}

fn extrapolate(input: &Vec<i32>) -> i32 {
    if input.iter().all(|f| *f == 0) {
        return 0;
    }
    let mut next = vec![];
    for (idx, x) in input[..input.len() - 1].iter().enumerate() {
        next.push(input[idx + 1] - x);
    }
    return input[input.len() - 1] + extrapolate(&next);
}

fn task1(input: Vec<Vec<i32>>) -> i32 {
    solve(input, false)
}

fn task2(input: Vec<Vec<i32>>) -> i32 {
    solve(input, true)
}

fn solve(input: Vec<Vec<i32>>, beninging: bool) -> i32 {
    if beninging {
        return input
            .iter()
            .map(|f| f.iter().rev().cloned().collect::<Vec<i32>>())
            .map(|f| extrapolate(&f))
            .sum();
    }
    return input.iter().map(extrapolate).sum();
}

fn parse(input: Vec<String>) -> Vec<Vec<i32>> {
    let mut res = vec![];
    for x in input {
        let x: Vec<i32> = x.split(" ").map(|s| s.parse::<i32>().unwrap()).collect();
        res.push(x);
    }
    return res;
}
