use std::collections::HashMap;

use common;
const INPUT_FILE: &str = "input/day09.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    let test = "London to Dublin = 464\nLondon to Belfast = 518\nDublin to Belfast = 141";
    let test: Vec<String> = test.lines().map(String::from).collect();
    assert_eq!(task1(parse_nodes(test)), 605);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input = parse_nodes(input);

    let ans = task1(input);
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test
    let test = "London to Dublin = 464\nLondon to Belfast = 518\nDublin to Belfast = 141";
    let test: Vec<String> = test.lines().map(String::from).collect();
    assert_eq!(task2(parse_nodes(test)), 982);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input = parse_nodes(input);

    let ans = task2(input);
    println!("Task 2 solution: {ans}");
}

fn task1(input: HashMap<String, Vec<(String, u16)>>) -> u32 {
    let best_path = tsp(&input, vec![], false);
    let dist = calc_dist(&input, &best_path);
    return dist;
}

fn task2(input: HashMap<String, Vec<(String, u16)>>) -> u32 {
    let best_path = tsp(&input, vec![], true);
    let dist = calc_dist(&input, &best_path);
    return dist;
}

fn tsp(
    graph: &HashMap<String, Vec<(String, u16)>>,
    path: Vec<String>,
    find_longest: bool,
) -> Vec<String> {
    let current_node = match path.last() {
        Some(x) => x,
        None => "",
    };
    let neighbors: Vec<String> = match graph.get(current_node) {
        Some(x) => x.iter().map(|f| f.0.clone()).collect(),
        None => graph.keys().map(|f| f.clone()).collect(),
    };

    if path.len() == graph.len() {
        return path;
    }
    let mut best_path: Vec<String> = vec![];
    for next_city in neighbors.iter().filter(|c| !path.contains(&c)) {
        let mut new_path = path.clone();
        new_path.push(next_city.clone());
        let new_path = tsp(graph, new_path, find_longest);
        if find_longest {
            if calc_dist(graph, &best_path) < calc_dist(graph, &new_path) || best_path.len() == 0 {
                best_path = new_path;
            }
        } else {
            if calc_dist(graph, &best_path) > calc_dist(graph, &new_path) || best_path.len() == 0 {
                best_path = new_path;
            }
        }
    }
    return best_path;
}

fn calc_dist(graph: &HashMap<String, Vec<(String, u16)>>, path: &Vec<String>) -> u32 {
    let mut a = path.iter().peekable();
    let mut dist: u32 = 0;
    while let Some(node) = a.next() {
        let city = graph.get(node).unwrap();
        let dista: u32 = match a.peek() {
            Some(next) => city.iter().find(|(name, _)| name == *next).unwrap().1 as u32,
            None => 0,
        };
        dist += dista;
    }
    return dist;
}

fn parse_nodes(input: Vec<String>) -> HashMap<String, Vec<(String, u16)>> {
    let mut map: HashMap<String, Vec<(String, u16)>> = HashMap::new();
    for line in input {
        let parts: Vec<&str> = line.split(" = ").collect();
        let dist: u16 = parts[1].parse().unwrap();
        let parts: Vec<&str> = parts[0].split(" to ").collect();
        let from_name = parts[0].to_string();
        let to_name = parts[1].to_string();

        if !map.contains_key(&from_name) {
            map.insert(from_name.clone(), vec![]);
        }
        if !map.contains_key(&to_name) {
            map.insert(to_name.clone(), vec![]);
        }
        map.get_mut(&from_name)
            .unwrap()
            .push((to_name.clone(), dist));
        map.get_mut(&to_name)
            .unwrap()
            .push((from_name.clone(), dist));
    }
    // println!("{:#?}", map);
    return map;
}
