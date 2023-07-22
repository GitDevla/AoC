use common;
const INPUT_FILE: &str = "input/day18.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    let test = r#".#.#.#
...##.
#....#
..#...
#.#..#
####.."#;
    let test: Vec<String> = test.lines().map(String::from).collect();
    let test = parse(test);
    assert_eq!(task1(test, 4), 4);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input = parse(input);

    let ans = task1(input, 100);
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test
    let test = r#".#.#.#
...##.
#....#
..#...
#.#..#
####.."#;
    let test: Vec<String> = test.lines().map(String::from).collect();
    let test = parse(test);
    assert_eq!(task2(test, 5), 17);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input = parse(input);

    let ans = task2(input, 100);
    println!("Task 2 solution: {ans}");
}

fn task1(input: Vec<Vec<bool>>, turns: usize) -> usize {
    let mut map = input;
    play_game_of_life(&mut map, turns, false);
    return get_number_of_lights(map);
}

fn task2(input: Vec<Vec<bool>>, turns: usize) -> usize {
    let mut map = input;
    play_game_of_life(&mut map, turns, true);
    return get_number_of_lights(map);
}

fn get_number_of_lights(input: Vec<Vec<bool>>) -> usize {
    input.iter().flat_map(|f| f.iter().filter(|c| **c)).count()
}

fn play_game_of_life(input: &mut Vec<Vec<bool>>, turns: usize, fix_corners: bool) -> () {
    if turns == 0 {
        return;
    }

    let height = input.len();
    let width = input[0].len();
    let clone: Vec<Vec<bool>> = input.clone();

    if fix_corners {
        input[0][0] = true;
        input[height - 1][0] = true;
        input[0][width - 1] = true;
        input[height - 1][width - 1] = true;
    }
    for (y, row) in input.iter_mut().enumerate() {
        for (x, bulb) in row.iter_mut().enumerate() {
            let neighbour = number_of_neigh(&clone, y, x);
            if *bulb {
                if neighbour != 2 && neighbour != 3 {
                    *bulb = false;
                }
            } else {
                if neighbour == 3 {
                    *bulb = true;
                }
            }
        }
    }
    if fix_corners {
        input[0][0] = true;
        input[height - 1][0] = true;
        input[0][width - 1] = true;
        input[height - 1][width - 1] = true;
    }
    play_game_of_life(input, turns - 1, fix_corners)
}

fn number_of_neigh(map: &Vec<Vec<bool>>, y: usize, x: usize) -> u8 {
    let height: i8 = map.len() as i8;
    let width: i8 = map[0].len() as i8;
    let mut count = 0;

    for dy in -1..=1_i8 {
        for dx in -1..=1_i8 {
            let ny = y as i8 + dy;
            let nx = x as i8 + dx;

            if dy == 0 && dx == 0 {
                continue;
            }

            if ny >= 0 && ny < height && nx >= 0 && nx < width {
                if map[ny as usize][nx as usize] {
                    count += 1;
                }
            }
        }
    }

    return count;
}

fn parse(input: Vec<String>) -> Vec<Vec<bool>> {
    let mut map = vec![vec![false; input.len()]; input.len()];
    for (y, l) in input.iter().enumerate() {
        for (x, c) in l.chars().enumerate() {
            map[y][x] = c == '#';
        }
    }
    return map;
}
