use std::collections::HashMap;

use common;
const INPUT_FILE: &str = "input/day13.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    let test = r#"Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."#;
    let test: Vec<String> = test.lines().map(String::from).collect();
    assert_eq!(task1(parse_data(test)), 330);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input = parse_data(input);

    let ans = task1(input);
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input = parse_data(input);

    let ans = task2(input);
    println!("Task 2 solution: {ans}");
}

fn task1(input: HashMap<String, Vec<(String, i8)>>) -> i32 {
    let seats = vec![input
        .keys()
        .collect::<Vec<&String>>()
        .first()
        .unwrap()
        .to_string()];
    let a = optimal_seating(&input, seats);
    return calc_dist(&input, &a);
}

fn optimal_seating(people: &HashMap<String, Vec<(String, i8)>>, seats: Vec<String>) -> Vec<String> {
    if seats.len() == people.len() {
        return seats;
    }
    let p: Vec<&String> = people.keys().collect();
    let mut best_path: Vec<String> = vec![];
    for next_people in p.iter().filter(|c| !seats.contains(&c)) {
        let mut new_seating = seats.clone();
        new_seating.push(next_people.to_string());
        let new_path = optimal_seating(people, new_seating);
        if best_path.len() == 0 || calc_dist(people, &best_path) < calc_dist(people, &new_path) {
            best_path = new_path;
        }
    }
    return best_path;
}

fn calc_dist(graph: &HashMap<String, Vec<(String, i8)>>, path: &Vec<String>) -> i32 {
    let mut a = path.iter().peekable();
    let mut sum: i32 = 0;
    let mut prev: Option<&String> = None;
    let last = path.last().unwrap();
    let first = path.first().unwrap();
    while let Some(node) = a.next() {
        let person = graph.get(node).unwrap();
        let next_love: i32 = match a.peek() {
            Some(next) => person.iter().find(|(name, _)| name == *next).unwrap().1 as i32,
            None => person.iter().find(|(name, _)| name == first).unwrap().1 as i32,
        };
        let prev_love: i32 = match prev {
            Some(next) => person.iter().find(|(name, _)| name == next).unwrap().1 as i32,
            None => person.iter().find(|(name, _)| name == last).unwrap().1 as i32,
        };
        prev = Some(node);
        sum += next_love;
        sum += prev_love;
    }
    return sum;
}

fn task2(input: HashMap<String, Vec<(String, i8)>>) -> i32 {
    let MY_NAME: String = "GitDevla".to_string();
    let mut new = input;
    let everyonw: Vec<(String, i8)> = new.keys().map(|c: &String| (c.clone(), 0_i8)).collect();
    new.values_mut()
        .for_each(|f: &mut Vec<(String, i8)>| f.push((MY_NAME.clone(), 0_i8)));
    new.insert(MY_NAME.clone(), everyonw);
    let seats = vec![new
        .keys()
        .collect::<Vec<&String>>()
        .first()
        .unwrap()
        .to_string()];
    let a = optimal_seating(&new, seats);
    return calc_dist(&new, &a);
}

fn parse_data(input: Vec<String>) -> HashMap<String, Vec<(String, i8)>> {
    let mut map: HashMap<String, Vec<(String, i8)>> = HashMap::new();
    for line in input {
        let parts: Vec<&str> = line.split(" happiness units by sitting next to ").collect();
        let next_to = parts[1].trim_end_matches(".");
        let parts: Vec<&str> = parts[0].split(" would ").collect();
        let who = parts[0].to_string();
        let parts: Vec<&str> = parts[1].split(" ").collect();
        let love: i8 = match parts[0] {
            "gain" => parts[1].parse().unwrap(),
            "lose" => parts[1].parse::<i8>().unwrap() * -1,
            _ => panic!("how"),
        };
        if !map.contains_key(&who) {
            map.insert(who.clone(), vec![]);
        }
        map.get_mut(&who).unwrap().push((next_to.to_string(), love));
    }
    return map;
}
