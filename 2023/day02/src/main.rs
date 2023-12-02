use common;
const INPUT_FILE: &str = "input/day02.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    let test_input = r#"Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"#;
    let test_input: Vec<String> = test_input.lines().map(String::from).collect();
    assert_eq!(task1(test_input), 8);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);

    let ans = task1(input);
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test
    let test_input = r#"Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"#;
    let test_input: Vec<String> = test_input.lines().map(String::from).collect();
    assert_eq!(task2(test_input), 2286);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);

    let ans = task2(input);
    println!("Task 2 solution: {ans}");
}

fn task1(input: Vec<String>) -> i32 {
    let limit = (12, 13, 14);
    let mut sum: i32 = 0;
    'single_game: for (i, game) in input.iter().enumerate() {
        let subsets: Vec<&str> = game.split(":").nth(1).unwrap().split(";").collect();
        for reveal in subsets {
            let pulls: Vec<&str> = reveal.split(",").map(|i| i.trim()).collect();
            for single_pull in pulls {
                let split: Vec<&str> = single_pull.split(" ").collect();
                let number: i32 = split[0].parse().unwrap();
                let color = split[1];
                let is_possible = match color {
                    "red" => number <= limit.0,
                    "green" => number <= limit.1,
                    "blue" => number <= limit.2,
                    _ => panic!("huh"),
                };
                if !is_possible {
                    continue 'single_game;
                }
            }
        }
        sum += i as i32 + 1;
    }
    return sum;
}

fn task2(input: Vec<String>) -> i32 {
    let mut sum: i32 = 0;
    for game in input {
        let mut max_colors = [0, 0, 0];
        let subsets: Vec<&str> = game.split(":").nth(1).unwrap().split(";").collect();
        for reveal in subsets {
            let pulls: Vec<&str> = reveal.split(",").map(|i| i.trim()).collect();
            for single_pull in pulls {
                let split: Vec<&str> = single_pull.split(" ").collect();
                let number: i32 = split[0].parse().unwrap();
                let color = split[1];
                match color {
                    "red" => {
                        if max_colors[0] < number {
                            max_colors[0] = number
                        }
                    }
                    "green" => {
                        if max_colors[1] < number {
                            max_colors[1] = number
                        }
                    }
                    "blue" => {
                        if max_colors[2] < number {
                            max_colors[2] = number
                        }
                    }
                    _ => panic!("huh"),
                };
            }
        }
        let mut mul = 1;
        for x in max_colors {
            mul *= x;
        }
        sum += mul;
    }
    return sum;
}
