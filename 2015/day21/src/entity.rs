use crate::item::Item;

#[derive(Clone, Debug)]
pub struct Entity {
    pub hp: i32,
    pub atk: i32,
    pub def: i32,
    pub items: Vec<Item>,
}

impl Entity {
    pub fn new(hp: i32, atk: i32, def: i32) -> Self {
        Self {
            hp,
            atk,
            def,
            items: vec![],
        }
    }

    pub fn attack(&self, enemy: &mut Self) {
        let my_attack: i32 = self.atk + self.items.iter().map(|f| f.atk).sum::<i32>();
        let enemy_def: i32 = enemy.def + enemy.items.iter().map(|f| f.def).sum::<i32>();
        let dmg = my_attack - enemy_def;
        let dmg: i32 = if dmg <= 0 { 1 } else { dmg };
        enemy.hp -= dmg as i32;
    }

    pub fn is_dead(&self) -> bool {
        self.hp <= 0
    }

    pub fn equip(&self, kit: Vec<Item>) -> Self {
        Self {
            atk: self.atk,
            hp: self.hp,
            def: self.def,
            items: kit,
        }
    }
}
