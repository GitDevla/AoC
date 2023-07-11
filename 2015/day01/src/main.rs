use common;
const INPUT_FILE: &str = "input/day01.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    assert_eq!(task1("(())".to_string()), 0);
    assert_eq!(task1("()()".to_string()), 0);
    assert_eq!(task1("(((".to_string()), 3);
    assert_eq!(task1("(()(()(".to_string()), 3);
    assert_eq!(task1("))(((((".to_string()), 3);
    assert_eq!(task1("())".to_string()), -1);
    assert_eq!(task1("))(".to_string()), -1);
    assert_eq!(task1(")))".to_string()), -3);
    assert_eq!(task1(")())())".to_string()), -3);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input: String = input.first().unwrap().to_string();

    let ans = task1(input);
    println!("Task 1: {ans}");
}

fn pt2() {
    // Test
    assert_eq!(task2(")".to_string()), 1);
    assert_eq!(task2("()())".to_string()), 5);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input: String = input.first().unwrap().to_string();

    let ans = task2(input);
    println!("Task 2: {ans}");
}

fn task1(steps: String) -> i32 {
    let mut floor = 0;
    for letter in steps.chars() {
        floor += match letter {
            '(' => 1,
            ')' => -1,
            _ => 0,
        };
    }
    return floor;
}

fn task2(steps: String) -> i32 {
    const BASEMENT: i32 = -1;
    let mut curr_floor: i32 = 0;
    for (i, letter) in steps.chars().enumerate() {
        curr_floor += match letter {
            '(' => 1,
            ')' => -1,
            _ => 0,
        };
        if curr_floor == BASEMENT {
            return i as i32 + 1;
        }
    }
    return -1;
}
