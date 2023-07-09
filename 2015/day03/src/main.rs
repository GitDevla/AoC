use common;
use std::collections::HashSet;

fn main() {
    assert_eq!(task1(&String::from(">")), 2);
    assert_eq!(task1(&String::from("^>v<")), 4);
    assert_eq!(task1(&String::from("^v^v^v^v^v")), 2);

    let file = common::read_file("input/day03.txt");
    let ans = task1(file.first().unwrap());
    println!("Task 1: {ans}");

    assert_eq!(task2(&String::from("^v")), 3);
    assert_eq!(task2(&String::from("^>v<")), 3);
    assert_eq!(task2(&String::from("^v^v^v^v^v")), 11);

    let ans = task2(file.first().unwrap());
    println!("Task 1: {ans}");
}

fn task1(moves: &String) -> usize {
    let mut houses = HashSet::new();
    houses.insert((0, 0));
    let mut cord = (0, 0);
    for step in moves.chars() {
        _ = match step {
            '^' => cord.1 += 1,
            'v' => cord.1 -= 1,
            '>' => cord.0 += 1,
            '<' => cord.0 -= 1,
            _ => (),
        };
        houses.insert(cord);
    }
    return houses.len();
}

fn task2(moves: &String) -> usize {
    let mut houses = HashSet::new();
    houses.insert((0, 0));
    let mut drunk = (0, 0);
    let mut robo = (0, 0);
    for (i, step) in moves.chars().into_iter().enumerate() {
        if i % 2 == 0 {
            _ = match step {
                '^' => drunk.1 += 1,
                'v' => drunk.1 -= 1,
                '>' => drunk.0 += 1,
                '<' => drunk.0 -= 1,
                _ => (),
            };
            houses.insert(drunk);
        } else {
            _ = match step {
                '^' => robo.1 += 1,
                'v' => robo.1 -= 1,
                '>' => robo.0 += 1,
                '<' => robo.0 -= 1,
                _ => (),
            };
            houses.insert(robo);
        }
    }
    return houses.len();
}
