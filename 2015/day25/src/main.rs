use common;
use regex::Regex;
const INPUT_FILE: &str = "input/day25.txt";

fn main() {
    pt1();
}

fn pt1() {
    // Test
    assert_eq!(task1((1, 2)), 31916031);
    assert_eq!(task1((6, 6)), 27995004);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input: String = input.first().unwrap().to_string();
    let input = parse(input);
    let ans = task1(input);
    println!("Task 1 solution: {ans}");
}

fn task1(input: (i32, i32)) -> u64 {
    let mut times: u64 = 1;
    let mut y = 1;
    let mut x = 1;
    while !(x == input.0 && y == input.1) {
        if y == 1 {
            y = 1 + x;
            x = 1;
        } else {
            x += 1;
            y -= 1;
        }
        times += 1;
    }

    let mut prev: u64 = 20151125;
    let multiplier: u64 = 252533;
    let divider: u64 = 33554393;
    for _ in 0..times - 1 {
        prev = (prev * multiplier) % divider;
    }
    return prev;
}

fn parse(input: String) -> (i32, i32) {
    let regex = Regex::new(r"row (\d+), column (\d+)").unwrap();
    let caps = regex.captures(input.as_str()).unwrap();
    return (
        caps[2].parse::<i32>().unwrap(),
        caps[1].parse::<i32>().unwrap(),
    );
}
