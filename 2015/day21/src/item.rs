use regex::Regex;

#[derive(Clone, Debug)]

pub struct Item {
    pub category: Category,
    pub name: String,
    pub cost: i32,
    pub atk: i32,
    pub def: i32,
}

impl Item {
    pub fn new(category: Category, name: String, cost: i32, atk: i32, def: i32) -> Self {
        Self {
            category,
            name,
            cost,
            atk,
            def,
        }
    }
}

#[derive(Clone, Debug, PartialEq)]
pub enum Category {
    Weapon,
    Armor,
    Ring,
}

pub fn generate_shop() -> Vec<Item> {
    let text = r#"
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3"#;
    let re = Regex::new(r"(\w+(\s\+\d+)?)\s+(\d+)\s+(\d+)\s+(\d+)").unwrap();
    let mut current_category: Option<Category> = None;
    let mut shop: Vec<Item> = vec![];
    for line in text.lines().skip(1) {
        if let Some(capture) = re.captures(line) {
            let name = capture.get(1).map_or("", |m| m.as_str());
            let cost: i32 = capture.get(3).map_or("", |m| m.as_str()).parse().unwrap();
            let atk: i32 = capture.get(4).map_or("", |m| m.as_str()).parse().unwrap();
            let def: i32 = capture.get(5).map_or("", |m| m.as_str()).parse().unwrap();
            let cat = current_category.as_ref().unwrap();
            shop.push(Item::new(cat.clone(), name.to_string(), cost, atk, def))
        } else {
            if line.is_empty() {
                continue;
            }
            match line.split(" ").nth(0).unwrap() {
                "Weapons:" => current_category = Some(Category::Weapon),
                "Armor:" => current_category = Some(Category::Armor),
                "Rings:" => current_category = Some(Category::Ring),
                _ => panic!("line:{}", line),
            }
        }
    }
    shop.push(Item {
        category: Category::Weapon,
        name: "Nothing".to_string(),
        cost: 0,
        atk: 0,
        def: 0,
    });
    shop.push(Item {
        category: Category::Armor,
        name: "Nothing".to_string(),
        cost: 0,
        atk: 0,
        def: 0,
    });
    shop.push(Item {
        category: Category::Ring,
        name: "Nothing".to_string(),
        cost: 0,
        atk: 0,
        def: 0,
    });
    shop.push(Item {
        category: Category::Ring,
        name: "Nothing2".to_string(),
        cost: 0,
        atk: 0,
        def: 0,
    });
    return shop;
}
