use common::{self, AOCInput};
const DAY: &str = env!("CARGO_PKG_NAME");

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    AOCInput::test("").solve(task1).check(1);

    // Solution
    let ans = AOCInput::input(DAY).solve(task1).unwrap();
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test
    AOCInput::test("").solve(task2).check(1);

    // Solution
    let ans = AOCInput::input(DAY).solve(task2).unwrap();
    println!("Task 1 solution: {ans}");
}

fn task1(input: Vec<String>) -> i32 {
    0
}

fn task2(input: Vec<String>) -> i32 {
    0
}
