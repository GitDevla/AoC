use common;
const INPUT_FILE: &str = "input/day10.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    assert_eq!(task1("1".to_string(), 1), "11".to_string());
    assert_eq!(task1("1".to_string(), 5), "312211".to_string());

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input: String = input.first().unwrap().to_string();

    let ans = task1(input, 40).len();
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input: String = input.first().unwrap().to_string();

    let ans = task1(input, 50).len();
    println!("Task 2 solution: {ans}");
}

fn task1(input: String, times: i32) -> String {
    let mut times = times;
    let mut input = string_to_vec(input);
    while times > 0 {
        let mut new: Vec<u8> = Vec::new();
        let mut curent_char: &u8 = &input[0];
        let mut repeated_times: u8 = 1;
        for c in &input[1..] {
            if curent_char != c {
                new.push(repeated_times);
                new.push(*curent_char);
                repeated_times = 1;
                curent_char = c;
            } else {
                repeated_times += 1;
            }
        }

        new.push(repeated_times);
        new.push(*curent_char);
        times -= 1;
        input = new;
    }

    return vec_to_string(input);
}

fn vec_to_string(input: Vec<u8>) -> String {
    input
        .iter()
        .map(|i| i.to_string())
        .fold("".to_string(), |acc, s| acc + s.as_str())
}

fn string_to_vec(input: String) -> Vec<u8> {
    input
        .chars()
        .map(|c| c.to_digit(10).unwrap() as u8)
        .collect()
}
