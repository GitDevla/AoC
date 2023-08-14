mod entity;
use spell::{get_spellbook, Effect};
use std::collections::VecDeque;

mod spell;
use common;

use crate::entity::Entity;
const INPUT_FILE: &str = "input/day22.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    let player = Entity::new(10, 0, 0, 250);
    let enemy = Entity::new(13, 8, 0, 0);
    assert_eq!(task1(player, enemy), 226);

    let player = Entity::new(10, 0, 0, 250);
    let enemy = Entity::new(14, 8, 0, 0);
    assert_eq!(task1(player, enemy), 641);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input = parse(input);

    let player = Entity::new(50, 0, 0, 500);
    let ans = task1(player, input);
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input = parse(input);

    let player = Entity::new(50, 0, 0, 500);
    let ans = task2(player, input);
    println!("Task 2 solution: {ans}");
}

fn task1(player: Entity, boss: Entity) -> i32 {
    solve(player, boss, false).unwrap()
}

fn task2(player: Entity, boss: Entity) -> i32 {
    solve(player, boss, true).unwrap()
}

#[derive(Clone)]
struct State {
    spent_mana: i32,
    player: Entity,
    enemy: Entity,
    dots: Vec<Effect>,
}

fn solve(player: Entity, enemy: Entity, player_poisoned: bool) -> Option<i32> {
    let start = State {
        spent_mana: 0,
        player: player.clone(),
        enemy: enemy.clone(),
        dots: vec![],
    };
    let spellbook = get_spellbook();
    let mut queue = VecDeque::new();
    queue.push_back(start);
    while let Some(state) = queue.pop_front() {
        let mut state = state;
        if player_poisoned {
            state.player.hp -= 1;
        }
        if state.player.is_dead() {
            continue;
        }
        proc_dots(&mut state);
        for spell in spellbook.iter() {
            let mut next_state = state.clone();
            if next_state.player.mana < spell.cost {
                continue;
            }

            next_state.spent_mana += spell.cost;
            let effect = spell.cast(&mut next_state.player, &mut next_state.enemy);
            if let Some(effect) = effect {
                if state.dots.iter().map(|f| f.id).any(|i| i == effect.id) {
                    continue; // already casted
                } else {
                    next_state.dots.push(effect.clone());
                }
            }

            proc_dots(&mut next_state);

            if next_state.enemy.is_dead() {
                return Some(next_state.spent_mana);
            }

            next_state.player.hp -= std::cmp::max(1, enemy.atk - next_state.player.armor);

            queue.push_back(next_state);
        }
    }
    return None;
}

fn proc_dots(state: &mut State) {
    let mut arm = 0;
    for effect in state.dots.iter_mut() {
        state.enemy.hp -= effect.damage;
        state.player.mana += effect.mana;
        arm += effect.armor;
        effect.turns -= 1;
    }
    state.dots = state
        .dots
        .iter()
        .filter(|e| e.turns > 0)
        .map(|f| f.clone())
        .collect();
    state.player.armor = arm;
}

fn parse(input: Vec<String>) -> Entity {
    let hp = input[0].split(": ").nth(1).unwrap().parse().unwrap();
    let atk = input[1].split(": ").nth(1).unwrap().parse().unwrap();
    return Entity::new(hp, atk, 0, 0);
}
