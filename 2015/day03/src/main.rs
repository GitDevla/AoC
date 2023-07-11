use std::collections::HashSet;

use common;
const INPUT_FILE: &str = "input/day03.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    assert_eq!(task1(">".to_string()), 2);
    assert_eq!(task1("^>v<".to_string()), 4);
    assert_eq!(task1("^v^v^v^v^v".to_string()), 2);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input: String = input.first().unwrap().to_string();

    let ans = task1(input);
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test
    assert_eq!(task2("^v".to_string()), 3);
    assert_eq!(task2("^>v<".to_string()), 3);
    assert_eq!(task2("^v^v^v^v^v".to_string()), 11);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input: String = input.first().unwrap().to_string();

    let ans = task2(input);
    println!("Task 2 solution: {ans}");
}

fn task1(moves: String) -> usize {
    let house = visited_houses(moves);
    return house.len();
}

fn task2(moves: String) -> usize {
    let drunk_moves: String = moves.chars().step_by(2).collect();
    let robot_moves: String = moves.chars().skip(1).step_by(2).collect();
    let mut drunk_moves = visited_houses(drunk_moves);
    let robot_moves = visited_houses(robot_moves);
    drunk_moves.extend(&robot_moves);
    return drunk_moves.len();
}

fn visited_houses(moves: String) -> HashSet<(i32, i32)> {
    let mut houses: HashSet<(i32, i32)> = HashSet::from([(0, 0)]);
    let (mut x, mut y) = (0, 0);
    for step in moves.chars() {
        _ = match step {
            '^' => y += 1,
            'v' => y -= 1,
            '>' => x += 1,
            '<' => x -= 1,
            _ => (),
        };
        houses.insert((x, y));
    }
    return houses;
}
