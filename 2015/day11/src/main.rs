use std::collections::HashSet;

use common;
const INPUT_FILE: &str = "input/day11.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    assert_eq!(check_password(&"hijklmmn".to_string()), false);
    assert_eq!(check_password(&"abbceffg".to_string()), false);
    assert_eq!(check_password(&"abbcegjk".to_string()), false);
    assert_eq!(check_password(&"abcdffaa".to_string()), true);
    assert_eq!(check_password(&"ghjaabcc".to_string()), true);
    assert_eq!(task1("abcdefgh".to_string()), "abcdffaa".to_string());
    assert_eq!(task1("ghijklmn".to_string()), "ghjaabcc".to_string());

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input: String = input.first().unwrap().to_string();

    let ans = task1(input);
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input: String = input.first().unwrap().to_string();

    let ans = task1(input);
    let ans = task1(ans);
    println!("Task 2 solution: {ans}");
}

fn task1(input: String) -> String {
    let mut found = false;
    let mut curr = input.to_string();
    while !found {
        curr = next_string(curr);
        found = check_password(&curr);
    }
    return curr;
}

fn next_string(input: String) -> String {
    let mut input: Vec<u8> = input.chars().map(|c| c as u8).collect();
    let length = input.len();
    let mut acc = 1;
    let mut curr = 0;
    while acc != 0 {
        let c = match input.get_mut(length - curr - 1) {
            Some(c) => c,
            None => panic!("Az baj"),
        };
        *c += 1;
        if *c > 'z' as u8 {
            acc += 1;
            curr += 1;
            *c = 'a' as u8;
        }
        acc -= 1;
    }
    return input.iter().map(|c| *c as char).collect();
}

fn check_password(input: &String) -> bool {
    const INVALID_CHARS: [char; 3] = ['i', 'o', 'l'];
    if INVALID_CHARS.iter().any(|c| input.contains(*c)) {
        return false;
    }
    let mut increasing_letter = false;
    let mut letter_pairs: HashSet<char> = HashSet::new();
    let mut streak = 1;
    for (i, curr_c) in input.chars().enumerate() {
        match input.chars().nth(i + 1) {
            Some(next_c) => {
                if curr_c == next_c {
                    letter_pairs.insert(curr_c);
                }
                if curr_c as u8 + 1 == next_c as u8 {
                    streak += 1;
                } else {
                    streak = 1;
                }
                if streak >= 3 {
                    increasing_letter = true;
                }
            }
            None => (),
        }
    }
    let two_letter_pairs = letter_pairs.len() >= 2;
    return two_letter_pairs && increasing_letter;
}
