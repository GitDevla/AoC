#[derive(Clone)]
pub struct Entity {
    pub hp: i32,
    pub atk: i32,
    pub armor: i32,
    pub mana: i32,
}

impl Entity {
    pub fn new(hp: i32, atk: i32, armor: i32, mana: i32) -> Self {
        Self {
            hp,
            atk,
            armor,
            mana,
        }
    }

    pub fn is_dead(&self) -> bool {
        self.hp <= 0
    }
}
