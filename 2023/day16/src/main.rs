use std::thread;
use std::{
    collections::{HashSet, VecDeque},
    vec,
};
const NTHREADS: u32 = 10;
use common::{self, AOCInput};
const DAY: &str = env!("CARGO_PKG_NAME");

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    AOCInput::test(
        r#" .|...\....
            |.-.\.....
            .....|-...
            ........|.
            ..........
            .........\
            ..../.\\..
            .-.-/..|..
            .|....-|.\
            ..//.|...."#,
    )
    .solve(task1)
    .check(46);

    // Solution
    let ans = AOCInput::input(DAY).solve(task1).unwrap();
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test
    AOCInput::test(
        r#" .|...\....
            |.-.\.....
            .....|-...
            ........|.
            ..........
            .........\
            ..../.\\..
            .-.-/..|..
            .|....-|.\
            ..//.|...."#,
    )
    .solve(task2)
    .check(51);

    // Solution
    let ans = AOCInput::input(DAY).solve(task2).unwrap();
    println!("Task 1 solution: {ans}");
}

fn task1(input: Vec<String>) -> i32 {
    solve(&input, Beam::new((0, 0), (1, 0)))
}

fn solve(input: &Vec<String>, start: Beam) -> i32 {
    let mut queue = VecDeque::new();
    queue.push_back(start);
    let mut seen = Vec::new();
    while let Some(beam) = queue.pop_front() {
        if beam.pos.0 < 0 || beam.pos.1 < 0 {
            continue;
        }
        if beam.pos.0 >= input.len() as i32 || beam.pos.1 >= input[0].len() as i32 {
            continue;
        }
        if seen.contains(&beam) {
            continue;
        }
        seen.push(beam);
        let c = input[beam.pos.1 as usize]
            .chars()
            .nth(beam.pos.0 as usize)
            .unwrap();
        if c == '\\' {
            queue.push_back(beam.rotate(1));
            continue;
        }
        if c == '/' {
            queue.push_back(beam.rotate(0));
            continue;
        }
        if beam.dir.0 == 0 {
            if c == '-' {
                let next_two = beam.split();
                queue.push_back(next_two.0);
                queue.push_back(next_two.1);
                continue;
            }
        }
        if beam.dir.1 == 0 {
            if c == '|' {
                let next_two = beam.split();
                queue.push_back(next_two.0);
                queue.push_back(next_two.1);
                continue;
            }
        }
        let next = beam.step();
        queue.push_back(next);
    }
    let positions = seen.iter().map(|b| b.pos).collect::<HashSet<_>>();
    positions.len() as i32
}

fn task2(input: Vec<String>) -> i32 {
    let mut max = 0;
    let possible_starts = get_border(&input);
    let mut children = vec![];
    for x in possible_starts {
        let input_clone = input.clone();
        children.push(thread::spawn(move || solve(&input_clone, x)));
    }
    for child in children {
        let a = child.join();
        if a.as_ref().unwrap() > &max {
            max = a.unwrap();
        }
    }
    max
}

fn get_border(input: &Vec<String>) -> Vec<Beam> {
    let width = input.first().unwrap().len();
    let height: usize = input.len();
    let mut border = vec![];
    for x in 0..width {
        border.push(Beam::new((x as i32, 0), (0, 1)));
        border.push(Beam::new((0, height as i32 - 1), (0, -1)));
    }
    for y in 0..height {
        border.push(Beam::new((0, y as i32), (1, 0)));
        border.push(Beam::new((input.len() as i32 - 1, y as i32), (-1, 0)));
    }
    border
}

#[derive(Debug, Clone, Copy, PartialEq)]
struct Beam {
    pos: (i32, i32),
    dir: (i32, i32),
}

impl Beam {
    fn new(pos: (i32, i32), dir: (i32, i32)) -> Self {
        Self { pos, dir }
    }

    fn step(self) -> Self {
        let (x, y) = self.pos;
        let (dx, dy) = self.dir;
        Self {
            pos: (x + dx, y + dy),
            dir: (dx, dy),
        }
    }

    fn rotate(self, dir: i32) -> Self {
        let (dx, dy) = self.dir;
        let (x, y) = self.pos;
        let (dx1, dy1) = match dir {
            0 => (-dy, -dx),
            1 => (dy, dx),
            _ => panic!("Invalid direction"),
        };
        Self {
            pos: (x + dx1, y + dy1),
            dir: (dx1, dy1),
        }
    }

    fn split(self) -> (Self, Self) {
        (self.rotate(0), self.rotate(1))
    }
}
