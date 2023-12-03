use std::collections::HashMap;

use common;
const INPUT_FILE: &str = "input/day03.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    let test_input = r#"467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."#;
    let test_input: Vec<String> = test_input.lines().map(String::from).collect();
    assert_eq!(task1(test_input), 4361);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);

    let ans = task1(input);
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test
    let test_input = r#"467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."#;
    let test_input: Vec<String> = test_input.lines().map(String::from).collect();
    assert_eq!(task2(test_input), 467835);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);

    let ans = task2(input);
    println!("Task 2 solution: {ans}");
}

fn task1(input: Vec<String>) -> i32 {
    let numbers = get_numbers(&input);
    let sysmbol = find_gears(&input, |f| is_token(f));
    let sum: i32 = find_number_next_to_gears(&sysmbol, &numbers)
        .iter()
        .flat_map(|f| f.1.iter().map(|f| f.number as i32))
        .sum();
    sum
}

fn task2(input: Vec<String>) -> i32 {
    let nums = get_numbers(&input);
    let gears = find_gears(&input, |f| *f == '*');
    let close_gears: HashMap<(usize, usize), Vec<Number>> =
        find_number_next_to_gears(&gears, &nums);
    close_gears
        .iter()
        .filter(|f| f.1.len() == 2)
        .map(|f| f.1[0].number as i32 * f.1[1].number as i32)
        .sum()
}

fn get_numbers(input: &Vec<String>) -> Vec<Number> {
    let mut numbers = vec![];
    for (y, line) in input.iter().enumerate() {
        let mut x: usize = 0;
        while x < line.len() {
            let character = line.chars().nth(x).unwrap();
            if character.is_numeric() {
                let next_non_number_char = line[x..]
                    .find(|f: char| !f.is_numeric())
                    .unwrap_or(line.len() - x);
                let number: u32 = line[x..next_non_number_char + x].parse().unwrap();
                let number_length = number.to_string().len();
                numbers.push(Number {
                    line: y,
                    start: x,
                    end: x + number_length - 1,
                    number: number,
                });
                x += number_length as usize - 1;
            }
            x += 1;
        }
    }
    return numbers;
}
#[derive(Debug, Clone, Copy)]
struct Number {
    line: usize,
    start: usize,
    end: usize,
    number: u32,
}

fn find_gears<P>(map: &Vec<String>, pred: P) -> Vec<(usize, usize)>
where
    P: Fn(&char) -> bool,
{
    let mut gears = vec![];
    for (y, line) in map.iter().enumerate() {
        for (x, character) in line.chars().enumerate() {
            if pred(&character) {
                gears.push((x, y));
            }
        }
    }
    return gears;
}

fn is_token(c: &char) -> bool {
    !c.is_numeric() && *c != '.'
}

fn find_number_next_to_gears(
    gear: &Vec<(usize, usize)>,
    numbers: &Vec<Number>,
) -> HashMap<(usize, usize), Vec<Number>> {
    let mut close_gears: HashMap<(usize, usize), Vec<Number>> = HashMap::new();
    for g in gear {
        let (x, y) = g;
        let nums: Vec<Number> = numbers
            .iter()
            .filter(|f| (y - 1..y + 2).contains(&f.line))
            .filter(|f| does_range_have_union((x - 1, x + 2), (f.start, f.end)))
            .map(|f| *f)
            .collect();
        close_gears.insert(*g, nums);
    }
    return close_gears;
}

fn does_range_have_union(range: (usize, usize), other: (usize, usize)) -> bool {
    (range.0..range.1).contains(&other.0) || (range.0..range.1).contains(&other.1)
}
