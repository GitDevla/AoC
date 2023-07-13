use common;
const INPUT_FILE: &str = "input/day08.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // // Test
    assert_eq!(task1(r#""""#.to_string()), 2);
    assert_eq!(task1(r#""abc""#.to_string()), 2);
    assert_eq!(task1(r#""aaa\"aaa""#.to_string()), 3);
    assert_eq!(task1(r#""\x27""#.to_string()), 5);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);

    let ans: usize = input.iter().map(|f| task1(f.to_string())).sum();
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // // Test
    assert_eq!(task2(r#""""#.to_string()), 4);
    assert_eq!(task2(r#""abc""#.to_string()), 4);
    assert_eq!(task2(r#""aaa\"aaa""#.to_string()), 6);
    assert_eq!(task2(r#""\x27""#.to_string()), 5);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);

    let ans: usize = input.iter().map(|f| task2(f.to_string())).sum();
    println!("Task 1 solution: {ans}");
}

#[warn(unused_assignments)]
fn task1(s: String) -> usize {
    let code = s.len();
    let mut memory = 0;
    let mut break_mode = false;
    const BREAK_CHAR: char = '\\';
    const HEX_NOTATION: char = 'x';
    if code == 2 {
        return 2;
    };
    let mut indice = s[1..code - 1].char_indices();
    while let Some(c) = indice.next() {
        if break_mode {
            if c.1 == HEX_NOTATION {
                indice.next();
                indice.next();
                break_mode = false; // tf you mean unused
            }
            break_mode = false;
            continue;
        } else {
            memory += 1;
        }
        break_mode = c.1 == BREAK_CHAR;
    }
    return code - memory;
}

fn task2(input: String) -> usize {
    let length = input.len();
    let formated: usize = format!("{:?}", input).len();
    return formated - length;
}
