use std::collections::HashMap;

use common;
const INPUT_FILE: &str = "input/day16.txt";
fn main() {
    pt1();
    pt2();
}

fn pt1() {
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

fn task1(input: Vec<Sue>) -> i16 {
    let mut ownings = HashMap::new();
    ownings.insert("children".to_string(), 3);
    ownings.insert("cats".to_string(), 7);
    ownings.insert("samoyeds".to_string(), 2);
    ownings.insert("pomeranians".to_string(), 3);
    ownings.insert("akitas".to_string(), 0);
    ownings.insert("vizslas".to_string(), 0);
    ownings.insert("goldfish".to_string(), 5);
    ownings.insert("trees".to_string(), 3);
    ownings.insert("cars".to_string(), 2);
    ownings.insert("perfumes".to_string(), 1);
    let ma = Sue {
        number: -1,
        ownings,
    };
    let found = input.iter().find(|s| s.is_like(&ma)).unwrap();
    return found.number;
}

fn task2(input: Vec<Sue>) -> i16 {
    let mut ownings = HashMap::new();
    ownings.insert("children".to_string(), 3);
    ownings.insert("cats".to_string(), 7);
    ownings.insert("samoyeds".to_string(), 2);
    ownings.insert("pomeranians".to_string(), 3);
    ownings.insert("akitas".to_string(), 0);
    ownings.insert("vizslas".to_string(), 0);
    ownings.insert("goldfish".to_string(), 5);
    ownings.insert("trees".to_string(), 3);
    ownings.insert("cars".to_string(), 2);
    ownings.insert("perfumes".to_string(), 1);
    let ma = Sue {
        number: -1,
        ownings,
    };
    let found = input
        .iter()
        .find(|s| s.i_dunno_what_to_call_this(&ma))
        .unwrap();
    return found.number;
}

fn parse(input: Vec<String>) -> Vec<Sue> {
    let mut sues = vec![];
    for l in input.iter() {
        let split: Vec<&str> = l.split(": ").collect();
        let name_split: Vec<&str> = split[0].split(" ").collect();
        let ownings_split = &split[1..].join(": ");
        let number = name_split[1].parse::<i16>().unwrap();
        let ownings = ownings_split
            .split(", ")
            .map(|f| f.split(": ").collect::<Vec<&str>>())
            .collect::<Vec<Vec<&str>>>();

        let mut hm: HashMap<String, u8> = HashMap::new();
        for l in ownings {
            hm.insert(l[0].to_string(), l[1].parse().unwrap());
        }
        sues.push(Sue {
            number,
            ownings: hm,
        })
    }
    return sues;
}

#[derive(Debug)]
struct Sue {
    number: i16,
    ownings: HashMap<String, u8>,
}

impl Sue {
    fn is_like(&self, other: &Sue) -> bool {
        for p in other.ownings.iter() {
            if !self.ownings.contains_key(p.0) {
                continue;
            }
            if self.ownings[p.0] != *p.1 {
                return false;
            }
        }
        return true;
    }

    fn i_dunno_what_to_call_this(&self, other: &Sue) -> bool {
        const LESS_THEN: [&str; 2] = ["pomeranians", "goldfish"];
        const MORE_THEN: [&str; 2] = ["cats", "trees"];
        for p in other.ownings.iter() {
            if !self.ownings.contains_key(p.0) {
                continue;
            }
            if MORE_THEN.contains(&&p.0[..]) {
                if self.ownings[p.0] < *p.1 {
                    return false;
                }
            } else if LESS_THEN.contains(&&p.0[..]) {
                if self.ownings[p.0] > *p.1 {
                    return false;
                }
            } else {
                if self.ownings[p.0] != *p.1 {
                    return false;
                }
            }
        }
        return true;
    }
}
