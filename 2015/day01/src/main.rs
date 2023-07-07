use common;

fn main() {
    // Puzzle 1 tests
    assert_eq!(task1("(())"), 0);
    assert_eq!(task1("()()"), 0);
    assert_eq!(task1("((("), 3);
    assert_eq!(task1("(()(()("), 3);
    assert_eq!(task1("))((((("), 3);
    assert_eq!(task1("())"), -1);
    assert_eq!(task1("))("), -1);
    assert_eq!(task1(")))"), -3);
    assert_eq!(task1(")())())"), -3);

    // Puzzle 1 solution
    let file = common::read_file("input/day01.txt");
    let input = file.first().unwrap();

    let ans = task1(input);
    println!("Task 1: {ans}");

    // Puzzle 2 tests
    assert_eq!(task1(")())())"), -3);
    assert_eq!(task1(")())())"), -3);

    let ans = task2(input);
    println!("Task 2: {ans}");
}

fn task1(steps: &str) -> i32 {
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

fn task2(steps: &String) -> i32 {
    const BASEMENT: i32 = -1;
    let mut curr_floor: i32 = 0;
    let mut steps_taken: i32 = 0;
    for letter in steps.chars() {
        curr_floor += match letter {
            '(' => 1,
            ')' => -1,
            _ => 0,
        };
        if curr_floor == BASEMENT {
            break;
        }
        steps_taken += 1;
    }
    return steps_taken;
}
