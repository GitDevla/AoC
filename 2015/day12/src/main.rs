use json::JsonValue;

use common;
const INPUT_FILE: &str = "input/day12.txt";

fn main() {
    pt1();
    pt2();
}

fn pt1() {
    // Test
    assert_eq!(task1(&parse(r#"{"a":{"b":4},"c":-1}"#.to_string())), 3);
    assert_eq!(task1(&parse(r#"[-1,{"a":1}]"#.to_string())), 0);

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input: String = input.first().unwrap().to_string();
    let input = parse(input);

    let ans = task1(&input);
    println!("Task 1 solution: {ans}");
}

fn pt2() {
    // Test
    assert_eq!(task2(&parse(r#"[1,{"c":"red","b":2},3]"#.to_string())), 4);
    assert_eq!(
        task2(&parse(r#"{"d":"red","e":[1,2,3,4],"f":5}"#.to_string())),
        0
    );

    // Solution
    let input: Vec<String> = common::read_file(INPUT_FILE);
    let input: String = input.first().unwrap().to_string();
    let input = parse(input);

    let ans = task2(&input);
    println!("Task 2 solution: {ans}");
}

fn task1(js: &JsonValue) -> i32 {
    solve(js, false)
}

fn task2(js: &JsonValue) -> i32 {
    solve(js, true)
}

fn solve(js: &JsonValue, i_hate_the_word_red: bool) -> i32 {
    if js.is_number() {
        return js.as_i32().unwrap();
    }

    let mut add = 0;
    if js.is_object() {
        if i_hate_the_word_red {
            if js
                .entries()
                .filter_map(|(_, v)| v.as_str())
                .any(|v| v == "red")
            {
                return 0;
            }
        }
        js.entries().for_each(|(_, n)| {
            if n.is_number() {
                add += n.as_i32().unwrap();
            } else {
                add += solve(n, i_hate_the_word_red);
            }
        });
    } else if js.is_array() {
        add += js
            .members()
            .fold(0, |acc, x| acc + solve(x, i_hate_the_word_red));
    }

    return add;
}

fn parse(input: String) -> JsonValue {
    return json::parse(&input).unwrap();
}
