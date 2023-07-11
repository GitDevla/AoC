use common;
const INPUT_FILE: &str = "input/day05.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    assert_eq!(task1("ugknbfddgicrmopn".to_string()), true);
    assert_eq!(task1("aaa".to_string()), true);
    assert_eq!(task1("jchzalrnumimnmhp".to_string()), false);
    assert_eq!(task1("haegwjzuvuyypxyu".to_string()), false);
    assert_eq!(task1("dvszwmarrgswjxmb".to_string()), false);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);

    let ans = input.iter().filter(|f| task1(f.to_string())).count();
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test
    assert_eq!(task2("qjhvhtzxzqqjkmpb".to_string()), true);
    assert_eq!(task2("xxyxxb".to_string()), true);
    assert_eq!(task2("uurcxstgmygtbstg".to_string()), false);
    assert_eq!(task2("ieodomkazucvgmuy".to_string()), false);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);

    let ans = input.iter().filter(|f| task2(f.to_string())).count();
    println!("Task 2 solution: {ans}");
}

fn task1(input: String) -> bool {
    const VOWELS: [char; 5] = ['a', 'e', 'i', 'o', 'u'];
    let mut no_of_vowels = 0;
    let mut same_letter_twice = false;
    const FILTER: [&str; 4] = ["ab", "cd", "pq", "xy"];
    if FILTER.iter().any(|f| input.contains(f)) {
        return false;
    }
    for (i, _) in input.chars().enumerate() {
        if input.chars().nth(i + 1).is_none() {
            continue;
        }
        let slice: &str = &input[i..i + 2];
        if slice.chars().nth(0) == slice.chars().nth(1) {
            same_letter_twice = true;
        }
    }
    for l in input.chars() {
        if VOWELS.contains(&l) {
            no_of_vowels += 1;
        }
    }
    return no_of_vowels >= 3 && same_letter_twice;
}

fn task2(input: String) -> bool {
    let mut repeating_letter = false;
    let mut repeating_pair = false;
    'outer: for (i, _) in input.chars().enumerate() {
        if input.chars().nth(i + 2).is_none() {
            break;
        }
        let left = &input[i..i + 2];
        for (x, _) in input.chars().skip(i + 2).enumerate() {
            let j = i + x + 2;
            if input.chars().nth(j + 1).is_none() {
                break;
            }
            let right = &input[j..j + 2];
            if left == right {
                repeating_pair = true;
                break 'outer;
            }
        }
    }

    for (i, l) in input.chars().enumerate() {
        let left: char = l;
        let right: char = match input.chars().nth(i + 2) {
            Some(a) => a,
            None => break,
        };
        if left == right {
            repeating_letter = true;
            break;
        }
    }

    return repeating_letter && repeating_pair;
}
