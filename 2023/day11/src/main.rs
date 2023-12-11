use common::{self, AOCInput};
const DAY: &str = env!("CARGO_PKG_NAME");

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    AOCInput::test(
        r#"...#......
            .......#..
            #.........
            ..........
            ......#...
            .#........
            .........#
            ..........
            .......#..
            #...#....."#,
    )
    .convert(parse)
    .solve(task1)
    .check(374);

    // Solution
    let ans = AOCInput::input(DAY).convert(parse).solve(task1).unwrap();
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test
    AOCInput::test(
        r#" ...#......
            .......#..
            #.........
            ..........
            ......#...
            .#........
            .........#
            ..........
            .......#..
            #...#....."#,
    )
    .convert(parse)
    .solve(|f| solve(f, 10))
    .check(1030);

    // Solution
    let ans = AOCInput::input(DAY).convert(parse).solve(task2).unwrap();
    println!("Task 1 solution: {ans}");
}

fn task1(input: Vec<Vec<bool>>) -> u64 {
    solve(input, 2)
}

fn task2(input: Vec<Vec<bool>>) -> u64 {
    solve(input, 1000000)
}

fn solve(input: Vec<Vec<bool>>, distortion: i32) -> u64 {
    let positions: (Vec<usize>, Vec<usize>) = number_of_expansions(&input);
    let galaxies = find_all_galaxies(&input);
    let mut sum: u64 = 0;
    let combinations = get_combinations(&galaxies);
    for (a, b) in combinations {
        let path = calculate_distance(*a, *b);
        let distortion = calculate_distortion(*a, *b, &positions, distortion);
        sum += path as u64 + distortion;
    }
    sum
}

fn get_combinations<T>(arr: &Vec<T>) -> Vec<(&T, &T)> {
    arr.iter()
        .enumerate()
        .flat_map(|(i, a)| arr[i + 1..].iter().map(move |b| (a, b)))
        .collect()
}

fn parse(input: Vec<String>) -> Vec<Vec<bool>> {
    input
        .iter()
        .map(|line| line.chars().map(|c| c == '#').collect())
        .collect()
}

fn number_of_expansions(input: &Vec<Vec<bool>>) -> (Vec<usize>, Vec<usize>) {
    let (mut row_o, mut col_o) = (vec![], vec![]);
    for col in 0..input[0].len() {
        let column: Vec<bool> = input
            .iter() // iterate over rows
            .map(|x| x[col]) // get the icolumn-th element from each row
            .collect();
        if !has_galaxies(&column) {
            col_o.push(col);
        }
    }
    for (idx, row) in input.iter().enumerate() {
        if !has_galaxies(&row) {
            row_o.push(idx);
        }
    }
    (row_o, col_o)
}

fn has_galaxies(input: &Vec<bool>) -> bool {
    input.iter().any(|&b| b)
}

fn calculate_distance(a: (usize, usize), b: (usize, usize)) -> i32 {
    let (x1, y1) = a;
    let (x2, y2) = b;
    ((x1 as i32 - x2 as i32).abs() + (y1 as i32 - y2 as i32).abs()) as i32
}

fn calculate_distortion(
    a: (usize, usize),
    b: (usize, usize),
    expand: &(Vec<usize>, Vec<usize>),
    distort: i32,
) -> u64 {
    let (x1, y1) = a;
    let (x2, y2) = b;
    let xdiff = expand
        .0
        .iter()
        .filter(|f| x1.min(x2) < **f && **f < x1.max(x2))
        .count();

    let ydiff = expand
        .1
        .iter()
        .filter(|f| y1.min(y2) < **f && **f < y1.max(y2))
        .count();

    (xdiff + ydiff) as u64 * (distort - 1) as u64
}

fn find_all_galaxies(map: &Vec<Vec<bool>>) -> Vec<(usize, usize)> {
    let mut galaxies = vec![];
    for (x, row) in map.iter().enumerate() {
        for (y, &cell) in row.iter().enumerate() {
            if cell {
                galaxies.push((x, y));
            }
        }
    }
    galaxies
}
