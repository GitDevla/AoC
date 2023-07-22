use std::collections::{HashMap, HashSet};

use common;

const INPUT_FILE: &str = "input/day19.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    let test = r#"H => HO
H => OH
O => HH
    
HOH"#;
    let test: Vec<String> = test.lines().map(String::from).collect();
    let test = parse(test);
    assert_eq!(task1(&test.0, &test.1).len(), 4);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input = parse(input);

    let ans = task1(&input.0, &input.1).len();
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test
    let test = r#"H => HO
H => OH
O => HH
e => H
e => O
    
HOH"#;
    let test: Vec<String> = test.lines().map(String::from).collect();
    let test = parse(test);
    assert_eq!(task2(&test.0, &test.1), 3);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input = parse(input);

    let ans = task2(&input.0, &input.1);
    println!("Task 2 solution: {ans}");
}

fn task1(dna: &String, replacements: &HashMap<String, Vec<String>>) -> Vec<String> {
    let mut variations = HashSet::new();
    for (key, value) in replacements {
        let found: Vec<_> = dna.match_indices(key).collect();
        for (starting_index, _) in found {
            for replacement in value.iter() {
                let clone = dna.clone();
                let length = key.len();
                let start = &clone[..starting_index];
                let end = &clone[starting_index + length..];
                let new = format!("{}{}{}", start, replacement, end);
                variations.insert(new);
            }
        }
    }
    return variations.into_iter().collect();
}

// this is peak rust code right here
// race condition causes the code to randomly fail 70% of the time
// and checking every possible state causes time/memory complexity to sky rocket
// so Nuh uh
fn task2(dna: &String, replacements: &HashMap<String, Vec<String>>) -> usize {
    let mut clone = dna.clone();
    let mut depth = 0_usize;

    while clone != "e" {
        'outer: for (key, value) in replacements {
            for replacement in value.iter() {
                if clone.contains(replacement) {
                    clone = clone.replacen(replacement, key, 1);
                    break 'outer;
                }
            }
        }
        depth += 1;

        if depth > 10000 {
            return 0;
        }
    }

    return depth;
}

fn parse(input: Vec<String>) -> (String, HashMap<String, Vec<String>>) {
    let length = input.len();
    let dna: String = input[length - 1].to_string();
    let mut replacements: HashMap<String, Vec<String>> = HashMap::new();

    for l in input[..input.len() - 2].iter() {
        let split: Vec<&str> = l.split(" => ").collect();
        let char = split[0].to_string();
        let encode = split[1].to_string();
        let inst = replacements.entry(char).or_insert(vec![]);
        inst.push(encode);
    }
    return (dna, replacements);
}
