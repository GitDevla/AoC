use common;
const INPUT_FILE: &str = "input/day14.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    let test = r#"Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."#;
    let test: Vec<String> = test.lines().map(String::from).collect();
    let test = parse(test);
    let test = simulate(test, 1000);
    let comet = test.iter().find(|r| r.name == "Comet").unwrap();
    let dancer = test.iter().find(|r| r.name == "Dancer").unwrap();
    assert_eq!(comet.distance_traveled, 1120);
    assert_eq!(dancer.distance_traveled, 1056);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input = parse(input);

    let ans = task1(input);
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test
    let test = r#"Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."#;
    let test: Vec<String> = test.lines().map(String::from).collect();
    let test = parse(test);
    let test = simulate(test, 1000);
    let comet = test.iter().find(|r| r.name == "Comet").unwrap();
    let dancer = test.iter().find(|r| r.name == "Dancer").unwrap();
    assert_eq!(comet.score, 312);
    assert_eq!(dancer.score, 689);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input = parse(input);

    let ans = task2(input);
    println!("Task 2 solution: {ans}");
}

fn task1(input: Vec<Reindeer>) -> u32 {
    let reindeers = simulate(input, 2503);
    return reindeers
        .iter()
        .max_by(|p, n| p.distance_traveled.cmp(&n.distance_traveled))
        .unwrap()
        .distance_traveled;
}

fn task2(input: Vec<Reindeer>) -> u16 {
    let reindeers = simulate(input, 2503);
    return reindeers
        .iter()
        .max_by(|p, n| p.score.cmp(&n.score))
        .unwrap()
        .score;
}

fn simulate(reindeers: Vec<Reindeer>, seconds: u16) -> Vec<Reindeer> {
    let mut reindeers = reindeers;
    for x in 0..seconds {
        for r in reindeers.iter_mut() {
            Reindeer::step(r);
        }
        let current_best = reindeers
            .iter()
            .max_by(|p, n| p.distance_traveled.cmp(&n.distance_traveled))
            .unwrap()
            .distance_traveled;
        for r in reindeers
            .iter_mut()
            .filter(|r| r.distance_traveled == current_best)
        {
            r.score += 1;
        }
    }
    return reindeers;
}

fn parse(input: Vec<String>) -> Vec<Reindeer> {
    let mut reindeers: Vec<Reindeer> = vec![];
    for l in input {
        let split: Vec<&str> = l.split(" seconds, but then must rest for ").collect();
        let recovery: u8 = split[1].trim_end_matches(" seconds.").parse().unwrap();
        let split: Vec<&str> = split[0].split(" km/s for ").collect();
        let fly_for: u8 = split[1].parse().unwrap();
        let split: Vec<&str> = split[0].split(" can fly ").collect();
        let name: String = split[0].to_string();
        let speed: u8 = split[1].parse().unwrap();
        let r = Reindeer::new(name, speed, fly_for, recovery);
        reindeers.push(r);
    }
    return reindeers;
}
#[derive(Debug)]
struct Reindeer {
    name: String,
    speed: u8,
    can_fly_for: u8,
    recovery_time: u8,

    timer: u16,
    is_recovering: bool,
    distance_traveled: u32,
    score: u16,
}

impl Reindeer {
    fn new(name: String, speed: u8, can_fly_for: u8, recovery_time: u8) -> Reindeer {
        Reindeer {
            name,
            speed,
            can_fly_for,
            recovery_time,
            timer: 0,
            is_recovering: false,
            distance_traveled: 0,
            score: 0,
        }
    }

    fn step(&mut self) {
        self.timer += 1;
        if self.is_recovering {
            if self.timer >= self.recovery_time as u16 {
                self.timer = 0;
                self.is_recovering = false;
            }
        } else {
            if self.timer >= self.can_fly_for as u16 {
                self.timer = 0;
                self.is_recovering = true;
            }
            self.distance_traveled += self.speed as u32;
        }
    }
}
