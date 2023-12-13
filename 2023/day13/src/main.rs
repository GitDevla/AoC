use std::ops::Sub;

use common::{self, AOCInput};
const DAY: &str = env!("CARGO_PKG_NAME");

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    AOCInput::test(
        r#"#...##..#
        #....#..#
        ..##..###
        #####.##.
        #####.##.
        ..##..###
        #....#..#

        #.##..##.
        ..#.##.#.
        ##......#
        ##......#
        ..#.##.#.
        ..##..##.
        #.#.##.#."#,
    )
    .convert(parse)
    .solve(task1)
    .check(405);

    // Solution
    let ans = AOCInput::input(DAY).convert(parse).solve(task1).unwrap();
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test
    AOCInput::test(
        r#"#...##..#
        #....#..#
        ..##..###
        #####.##.
        #####.##.
        ..##..###
        #....#..#

        #.##..##.
        ..#.##.#.
        ##......#
        ##......#
        ..#.##.#.
        ..##..##.
        #.#.##.#."#,
    )
    .convert(parse)
    .solve(task2)
    .check(400);

    // Solution
    let ans = AOCInput::input(DAY).convert(parse).solve(task2).unwrap();
    println!("Task 2 solution: {ans}");
}

fn task1(input: Vec<Vec<Vec<bool>>>) -> i32 {
    let mut sum = 0;
    for x in input {
        let (idx, vertical) = mirroring(&x).unwrap();
        if vertical {
            sum += idx;
        } else {
            sum += idx * 100;
        }
    }
    sum
}

fn task2(input: Vec<Vec<Vec<bool>>>) -> i32 {
    0
}

fn mirroring(input: &Vec<Vec<bool>>) -> Option<(i32, bool)> {
    let horizontal = find_mirror(&input);
    if horizontal.is_some() {
        return Some((horizontal.unwrap(), false));
    }
    let rotated = rotate(&input);
    let vertical = find_mirror(&rotated);
    if vertical.is_none() {
        return None;
    }
    return Some((vertical.unwrap(), true));
}

fn find_mirror(input: &Vec<Vec<bool>>) -> Option<i32> {
    let rows = find_possible_mirrors(input);
    for row in rows {
        let idx = row as usize;
        let mut offset = 0;
        loop {
            let left = input.get(idx.overflowing_sub(offset).0);
            let right = input.get(idx + offset + 1);
            if left.is_none() || right.is_none() {
                return Some(idx as i32 + 1);
            }
            if left.unwrap() != right.unwrap() {
                break;
            }
            offset += 1;
        }
    }
    None
}

fn find_possible_mirrors(input: &Vec<Vec<bool>>) -> Vec<i32> {
    let mut rows = vec![];
    let mut peek = input.iter().peekable();
    let original_len = peek.len();
    while let Some(line) = peek.next() {
        if let Some(next) = peek.peek() {
            if line == *next {
                rows.push((original_len - peek.len()) as i32 - 1)
            }
        }
    }
    return rows;
}

fn rotate(input: &Vec<Vec<bool>>) -> Vec<Vec<bool>> {
    let mut ans = vec![];
    for i in 0..input[0].len() {
        let new = input.iter().map(|line| line[i]).collect();
        ans.push(new);
    }

    ans
}

fn parse(input: Vec<String>) -> Vec<Vec<Vec<bool>>> {
    let mut maps = vec![];
    let mut curr = vec![];
    for x in input {
        if x == "" {
            maps.push(curr);
            curr = vec![];
            continue;
        }
        curr.push(x.chars().map(|c| c == '#').collect());
    }
    maps.push(curr);

    maps
}
