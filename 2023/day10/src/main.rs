use common::{self, AOCInput};
use std::collections::HashMap;
const DAY: &str = env!("CARGO_PKG_NAME");

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    AOCInput::test(
        r#".....
        .S-7.
        .|.|.
        .L-J.
        ....."#,
    )
    .convert(parse)
    .solve(task1)
    .check(4);
    AOCInput::test(
        r#"..F7.
        .FJ|.
        SJ.L7
        |F--J
        LJ..."#,
    )
    .convert(parse)
    .solve(task1)
    .check(8);

    // Solution
    let ans = AOCInput::input(DAY).convert(parse).solve(task1).unwrap();
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Yeah idk
}

fn task1(input: Vec<Vec<char>>) -> i32 {
    let mut input = input;
    let starting_pos = find_starting_pos(&input);
    let mut curren_pos = starting_pos.clone();
    input[curren_pos.1][curren_pos.0] = substitute_position(&input, curren_pos);
    let mut next_movement =
        convert_possiblemovements_to_delta(possible_movements2(&input, curren_pos));
    if next_movement.len() != 1 {
        next_movement.pop();
    }
    let mut next_movement = next_movement.pop().unwrap();
    let mut steps = 1;
    loop {
        let next_pos = (
            (curren_pos.0 as i32 + next_movement.0) as usize,
            (curren_pos.1 as i32 + next_movement.1) as usize,
        );
        if next_pos == starting_pos {
            return steps / 2;
        }
        curren_pos = next_pos;
        let possible = convert_possiblemovements_to_delta(possible_movements2(&input, curren_pos));
        if possible.len() == 1 {
            next_movement = possible[0];
        } else {
            next_movement = *possible
                .iter()
                .filter(|f| !(f.0 * -1 == next_movement.0 && f.1 * -1 == next_movement.1))
                .next()
                .unwrap();
        }
        steps += 1
    }
}

fn parse(input: Vec<String>) -> Vec<Vec<char>> {
    input.iter().map(|line| line.chars().collect()).collect()
}

fn find_starting_pos(input: &Vec<Vec<char>>) -> (usize, usize) {
    for (y, line) in input.iter().enumerate() {
        for (x, c) in line.iter().enumerate() {
            if *c == 'S' {
                return (x, y);
            }
        }
    }
    panic!("No starting position found")
}

fn possible_movements(input: &Vec<Vec<char>>, pos: (usize, usize)) -> (bool, bool, bool, bool) {
    let connections = Pipe::get_connections();

    let left = if let Some(left) = get(input, pos, (-1, 0)) {
        connections.get(&left).unwrap().right
    } else {
        false
    };
    let right = if let Some(right) = get(input, pos, (1, 0)) {
        connections.get(&right).unwrap().left
    } else {
        false
    };
    let up = if let Some(up) = get(input, pos, (0, -1)) {
        connections.get(&up).unwrap().down
    } else {
        false
    };
    let down = if let Some(down) = get(input, pos, (0, 1)) {
        connections.get(&down).unwrap().up
    } else {
        false
    };
    return (left, right, up, down);
}

fn possible_movements2(input: &Vec<Vec<char>>, pos: (usize, usize)) -> (bool, bool, bool, bool) {
    let connections = Pipe::get_connections();
    let curr = connections.get(&input[pos.1][pos.0]).unwrap();
    let (left, right, up, down) = possible_movements(input, pos);
    return (
        left && curr.left,
        right && curr.right,
        up && curr.up,
        down && curr.down,
    );
}

fn convert_possiblemovements_to_delta(
    possible_movements: (bool, bool, bool, bool),
) -> Vec<(i32, i32)> {
    let mut delta = vec![];
    if possible_movements.0 {
        delta.push((-1, 0));
    }
    if possible_movements.1 {
        delta.push((1, 0));
    }
    if possible_movements.2 {
        delta.push((0, -1));
    }
    if possible_movements.3 {
        delta.push((0, 1));
    }
    delta
}

fn substitute_position(input: &Vec<Vec<char>>, pos: (usize, usize)) -> char {
    let connections = Pipe::get_connections();
    let (left, right, up, down) = possible_movements(input, pos);
    *connections
        .iter()
        .find(|(_, pipe)| {
            pipe.left == left && pipe.right == right && pipe.up == up && pipe.down == down
        })
        .unwrap()
        .0
}

fn get(input: &Vec<Vec<char>>, pos: (usize, usize), offset: (i32, i32)) -> Option<char> {
    let x = pos.0 as i32 + offset.0 as i32;
    let y = pos.1 as i32 + offset.1 as i32;
    if x < 0 || y < 0 {
        return None;
    }
    let x = x as usize;
    let y = y as usize;
    if x >= input[0].len() || y >= input.len() {
        return None;
    }
    Some(input[y as usize][x as usize])
}

#[derive(Debug)]
struct Pipe {
    form: char,
    left: bool,
    right: bool,
    up: bool,
    down: bool,
    alternate: char,
}

impl Pipe {
    fn new(form: char, left: bool, right: bool, up: bool, down: bool, alternate: char) -> Pipe {
        Pipe {
            form,
            left,
            right,
            up,
            down,
            alternate,
        }
    }

    fn get_connections() -> HashMap<char, Pipe> {
        HashMap::from([
            ('-', Pipe::new('-', true, true, false, false, '─')),
            ('|', Pipe::new('|', false, false, true, true, '│')),
            ('L', Pipe::new('L', false, true, true, false, '└')),
            ('J', Pipe::new('J', true, false, true, false, '┘')),
            ('7', Pipe::new('7', true, false, false, true, '┐')),
            ('F', Pipe::new('F', false, true, false, true, '┌')),
            ('.', Pipe::new('.', false, false, false, false, ' ')),
        ])
    }
}
