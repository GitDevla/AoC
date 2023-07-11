use common;
use std::cmp::max;
use std::cmp::min;
const INPUT_FILE: &str = "input/day02.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    assert_eq!(task1(line_parse("2x3x4".to_string())), 58);
    assert_eq!(task1(line_parse("1x1x10".to_string())), 43);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);

    let ans: i32 = input.iter().map(|f| task1(line_parse(f.to_string()))).sum();
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test
    assert_eq!(task2(line_parse("2x3x4".to_string())), 34);
    assert_eq!(task2(line_parse("1x1x10".to_string())), 14);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);

    let ans: i32 = input.iter().map(|f| task2(line_parse(f.to_string()))).sum();
    println!("Task 2 solution: {ans}");
}

fn task1(sides: Vec<i32>) -> i32 {
    let length = sides[0];
    let width = sides[1];
    let height = sides[2];

    let a: i32 = length * width;
    let b: i32 = width * height;
    let c: i32 = height * length;

    let smallest = min(a, min(b, c));
    let area: i32 = 2 * a + 2 * b + 2 * c;
    return smallest + area;
}

fn task2(sides: Vec<i32>) -> i32 {
    let length = sides[0];
    let width = sides[1];
    let height = sides[2];

    let volume = length * width * height;

    let max: i32 = max(length, max(width, height));
    let mut vec = sides.clone();
    vec.remove(vec.iter().position(|x| *x == max).unwrap());
    let ribbon: i32 = vec.iter().map(|a| a * 2).sum();
    return ribbon + volume;
}

fn line_parse(s: String) -> Vec<i32> {
    let parts: Vec<i32> = s.split("x").map(|a| a.parse().unwrap()).collect();
    return parts;
}
