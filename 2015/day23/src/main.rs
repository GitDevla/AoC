use std::borrow::BorrowMut;

use common;
const INPUT_FILE: &str = "input/day23.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    let test = r#"inc b
jio b, +2
tpl b
inc b"#;
    let test: Vec<String> = test.lines().map(String::from).collect();

    assert_eq!(task1(test), 2);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);

    let ans = task1(input);
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);

    let ans = task2(input);
    println!("Task 2 solution: {ans}");
}

fn task1(input: Vec<String>) -> i32 {
    let mut comp: Computer = Computer::new();
    comp.execute(input);
    return *comp.letter_to_reg("b");
}

fn task2(input: Vec<String>) -> i32 {
    let mut comp: Computer = Computer::new();
    *comp.letter_to_reg("a") = 1;
    comp.execute(input);
    return *comp.letter_to_reg("b");
}

struct Computer {
    registers: Vec<i32>,
}

impl Computer {
    fn new() -> Self {
        Self {
            registers: vec![0; 2],
        }
    }

    fn execute(&mut self, code: Vec<String>) {
        let mut line: i32 = 0;
        while line < code.len() as i32 {
            let current_code = &code[line as usize];
            let split: Vec<&str> = current_code
                .split(" ")
                .map(|s| s.trim_end_matches(","))
                .collect::<Vec<_>>();
            match split[0] {
                "hlf" => *self.letter_to_reg(split[1]) = *self.letter_to_reg(split[1]) / 2,
                "tpl" => *self.letter_to_reg(split[1]) = *self.letter_to_reg(split[1]) * 3,
                "inc" => *self.letter_to_reg(split[1]) += 1,
                "jmp" => {
                    line += split[1].parse::<i32>().unwrap();
                    continue;
                }
                "jie" => {
                    if *self.letter_to_reg(split[1]) % 2 == 0 {
                        line += split[2].parse::<i32>().unwrap();
                        continue;
                    }
                }
                "jio" => {
                    if *self.letter_to_reg(split[1]) == 1 {
                        line += split[2].parse::<i32>().unwrap();
                        continue;
                    }
                }
                _ => panic!("xd"),
            }
            line += 1;
        }
    }

    fn letter_to_reg(&mut self, letter: &str) -> &mut i32 {
        self.registers[letter.chars().nth(0).unwrap() as usize - 'a' as usize].borrow_mut()
    }
}
