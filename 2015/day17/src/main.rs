use std::{
    collections::{HashMap, HashSet},
    vec,
};

use common;
const INPUT_FILE: &str = "input/day17.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    assert_eq!(
        task1(vec![20, 15, 10, 5, 5], 25, 0, 0, &mut HashMap::new()).round(),
        4f64
    );

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input: Vec<u8> = input.iter().map(|f| f.parse().unwrap()).collect();

    let ans = task1(input, 150, 0, 0, &mut HashMap::new()).round();
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test
    assert_eq!(lowest(vec![20, 15, 10, 5, 5], 25, 0, 0, &mut u8::MAX), 2);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input: Vec<u8> = input.iter().map(|f| f.parse().unwrap()).collect();

    let ans = task2(input);
    println!("Task 2 solution: {ans}");
}

fn task1(
    buckets: Vec<u8>,
    target: u8,
    starting: u8,
    depth: i8,
    cache: &mut HashMap<Vec<u8>, f64>,
) -> f64 {
    if cache.contains_key(&buckets) {
        return cache[&buckets];
    }
    if buckets.len() == 0 {
        return 0f64;
    }
    if starting > target {
        cache.insert(buckets, 0f64);
        return 0f64;
    }
    if starting == target {
        return 1f64 / factorial(depth as u64) as f64;
    }
    let mut sum: f64 = 0f64;
    for (i, b) in buckets.iter().enumerate() {
        let mut new = buckets.clone();
        new.remove(i);
        sum += task1(new, target, starting + b, depth + 1, cache);
    }
    cache.insert(buckets, sum);
    return sum;
}

fn task2(input: Vec<u8>) -> f64 {
    let min_depth = lowest(input.clone(), 150, 0, 0, &mut u8::MAX);
    find(input, 150, 0, 0, &mut HashMap::new(), min_depth).round()
}

fn lowest(buckets: Vec<u8>, target: u8, starting: u8, depth: u8, best: &mut u8) -> u8 {
    let best = best;
    if depth > *best {
        return u8::MAX;
    }
    if buckets.len() == 0 {
        return u8::MAX;
    }
    if starting > target {
        return u8::MAX;
    }
    if starting == target {
        *best = depth;
        return depth;
    }
    for (i, b) in buckets.iter().enumerate() {
        let mut new = buckets.clone();
        new.remove(i);
        lowest(new, target, starting + b, depth + 1, best);
    }
    return *best;
}

fn find(
    buckets: Vec<u8>,
    target: u8,
    starting: u8,
    depth: u8,
    cache: &mut HashMap<Vec<u8>, f64>,
    min_depth: u8,
) -> f64 {
    if depth > min_depth {
        return 0f64;
    }
    if cache.contains_key(&buckets) {
        return cache[&buckets];
    }
    if buckets.len() == 0 {
        return 0f64;
    }
    if starting > target {
        cache.insert(buckets, 0f64);
        return 0f64;
    }
    if starting == target {
        return 1f64 / factorial(depth as u64) as f64;
    }
    let mut sum: f64 = 0f64;
    for (i, b) in buckets.iter().enumerate() {
        let mut new = buckets.clone();
        new.remove(i);
        sum += find(new, target, starting + b, depth + 1, cache, min_depth);
    }
    cache.insert(buckets, sum);
    return sum;
}

fn factorial(num: u64) -> u64 {
    match num {
        0 => 1,
        1 => 1,
        _ => factorial(num - 1) * num,
    }
}
