use common;
const INPUT_FILE: &str = "input/day06.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    let test_input = r#"Time:      7  15   30
Distance:  9  40  200"#;
    let test_input = parse(test_input.lines().map(String::from).collect());
    assert_eq!(solve(test_input), 288);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input = parse(input);

    let ans = solve(input);
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test
    let test_input = r#"Time:      7  15   30
Distance:  9  40  200"#;
    let test_input = test_input.replace(" ", "");
    let test_input = parse(test_input.lines().map(String::from).collect());
    assert_eq!(solve(test_input), 71503);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input = input.iter().map(|f| f.replace(" ", "")).collect();
    let input = parse(input);

    let ans = solve(input);
    println!("Task 2 solution: {ans}");
}

fn solve(input: Vec<Race>) -> i32 {
    input
        .iter()
        .map(|i| count_possible_wins(*i))
        .reduce(|acc, f| acc * f)
        .unwrap()
}

fn count_possible_wins(input: Race) -> i32 {
    let a = -1.0;
    let b = input.time as f64;
    let c = -(input.distance as f64);
    let d = b.powi(2) - 4.0 * a * c;
    let x1 = (-b + d.sqrt()) / (2.0 * a) + 0.001;
    let x2 = (-b - d.sqrt()) / (2.0 * a) - 0.001;
    return x2.floor() as i32 - x1.ceil() as i32 + 1;
}

fn parse(input: Vec<String>) -> Vec<Race> {
    let times: Vec<&str> = input[0]
        .trim_start_matches("Time:")
        .split_whitespace()
        .collect();
    let distances: Vec<&str> = input[1]
        .trim_start_matches("Distance:")
        .split_whitespace()
        .collect();
    let mut output = vec![];
    for (idx, t) in times.iter().enumerate() {
        output.push(Race {
            time: t.parse::<u64>().unwrap(),
            distance: distances[idx].parse::<u64>().unwrap(),
        })
    }
    return output;
}

#[derive(Debug, Clone, Copy)]
struct Race {
    time: u64,
    distance: u64,
}
