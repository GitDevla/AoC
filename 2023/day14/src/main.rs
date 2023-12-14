use std::collections::VecDeque;

use common::{self, AOCInput};
const DAY: &str = env!("CARGO_PKG_NAME");

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    AOCInput::test(
        r#"O....#....
    O.OO#....#
    .....##...
    OO.#O....O
    .O.....O#.
    O.#..O.#.#
    ..O..#O..O
    .......O..
    #....###..
    #OO..#...."#,
    )
    .convert(parse)
    .solve(task1)
    .check(136);

    // Solution
    let ans = AOCInput::input(DAY).convert(parse).solve(task1).unwrap();
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test
    AOCInput::test(
        r#"O....#....
    O.OO#....#
    .....##...
    OO.#O....O
    .O.....O#.
    O.#..O.#.#
    ..O..#O..O
    .......O..
    #....###..
    #OO..#...."#,
    )
    .convert(parse)
    .solve(task2)
    .check(64);

    // Solution
    let ans = AOCInput::input(DAY).convert(parse).solve(task2).unwrap();
    println!("Task 1 solution: {ans}");
}

fn task1(input: Vec<Vec<Material>>) -> i32 {
    let waters = find_all_water(&input);
    let queue: VecDeque<(usize, usize)> = waters.iter().map(|f| *f).collect();
    let new_water = flow_to(queue, &input, (0, -1));
    calculate_weight(new_water, input.len())
}

fn task2(input: Vec<Vec<Material>>) -> i32 {
    const DIRECTIONS: [(i8, i8); 4] = [(0, -1), (-1, 0), (0, 1), (1, 0)];
    let waters: Vec<(usize, usize)> = find_all_water(&input);
    let mut waters: VecDeque<(usize, usize)> = waters.iter().map(|f| *f).collect();
    let mut cache = Vec::new();
    cache.push(hash(&waters));
    let mut limit = 1000000000;
    let mut i = 0;
    while i < limit {
        for dir in DIRECTIONS {
            waters = flow_to(waters, &input, dir);
        }
        if cache.contains(&hash(&waters)) {
            let relative = cache.iter().position(|f| f == &hash(&waters)).unwrap();
            let modulo = i - relative + 1;
            limit = ((limit - i) % modulo) + i;
            cache.clear();
        }
        cache.push(hash(&waters));
        i += 1;
    }

    calculate_weight(waters, input.len())
}

fn hash(waters: &VecDeque<(usize, usize)>) -> i32 {
    let mut hash = 0;
    for (x, y) in waters.iter() {
        hash += x * y;
    }
    hash as i32
}

fn calculate_weight(waters: VecDeque<(usize, usize)>, height: usize) -> i32 {
    waters
        .iter()
        .map(|f| height as i32 - f.1 as i32)
        .sum::<i32>()
}

fn find_all_water(map: &Vec<Vec<Material>>) -> Vec<(usize, usize)> {
    let mut water = Vec::new();
    for (y, row) in map.iter().enumerate() {
        for (x, material) in row.iter().enumerate() {
            if *material == Material::Water {
                water.push((x, y));
            }
        }
    }
    water
}

fn parse(input: Vec<String>) -> Vec<Vec<Material>> {
    let mut map = Vec::new();
    for line in input {
        let mut row = Vec::new();
        for c in line.chars() {
            match c {
                '.' => row.push(Material::Air),
                '#' => row.push(Material::Rock),
                'O' => row.push(Material::Water),
                _ => panic!("Unknown material: {}", c),
            }
        }
        map.push(row);
    }
    map
}

fn flow_to(
    waters: VecDeque<(usize, usize)>,
    map: &Vec<Vec<Material>>,
    direction: (i8, i8),
) -> VecDeque<(usize, usize)> {
    let mut queue = waters;
    let mut new_water = VecDeque::new();
    while let Some((x, y)) = queue.pop_front() {
        let next = (
            (x as i8 + direction.0) as usize,
            (y as i8 + direction.1) as usize,
        );
        let map_next = map.get(next.1).and_then(|f| f.get(next.0));
        if map_next.is_none() {
            new_water.push_back((x, y));
            continue;
        }

        if *map_next.unwrap() == Material::Rock || new_water.contains(&(next.0, next.1)) {
            new_water.push_back((x, y));
            continue;
        }
        if queue.contains(&next) {
            queue.push_back((x, y));
            continue;
        }
        queue.push_back(next);
    }
    new_water
}

#[derive(PartialEq)]
enum Material {
    Air,
    Water, // Round rock
    Rock,  // Flat rock
}
