use std::{collections::VecDeque, ops::Range};

use common::{self, benchmark};
const INPUT_FILE: &str = "input/day05.txt";

fn main() {
    benchmark(pt1);
    benchmark(pt2);
    // pt2();
}

fn pt1() {
    let test_input = r#"seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"#;
    let test_input: Vec<String> = test_input.lines().map(String::from).collect();
    // Test
    let test_input = parse(test_input);
    assert_eq!(task1(test_input), 35);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input = parse(input);

    let ans = task1(input);
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test
    let test_input = r#"seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"#;
    let test_input: Vec<String> = test_input.lines().map(String::from).collect();
    // Test
    let test_input = parse(test_input);
    assert_eq!(task2(test_input), 46);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input = parse(input);

    let ans = task2(input);
    println!("Task 2 solution: {ans}");
}

fn task1(input: (Vec<u64>, Vec<Vec<Convertor>>)) -> u64 {
    let (mut seeds, convertors) = input;
    for converts in convertors {
        for seed in seeds.iter_mut() {
            converts
                .iter()
                .find(|x| x.is_in_range(*seed))
                .and_then(|f| Some(*seed = f.convert(*seed)));
        }
    }
    return *seeds.iter().min().unwrap();
}

// i dont wanna talk about it
fn task2(input: (Vec<u64>, Vec<Vec<Convertor>>)) -> u64 {
    let (seeds, convertors) = input;
    let mut ranges = vec![];
    for x in seeds.iter().step_by(2).zip(seeds.iter().skip(1).step_by(2)) {
        ranges.push(*x.0..(x.0 + x.1));
    }
    for converts in convertors {
        let mut range_queue: VecDeque<Range<u64>> = ranges.iter().cloned().collect();
        let mut new_ranges: Vec<Range<u64>> = vec![];
        while let Some(range) = range_queue.pop_front() {
            let mut something_happened: bool = false;
            for convert in converts.iter() {
                if convert.has_union_with_range(range.clone()) {
                    let (new_range, untouched) = convert.convert_range(range.clone());
                    something_happened = true;
                    new_ranges.push(new_range);
                    for x in untouched.iter() {
                        range_queue.push_back(x.clone());
                    }
                }
            }
            if !something_happened {
                new_ranges.push(range.clone());
            }
        }
        for x in range_queue.iter() {
            new_ranges.push(x.clone());
        }
        ranges = new_ranges;
    }
    return ranges.iter().map(|f| f.start).min().unwrap();
}

fn parse(input: Vec<String>) -> (Vec<u64>, Vec<Vec<Convertor>>) {
    let seeds = &input[0];
    let seeds: Vec<u64> = seeds
        .trim_start_matches("seeds: ")
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let mut convertors: Vec<Vec<Convertor>> = vec![];
    let mut current_convertors: Vec<Convertor> = vec![];
    for line in input[2..].iter() {
        if line == "" {
            convertors.push(current_convertors.clone());
            current_convertors.clear();
            continue;
        }
        if line.contains("map:") {
            continue;
        }
        let line: Vec<u64> = line
            .split_whitespace()
            .map(|x| x.parse().unwrap())
            .collect();
        current_convertors.push(Convertor::new(line[1], line[0], line[2]));
    }
    convertors.push(current_convertors.clone());

    return (seeds, convertors);
}

#[derive(Clone, Debug)]
struct Convertor {
    from_start: u64,
    from_end: u64,
    to_start: u64,
}
impl Convertor {
    fn new(from_start: u64, to_start: u64, length: u64) -> Self {
        Self {
            from_start,
            from_end: from_start + length,
            to_start,
        }
    }

    fn is_in_range(&self, value: u64) -> bool {
        value >= self.from_start && value < self.from_end
    }

    fn convert(&self, value: u64) -> u64 {
        let offset = value - self.from_start;
        return self.to_start + offset;
    }

    fn has_union_with_range(&self, range: std::ops::Range<u64>) -> bool {
        return range.start < self.from_end && range.end > self.from_start;
    }

    fn convert_range(&self, range: Range<u64>) -> (Range<u64>, Vec<Range<u64>>) {
        let union_start = range.start.max(self.from_start);
        let union_end = range.end.min(self.from_end);
        let mut everything_else = vec![];
        if range.start < self.from_start {
            let left = range.start..self.from_start;
            everything_else.push(left);
        }
        if range.end > self.from_end {
            let right = self.from_end..range.end;
            everything_else.push(right);
        }

        return (
            self.convert(union_start)..self.convert(union_end),
            everything_else,
        );
    }
}
