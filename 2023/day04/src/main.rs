use std::collections::HashSet;

use common;
const INPUT_FILE: &str = "input/day04.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    let test_input = r#"Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"#;
    let test_input: Vec<String> = test_input.lines().map(String::from).collect();
    assert_eq!(task1(test_input), 13);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);

    let ans = task1(input);
    assert_eq!(ans, 22193);
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test
    let test_input = r#"Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"#;
    let test_input: Vec<String> = test_input.lines().map(String::from).collect();
    assert_eq!(task2(test_input), 30);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);

    let ans = task2(input);
    assert_eq!(ans, 5625994);
    println!("Task 2 solution: {ans}");
}

fn task1(input: Vec<String>) -> i32 {
    input
        .iter()
        .map(|f| calc_score(union_count(f.to_string())))
        .sum()
}

fn task2(input: Vec<String>) -> i32 {
    let mut scores: Vec<(i32, i32)> = input
        .iter()
        .map(|f| (union_count(f.to_string()), 1))
        .collect();
    let mut idx = 0;
    while idx < scores.len() {
        let (score, instances) = scores[idx];
        for x in 0..score {
            scores
                .get_mut(idx + (x + 1) as usize)
                .and_then(|f| Some(f.1 += instances));
        }
        idx += 1;
    }

    return scores.iter().map(|f| f.1).sum();
}

fn union_count(input: String) -> i32 {
    // Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    let numbers: Vec<i32> = input
        .split(":")
        .nth(1)
        .unwrap()
        .split("|")
        .flat_map(|f| f.split_whitespace())
        .map(|f| f.trim().parse::<i32>().unwrap())
        .collect();
    let original_len = numbers.len();
    let union_numbers = numbers.iter().cloned().collect::<HashSet<i32>>();
    let union_len = union_numbers.len();
    let points = (original_len - union_len) as i32;
    return points;
}

fn calc_score(i: i32) -> i32 {
    return if i == 0 { 0 } else { 2_i32.pow((i - 1) as u32) };
}
