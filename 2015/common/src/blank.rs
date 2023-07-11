use common;
const INPUT_FILE: &str = "input/dayXX.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    assert_eq!(task1(), ());

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input: String = input.first().unwrap().to_string();

    let ans = task1(input);
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test
    assert_eq!(task2(), ());

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input: String = input.first().unwrap().to_string();

    let ans = task2(input);
    println!("Task 2 solution: {ans}");
}

fn task1(input: String) -> i32 {}

fn task2(input: String) -> i32 {}
