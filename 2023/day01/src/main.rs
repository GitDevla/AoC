use common;
const INPUT_FILE: &str = "input/day01.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    let test_input = r#"1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet"#;
    let test_input: Vec<String> = test_input.lines().map(String::from).collect();
    assert_eq!(task1(test_input), 142);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);

    let ans = task1(input);
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test
    let test_input = r#"two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen"#;
    let test_input: Vec<String> = test_input.lines().map(String::from).collect();
    assert_eq!(task2(test_input), 281);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);

    let ans = task2(input);
    println!("Task 2 solution: {ans}");
}

fn task1(input: Vec<String>) -> i32 {
    input.iter().map(|i| get_passwd(i)).sum()
}

fn task2(input: Vec<String>) -> i32 {
    input
        .iter()
        .map(|i| convert_password(i))
        .map(|i| get_passwd(&i))
        .sum()
}

fn get_passwd(input: &String) -> i32 {
    let mut nums: Vec<char> = vec![];
    for letter in input.chars() {
        if letter.is_numeric() {
            nums.push(letter)
        }
    }
    return format!("{}{}", nums.first().unwrap(), nums.last().unwrap())
        .parse()
        .unwrap();
}

fn convert_password(input: &String) -> String {
    let input = input;
    let input = &input.replace("one", "one1one");
    let input = &input.replace("two", "two2two");
    let input = &input.replace("three", "three3three");
    let input = &input.replace("four", "four4four");
    let input = &input.replace("five", "five5five");
    let input = &input.replace("six", "six6six");
    let input = &input.replace("seven", "seven7seven");
    let input = &input.replace("eight", "eight8eight");
    let input = &input.replace("nine", "nine9nine");
    return input.to_string();
}
