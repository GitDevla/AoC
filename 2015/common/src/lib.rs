use std::fs::read_to_string;

pub fn read_file(filename: &str) -> Vec<String> {
    let file = read_to_string(filename).expect("Kek");
    let conents = file.lines().map(String::from).collect();
    return conents;
}
