use md5;

fn main() {
    assert_eq!(task("abcdef".to_string(), 5), "609043");
    assert_eq!(task("pqrstuv".to_string(), 5), "1048970");

    let file = common::read_file("input/day04.txt");
    let ans = task(file.first().unwrap().to_string(), 5);
    println!("Task 1: {ans}");

    let ans = task(file.first().unwrap().to_string(), 6);
    println!("Task 1: {ans}");
}

fn task(input: String, no_zeros: usize) -> String {
    (0..)
        .find_map(|x| {
            let input_with_suffix = format!("{}{}", input, x);
            let digest = md5::compute(input_with_suffix);
            let hash = format!("{:x}", digest);
            let first_n_chars = &hash[..no_zeros];
            if first_n_chars.chars().all(|c| c == '0') {
                Some(x.to_string())
            } else {
                None
            }
        })
        .unwrap()
}
