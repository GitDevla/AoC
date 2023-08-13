use std::collections::HashSet;

use common;
use itertools::Itertools;
const INPUT_FILE: &str = "input/day24.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    assert_eq!(task1(vec![1, 2, 3, 4, 5, 7, 8, 9, 10, 11]), 99);

    // Solution
    let input: Vec<i32> = common::read_file(INPUT_FILE)
        .iter()
        .map(|s| s.parse::<i32>().unwrap())
        .collect();

    let ans = task1(input);
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test
    assert_eq!(task2(vec![1, 2, 3, 4, 5, 7, 8, 9, 10, 11]), 44);

    // Solution
    let input: Vec<i32> = common::read_file(INPUT_FILE)
        .iter()
        .map(|s| s.parse::<i32>().unwrap())
        .collect();

    let ans = task2(input);
    println!("Task 2 solution: {ans}");
}

fn task1(input: Vec<i32>) -> u64 {
    let target: i32 = input.iter().sum::<i32>() / 3;
    let all_combinations = find_combinations!(&input, target);
    let lightest_fronts = all_combinations
        .iter()
        .min_set_by(|a, b| a.len().cmp(&b.len()));

    let mut products = vec![];
    for a in lightest_fronts {
        let without_front = all_combinations
            .iter()
            .filter(|f| f.iter().any(|n| !a.contains(n)));
        'outer: for b in without_front.clone() {
            for c in without_front.clone() {
                if b.iter().any(|n| c.contains(n)) {
                    continue;
                }

                products.push(a.iter().fold(1_u64, |acc, e| acc * *e as u64));
                break 'outer;
            }
        }
    }
    *products.iter().min().unwrap()
}

fn task2(input: Vec<i32>) -> u64 {
    let target: i32 = input.iter().sum::<i32>() / 4;
    let all_combinations = find_combinations!(&input, target);
    let lightest_fronts = all_combinations
        .iter()
        .min_set_by(|a, b| a.len().cmp(&b.len()));

    let mut products = vec![];
    for a in lightest_fronts {
        let without_front = all_combinations
            .iter()
            .filter(|f| f.iter().any(|n| !a.contains(n)));
        'outer: for b in without_front.clone() {
            for c in without_front.clone() {
                for d in without_front.clone() {
                    if b.iter().any(|n| !c.contains(n) && !d.contains(n)) {
                        continue;
                    }

                    products.push(a.iter().fold(1_u64, |acc, e| acc * *e as u64));
                    break 'outer;
                }
            }
        }
    }
    *products.iter().min().unwrap()
}

#[macro_export]
macro_rules! find_combinations {
    ($nums:expr,$target:expr) => {{
        let mut all_combinations: HashSet<Vec<i32>> = HashSet::new();
        find_combinations($nums, $target, 0, &mut all_combinations, vec![]);
        all_combinations
    }};
}

fn find_combinations(
    all_nums: &Vec<i32>,
    remaining: i32,
    start_idx: usize,
    found: &mut HashSet<Vec<i32>>,
    current_nums: Vec<i32>,
) {
    if remaining == 0 {
        found.insert(current_nums);
        return;
    }

    for i in start_idx..all_nums.len() {
        let n = all_nums[i];
        if n > remaining {
            continue;
        }
        if current_nums.contains(&n) {
            continue;
        }
        let mut temp = current_nums.clone();
        temp.push(n);
        find_combinations(all_nums, remaining - n, i, found, temp);
    }
}
