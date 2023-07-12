use common;
const INPUT_FILE: &str = "input/day06.txt";

enum Mode {
    On,
    Off,
    Toggle,
}

struct Action {
    mode: Mode,
    from: (u16, u16),
    to: (u16, u16),
}

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    let test =
        "turn on 0,0 through 999,999\ntoggle 0,0 through 999,0\nturn off 499,499 through 500,500";
    let test: Vec<Action> = test.lines().map(|f| line_parse(f.to_string())).collect();
    assert_eq!(task1(test), 1_000_000 - 1_000 - 4);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input: Vec<Action> = input.iter().map(|f| line_parse(f.to_string())).collect();

    let ans = task1(input);
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input: Vec<Action> = input.iter().map(|f| line_parse(f.to_string())).collect();

    let ans = task2(input);
    println!("Task 2 solution: {ans}");
}

fn task1(input: Vec<Action>) -> u32 {
    let mut map: Vec<Vec<bool>> = vec![vec![false; 1000]; 1000];
    for a in input {
        for x in a.from.0..a.to.0 + 1 {
            for y in a.from.1..a.to.1 + 1 {
                // println!("{x}:{y}");
                map[x as usize][y as usize] = match a.mode {
                    Mode::On => true,
                    Mode::Off => false,
                    Mode::Toggle => !map[x as usize][y as usize],
                }
            }
        }
    }

    map.iter()
        .map(|row| row.iter().fold(0, |acc, x| acc + *x as u32))
        .sum()
}

fn task2(input: Vec<Action>) -> u32 {
    let mut map: Vec<Vec<u32>> = vec![vec![0; 1000]; 1000];
    for a in input {
        for x in a.from.0..a.to.0 + 1 {
            for y in a.from.1..a.to.1 + 1 {
                // println!("{x}:{y}");
                let value = &mut map[x as usize][y as usize];
                *value = match a.mode {
                    Mode::On => *value + 1,
                    Mode::Off => match value.checked_sub(1) {
                        Some(i) => i,
                        None => 0,
                    },
                    Mode::Toggle => *value + 2,
                }
            }
        }
    }

    map.iter()
        .map(|row| row.iter().fold(0, |acc, x| acc + *x))
        .sum()
}

fn line_parse(input: String) -> Action {
    let parts = input.split(" ");
    let len = parts.clone().count();
    let from: Vec<u16> = parts
        .clone()
        .nth(len - 3)
        .unwrap()
        .split(",")
        .map(|f| f.parse().unwrap())
        .collect();
    let to: Vec<u16> = parts
        .clone()
        .nth(len - 1)
        .unwrap()
        .split(",")
        .map(|f| f.parse().unwrap())
        .collect();
    Action {
        mode: match parts.clone().nth(0).unwrap() {
            "toggle" => Mode::Toggle,
            "turn" => match parts.clone().nth(1).unwrap() {
                "on" => Mode::On,
                "off" => Mode::Off,
                _ => panic!("How"),
            },
            _ => panic!("How"),
        },
        from: (from[0], from[1]),
        to: (to[0], to[1]),
    }
}
