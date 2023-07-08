use common;
use std::cmp::max;

fn line_parse(s: &String) -> Vec<i32> {
    let parts: Vec<i32> = s.split("x").map(|a| a.parse().unwrap()).collect();
    return parts;
}

fn main() {
    // Puzzle 1 tests
    assert_eq!(task1(line_parse(&String::from("2x3x4"))), 58);
    assert_eq!(task1(line_parse(&String::from("1x1x10"))), 43);

    // Puzzle 1 solution
    let file = common::read_file("input/day02.txt");

    let mut sum = 0;
    for line in &file {
        let ans = task1(line_parse(line));
        sum += ans;
    }
    println!("{sum}");

    // Puzzle 2 tests
    assert_eq!(task2(line_parse(&String::from("2x3x4"))), 34);
    assert_eq!(task2(line_parse(&String::from("1x1x10"))), 14);

    let mut sum = 0;
    for line in &file {
        let ans = task2(line_parse(line));
        sum += ans;
    }
    println!("{sum}");
}

fn task1(sides: Vec<i32>) -> i32 {
    let length = sides[0];
    let width = sides[1];
    let height = sides[2];

    let a: i32 = length * width;
    let b: i32 = width * height;
    let c: i32 = height * length;

    let values = [a, b, c];
    let smallest = values.iter().min().unwrap();
    let area: i32 = 2 * a + 2 * b + 2 * c;
    return smallest + area;
}

fn task2(sides: Vec<i32>) -> i32 {
    let length = sides[0];
    let width = sides[1];
    let height = sides[2];

    let volume = length * width * height;
    let max: i32 = max(length, max(width, height));
    let mut vec = Vec::from(sides);
    vec.remove(
        vec.iter()
            .position(|x| *x == max)
            .expect("needle not found"),
    );
    let mut ribbon = 0;
    for side in vec {
        ribbon += side * 2;
    }
    ribbon + volume
}
