use std::collections::HashMap;

use common;
const INPUT_FILE: &str = "input/day08.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    let test_input = r#"RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"#;
    let test_input: Vec<String> = test_input.split("\n").map(|s| s.to_string()).collect();
    let test_input = parse(test_input);
    assert_eq!(task1(test_input), 2);
    let test_input = r#"LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"#;
    let test_input: Vec<String> = test_input.split("\n").map(|s| s.to_string()).collect();
    let test_input = parse(test_input);
    assert_eq!(task1(test_input), 6);
    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input = parse(input);

    let ans = task1(input);
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test
    let test_input = r#"LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"#;
    let test_input: Vec<String> = test_input.split("\n").map(|s| s.to_string()).collect();
    let test_input = parse(test_input);
    assert_eq!(task2(test_input), 6);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input = parse(input);

    let ans = task2(input);
    println!("Task 2 solution: {ans}");
}

fn task1(input: (String, HashMap<String, (String, String)>)) -> i32 {
    let hashmap = input.1;
    let mut current_node = "AAA".to_string();
    for (idx, x) in input.0.chars().cycle().enumerate() {
        if current_node == "ZZZ" {
            return idx as i32;
        }
        let next = match x {
            'R' => &hashmap[&current_node].1,
            'L' => &hashmap[&current_node].0,
            _ => panic!("Invalid input"),
        };
        current_node = next.to_string();
    }
    return -1;
}

fn task2(input: (String, HashMap<String, (String, String)>)) -> u64 {
    let hashmap = input.1;
    let mut current_nodes: Vec<String> = hashmap
        .keys()
        .filter_map(|f| f.ends_with("A").then(|| f.to_string()))
        .collect();
    let mut loops = vec![];
    for n in current_nodes.iter_mut() {
        for (idx, x) in input.0.chars().cycle().enumerate() {
            if n.ends_with("Z") {
                loops.push(idx as u64);
                break;
            }
            let next = match x {
                'R' => &hashmap[n].1,
                'L' => &hashmap[n].0,
                _ => panic!("Invalid input"),
            };
            *n = next.to_string();
        }
    }
    return lcm_n(&loops);
}

fn lcm_n(array: &Vec<u64>) -> u64 {
    let mut result = array[0];
    for i in 1..array.len() {
        result = lcm(result, array[i]);
    }
    return result;
}

fn lcm(a: u64, b: u64) -> u64 {
    return a * b / gcd(a, b);
}

fn gcd(a: u64, b: u64) -> u64 {
    if b == 0 {
        return a;
    }
    return gcd(b, a % b);
}

fn parse(input: Vec<String>) -> (String, HashMap<String, (String, String)>) {
    let mut nodes: HashMap<String, (String, String)> = HashMap::new();
    for line in &input[2..] {
        let id = line.split_whitespace().nth(0).unwrap().to_string();
        let split: Vec<&str> = line
            .split("(")
            .nth(1)
            .unwrap()
            .trim_end_matches(")")
            .split(", ")
            .collect();
        let left = split.get(0).unwrap().to_string();
        let right = split.get(1).unwrap().to_string();

        nodes.insert(id, (left, right));
    }
    return (input[0].clone(), nodes);
}
