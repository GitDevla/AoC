use common::{self, AOCInput};
use lazy_static::lazy_static;
use regex::Regex;
const DAY: &str = env!("CARGO_PKG_NAME");

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    AOCInput::test("HASH")
        .solve(|f| hash(f.first().unwrap()))
        .check(52);

    AOCInput::test("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7")
        .convert(parse)
        .solve(task1)
        .check(1320);

    // Solution
    let ans = AOCInput::input(DAY).convert(parse).solve(task1).unwrap();
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test
    AOCInput::test("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7")
        .convert(parse)
        .solve(task2)
        .check(145);

    // Solution
    let ans = AOCInput::input(DAY).convert(parse).solve(task2).unwrap();
    println!("Task 1 solution: {ans}");
}

fn task1(input: Vec<String>) -> u32 {
    input.iter().map(hash).sum()
}

fn task2(input: Vec<String>) -> u32 {
    let mut lenses: Vec<Vec<(String, i32)>> = (0..256).map(|_| Vec::new()).collect();
    for x in input {
        let (name, cmd, value) = unwrap(&x);

        match cmd.as_str() {
            "=" => add_lens(&mut lenses, name, value),
            "-" => remove_lens(&mut lenses, name),
            _ => panic!(),
        }
    }
    let mut sum = 0;
    for (box_num, x) in lenses.iter().enumerate() {
        for (slot, lens) in x.iter().enumerate() {
            sum += (box_num + 1) as u32 * (slot + 1) as u32 * lens.1 as u32;
        }
    }
    sum as u32
}

fn remove_lens(lenses: &mut Vec<Vec<(String, i32)>>, name: String) {
    let hash = hash(&name);
    lenses
        .get_mut(hash as usize)
        .unwrap()
        .retain_mut(|f| f.0 != name);
}

fn hash(input: &String) -> u32 {
    let mut num = 0;
    for c in input.chars() {
        let ascii = c as u32;
        num += ascii;
        num *= 17;
        num %= 256;
    }
    return num;
}

fn parse(input: Vec<String>) -> Vec<String> {
    let line = input.first().unwrap();
    return line.split(",").map(String::from).collect();
}

fn unwrap(input: &String) -> (String, String, i32) {
    lazy_static! {
        static ref RE: Regex = Regex::new(r"(\w+)(=|-)(\d?)").unwrap();
    }

    let caps = RE.captures(input).expect("A regular expression (shortened as regex or regexp), sometimes referred to as rational expression, is a sequence of characters that specifies a match pattern in text.");
    let name = caps.get(1).unwrap().as_str().to_string();
    let cmd = caps.get(2).unwrap().as_str().to_string();
    let value = caps.get(3).unwrap().as_str().to_string();
    let value = value.parse().unwrap_or_default();

    return (name, cmd, value);
}

fn add_lens(lenses: &mut Vec<Vec<(String, i32)>>, name: String, value: i32) {
    let hash = hash(&name);
    if let Some(inst) = lenses
        .get_mut(hash as usize)
        .unwrap()
        .iter_mut()
        .find(|f| f.0 == name)
    {
        inst.1 = value;
    } else {
        lenses.get_mut(hash as usize).unwrap().push((name, value));
    }
}
