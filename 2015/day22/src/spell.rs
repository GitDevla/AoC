use crate::entity::Entity;

#[derive(Clone, Debug)]
pub struct Effect {
    pub id: i32,
    pub turns: i32,
    pub armor: i32,
    pub damage: i32,
    pub mana: i32,
}

impl Effect {
    fn new(id: i32, turns: i32, armor: i32, damage: i32, mana: i32) -> Self {
        Self {
            id,
            turns,
            armor,
            damage,
            mana,
        }
    }
}

pub struct Spell {
    pub name: String,
    pub cost: i32,
    pub damage: i32,
    pub heal: i32,
    pub effect_applied: Option<Effect>,
}

impl Spell {
    fn new(name: &str, cost: i32, damage: i32, heal: i32, effect_applied: Option<Effect>) -> Self {
        Self {
            name: name.to_string(),
            cost,
            damage,
            heal,
            effect_applied,
        }
    }

    pub fn cast(&self, caster: &mut Entity, target: &mut Entity) -> &Option<Effect> {
        caster.mana -= self.cost;
        target.hp -= self.damage;
        caster.hp += self.heal;
        return &self.effect_applied;
    }
}

pub fn get_spellbook() -> [Spell; 5] {
    [
        // Spell::new("AFK", 0, 0, 0, None),
        Spell::new("Magic Missile", 53, 4, 0, None),
        Spell::new("Drain", 73, 2, 2, None),
        Spell::new("Shield", 113, 0, 0, Some(Effect::new(1, 6, 7, 0, 0))),
        Spell::new("Poison", 173, 0, 0, Some(Effect::new(2, 6, 0, 3, 0))),
        Spell::new("Recharge", 229, 0, 0, Some(Effect::new(3, 5, 0, 0, 101))),
    ]
}
