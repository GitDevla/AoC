use std::collections::HashMap;

use common;
use regex::Regex;
const INPUT_FILE: &str = "input/day15.txt";

/*
    change          time
    first impl      n/a
    cache:String    22s
    cache:Vec       12s
*/

fn main() {
    // use std::time::Instant;
    // let now = Instant::now();

    // // Code block to measure.
    // {
    pt1();
    pt2();
    // }

    // let elapsed = now.elapsed();
    // println!("Elapsed: {:.2?}", elapsed);
}

fn pt1() {
    // Test
    let test = r#"Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"#;
    let test: Vec<String> = test.lines().map(String::from).collect();
    let test = parse(test);
    assert_eq!(task1(test), 62842880);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input = parse(input);

    let ans = task1(input);
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // // Test
    let test = r#"Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"#;
    let test: Vec<String> = test.lines().map(String::from).collect();
    let test = parse(test);
    assert_eq!(task2(test), 57600000);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input = parse(input);

    let ans = task2(input);
    println!("Task 2 solution: {ans}");
}

fn task1(input: Vec<Recipe>) -> i32 {
    let mut cache = HashMap::new();
    find_best_calorie(&input, vec![0; input.len()], 0, &mut cache, false)
}

fn task2(input: Vec<Recipe>) -> i32 {
    let mut cache = HashMap::new();
    find_best_calorie(&input, vec![0; input.len()], 0, &mut cache, true)
}

fn calculate_score(recipies: &Vec<Recipe>, current_combination: &Vec<u8>) -> i32 {
    let mut sum: Vec<i32> = vec![0; 4];
    for (i, x) in current_combination.iter().enumerate() {
        let recipie = &recipies[i];
        sum[0] += i32::from(recipie.capacity) * i32::from(*x);
        sum[1] += i32::from(recipie.durability) * i32::from(*x);
        sum[2] += i32::from(recipie.flavor) * i32::from(*x);
        sum[3] += i32::from(recipie.texture) * i32::from(*x);
    }
    if sum.iter().any(|f| *f < 0) {
        return 0;
    }
    return sum.iter().fold(1_i32, |acc, &value| acc * value);
}

fn calculate_calorie(recipies: &Vec<Recipe>, current_combination: &Vec<u8>) -> i32 {
    let mut sum = 0;
    for (i, x) in current_combination.iter().enumerate() {
        let recipie = &recipies[i];
        sum += i32::from(recipie.calories) * i32::from(*x);
    }
    return sum;
}

fn no_spoons(current_combination: &Vec<u8>) -> i8 {
    current_combination.iter().map(|f| *f as i8).sum()
}

fn parse(input: Vec<String>) -> Vec<Recipe> {
    let pattern = r"(?P<name>[a-zA-Z\s]+):\s*capacity\s*(?P<capacity>-?\d+),\s*durability\s*(?P<dur>-?\d+),\s*flavor\s*(?P<flav>-?\d+),\s*texture\s*(?P<text>-?\d+),\s*calories\s*(?P<calor>-?\d+)";
    let re = Regex::new(pattern).unwrap();
    let mut recipies: Vec<Recipe> = vec![];
    for l in input.iter() {
        let caps = re.captures(l).unwrap();
        let name = caps.name("name").unwrap().as_str().to_string();
        let capacity = caps
            .name("capacity")
            .unwrap()
            .as_str()
            .parse::<i8>()
            .unwrap();
        let durability = caps.name("dur").unwrap().as_str().parse::<i8>().unwrap();
        let flavor = caps.name("flav").unwrap().as_str().parse::<i8>().unwrap();
        let texture = caps.name("text").unwrap().as_str().parse::<i8>().unwrap();
        let calories = caps.name("calor").unwrap().as_str().parse::<i8>().unwrap();
        recipies.push(Recipe {
            name,
            capacity,
            durability,
            flavor,
            texture,
            calories,
        })
    }
    return recipies;
}

#[allow(dead_code)]
struct Recipe {
    name: String,
    capacity: i8,
    durability: i8,
    flavor: i8,
    texture: i8,
    calories: i8,
}

fn find_best_calorie(
    recipies: &Vec<Recipe>,
    current_combination: Vec<u8>,
    best: i32,
    cache: &mut HashMap<Vec<u8>, i32>,
    calorie_limit: bool,
) -> i32 {
    let mut best = best;

    if cache.contains_key(&current_combination) {
        return cache[&current_combination];
    }
    if no_spoons(&current_combination) - 100 == 0 {
        if calorie_limit && calculate_calorie(recipies, &current_combination) != 500 {
            return -1;
        }
        let score = calculate_score(recipies, &current_combination);

        return score;
    }

    for i in 0..recipies.len() {
        let mut next_comb = current_combination.clone();
        next_comb[i] += 1;
        let next = find_best_calorie(recipies, next_comb.clone(), best, cache, calorie_limit);
        if next > best {
            best = next;
        }
    }
    cache.insert(current_combination, best);
    return best;
}
