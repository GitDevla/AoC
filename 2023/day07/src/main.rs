use std::{cmp::Ordering, collections::HashMap, vec};

use common;
const INPUT_FILE: &str = "input/day07.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    let test_input = r#"32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"#;
    let test_input: Vec<String> = test_input.lines().map(|s| s.to_string()).collect();
    let test_input = parse(test_input);
    assert_eq!(task1(test_input), 6440);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input: Vec<Hand> = parse(input);

    let ans = task1(input);
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test
    let test_input = r#"32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"#;
    let test_input: Vec<String> = test_input.lines().map(|s| s.to_string()).collect();
    let test_input = parse(test_input);
    assert_eq!(task2(test_input), 5905);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input: Vec<Hand> = parse(input);

    let ans = task2(input);
    println!("Task 2 solution: {ans}");
}

fn task1(input: Vec<Hand>) -> i32 {
    solve(input, false)
}

fn task2(input: Vec<Hand>) -> i32 {
    solve(input, true)
}

fn solve(input: Vec<Hand>, joker: bool) -> i32 {
    let mut input = input;
    input.sort_by(|a, b| a.compare(b, joker));
    return input
        .iter()
        .rev()
        .enumerate()
        .map(|f| (f.0 as i32 + 1) * f.1.bid)
        .sum::<i32>();
}

#[derive(Debug, Eq, PartialEq)]
struct Hand {
    cards: String,
    bid: i32,
}

impl Hand {
    fn new(cards: String, bid: i32) -> Hand {
        Hand { cards, bid }
    }

    fn get_strenth(&self, joker: bool) -> HandStrength {
        let mut cards = HashMap::new();
        for c in self.cards.chars() {
            let count = cards.entry(c).or_insert(0);
            *count += 1;
        }
        if joker {
            if let Some(number_of_jokers) = cards.get(&'J') {
                let mut new_cards = cards.clone(); // borrow checker is aids
                new_cards.get_mut(&'J').and_then(|f| Some(*f = 0));
                new_cards
                    .iter_mut()
                    .max_by_key(|f| *f.1)
                    .and_then(|f| Some(*f.1 += number_of_jokers));
                cards = new_cards;
            }
        }

        if cards.iter().any(|f| *f.1 >= 5) {
            return HandStrength::FiveOfAKind;
        }
        if cards.iter().any(|f| *f.1 >= 4) {
            return HandStrength::FourOfAKind;
        }
        if cards.iter().any(|f| *f.1 >= 3) && cards.iter().any(|f| *f.1 == 2) {
            return HandStrength::FullHouse;
        }
        if cards.iter().any(|f| *f.1 >= 3) {
            return HandStrength::ThreeOfAKind;
        }
        if cards.iter().filter(|f| *f.1 >= 2).count() >= 2 {
            return HandStrength::TwoPair;
        }
        if cards.iter().any(|f| *f.1 >= 2) {
            return HandStrength::OnePair;
        }

        return HandStrength::HighCard;
    }

    fn get_high_card(&self, other: &Self, joker: bool) -> Ordering {
        let cards = if joker {
            vec![
                'A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J',
            ]
        } else {
            vec![
                'A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2',
            ]
        };

        for (a, b) in self.cards.chars().zip(other.cards.chars()) {
            if cards.iter().position(|&r| r == a) > cards.iter().position(|&r| r == b) {
                return Ordering::Greater;
            } else if cards.iter().position(|&r| r == a) < cards.iter().position(|&r| r == b) {
                return Ordering::Less;
            }
        }
        return Ordering::Equal;
    }

    fn compare(&self, other: &Self, joker: bool) -> std::cmp::Ordering {
        let a = self.get_strenth(joker);
        let b = other.get_strenth(joker);
        if a == b {
            return self.get_high_card(other, joker);
        }
        return a.cmp(&b);
    }
}

fn parse(input: Vec<String>) -> Vec<Hand> {
    let mut hands: Vec<Hand> = Vec::new();
    for line in input {
        let mut line = line.split_whitespace();
        let cards = line.next().unwrap().to_string();
        let bid = line.next().unwrap().parse::<i32>().unwrap();
        hands.push(Hand::new(cards, bid));
    }
    return hands;
}

#[derive(Debug, Eq, Ord, PartialEq, PartialOrd)]
enum HandStrength {
    FiveOfAKind,
    FourOfAKind,
    FullHouse,
    ThreeOfAKind,
    TwoPair,
    OnePair,
    HighCard,
}
