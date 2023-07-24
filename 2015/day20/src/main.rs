use common;
const INPUT_FILE: &str = "input/day20.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input: u32 = input.first().unwrap().parse().unwrap();
    let input = input / 10;

    let ans = task1(input);
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input: u32 = input.first().unwrap().parse().unwrap();
    let input = input / 11;

    let ans = task2(input);
    println!("Task 2 solution: {ans}");
}

fn task1(input: u32) -> u32 {
    let mut house = 770_000;
    loop {
        let sum = (1..=house).fold(0, |sum, n| sum + if house % n == 0 { n } else { 0 });

        if sum >= input {
            return house;
        }

        house += 1;
    }
}

fn task2(input: u32) -> u32 {
    let mut house = 780_000;
    loop {
        let sum = (1..=house).fold(0, |sum, n| {
            sum + if house % n == 0 && n * 50 >= house {
                n
            } else {
                0
            }
        });

        if sum >= input {
            return house;
        }

        house += 1;
    }
}
