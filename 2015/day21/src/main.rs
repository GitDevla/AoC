use itertools::iproduct;

mod entity;
mod item;

use common;

use entity::Entity;
use item::{generate_shop, Category, Item};
const INPUT_FILE: &str = "input/day21.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    let player = Entity::new(8, 5, 5);
    let boss = Entity::new(12, 7, 2);
    assert_eq!(simulate_fight(&player, &boss), true);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input = parse(input);
    let ans = task1(input);
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input = parse(input);
    let ans = task2(input);
    println!("Task 2 solution: {ans}");
}

fn task1(enemy: Entity) -> i32 {
    let player = Entity::new(100, 0, 0);
    let possible_loudouts = generate_loadouts();
    let mut won = vec![];
    for kit in possible_loudouts {
        let qeared_up = player.equip(kit.clone());
        if simulate_fight(&qeared_up, &enemy) {
            won.push(kit.iter().map(|i| i.cost).sum::<i32>());
        }
    }
    let best = *won.iter().min().unwrap();
    return best;
}

fn task2(enemy: Entity) -> i32 {
    let player = Entity::new(100, 0, 0);
    let possible_loudouts = generate_loadouts();
    let mut lost = vec![];
    for kit in possible_loudouts {
        let qeared_up = player.equip(kit.clone());
        if !simulate_fight(&qeared_up, &enemy) {
            lost.push(kit.iter().map(|i| i.cost).sum::<i32>());
        }
    }
    let worst = *lost.iter().max().unwrap();
    return worst;
}

fn generate_loadouts() -> Vec<Vec<Item>> {
    let shop = generate_shop();
    let weapons = shop.iter().filter(|i| i.category == Category::Weapon);
    let armour = shop.iter().filter(|i| i.category == Category::Armor);
    let rings = shop.iter().filter(|i| i.category == Category::Ring);
    let combinations: Vec<_> = iproduct!(weapons, armour, rings.clone(), rings)
        .filter(|(_, _, r1, r2)| r1.name != r2.name)
        .map(|(w, a, r1, r2)| vec![w.clone(), a.clone(), r1.clone(), r2.clone()])
        .collect();
    return combinations;
}

fn simulate_fight(player: &Entity, boss: &Entity) -> bool {
    let mut player = player.clone();
    let mut boss = boss.clone();
    loop {
        player.attack(&mut boss);
        if boss.is_dead() {
            return true;
        }
        boss.attack(&mut player);
        if player.is_dead() {
            return false;
        }
    }
}

fn parse(input: Vec<String>) -> Entity {
    let hp: i32 = input[0]
        .split("Hit Points: ")
        .nth(1)
        .unwrap()
        .parse()
        .unwrap();
    let atk: i32 = input[1].split("Damage: ").nth(1).unwrap().parse().unwrap();
    let def: i32 = input[2].split("Armor: ").nth(1).unwrap().parse().unwrap();
    Entity::new(hp, atk, def)
}
