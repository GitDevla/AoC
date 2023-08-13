use std::collections::HashMap;

use common::{self, benchmark};
const INPUT_FILE: &str = "input/day07.txt";

fn main() {
    benchmark(|| {
        pt1();
        pt2();
    })
}

fn pt1() {
    // Test
    let test = r#"123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> a
NOT y -> i"#;
    let test = parse(test.lines().map(String::from).collect());
    assert_eq!(task1(test), 65412);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input = parse(input);

    let ans = task1(input);
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input = parse(input);

    let ans = task2(input);
    println!("Task 2 solution: {ans}");
}

fn task1(input: HashMap<String, String>) -> u16 {
    let mut cache = HashMap::new();
    backtrack("a", &input, &mut cache)
}

fn task2(input: HashMap<String, String>) -> u16 {
    let a = task1(input.clone());

    let mut input = input.clone();
    input.insert("b".to_string(), a.to_string());
    task1(input)
}

fn backtrack(
    letter: &str,
    plugs: &HashMap<String, String>,
    cache: &mut HashMap<String, u16>,
) -> u16 {
    let current_cmd = &plugs[letter];
    if cache.contains_key(letter) {
        return cache[letter];
    }
    let split: Vec<_> = current_cmd.split(" ").collect();
    let res = match split.len() {
        3 => {
            let left = num_or_backtrack(split[0], plugs, cache);
            let right = num_or_backtrack(split[2], plugs, cache);
            match split[1] {
                "AND" => left & right,
                "OR" => left | right,
                "LSHIFT" => left << right,
                "RSHIFT" => left >> right,
                _ => panic!("xd"),
            }
        }
        2 => !num_or_backtrack(split[1], plugs, cache), // NOT
        1 => num_or_backtrack(split[0], plugs, cache),
        _ => panic!("xd"),
    };
    cache.insert(letter.to_string(), res);
    return res;
}

fn parse(input: Vec<String>) -> HashMap<String, String> {
    let mut plugs: HashMap<String, String> = HashMap::new();
    for line in input {
        let split: Vec<_> = line.split(" -> ").collect();
        plugs.insert(split[1].to_string(), split[0].to_string());
    }
    return plugs;
}

fn num_or_backtrack(
    letter: &str,
    plugs: &HashMap<String, String>,
    cache: &mut HashMap<String, u16>,
) -> u16 {
    return match letter.parse::<u16>() {
        Ok(x) => x,
        Err(_) => backtrack(letter, plugs, cache),
    };
}
