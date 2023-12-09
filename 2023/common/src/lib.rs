use std::{fmt::Debug, fs::read_to_string};

pub fn read_file(filename: &str) -> Vec<String> {
    let file = read_to_string(filename).expect("Kek");
    let conents = file.lines().map(String::from).collect();
    return conents;
}

pub fn benchmark(function: fn()) {
    use std::time::Instant;
    let now = Instant::now();

    function();

    let elapsed = now.elapsed();
    println!("Elapsed: {:.2?}", elapsed);
}

pub fn read_task_input_multiline<F, T>(project_name: &str, parse_function: F) -> T
where
    F: Fn(Vec<String>) -> T,
{
    let input_file = format!("input/{}.txt", project_name);
    let file = read_to_string(input_file).expect("Kek");
    let contents: Vec<String> = file.lines().map(String::from).collect();
    parse_function(contents)
}

#[macro_export]
macro_rules! read_task_input {
    ($project_name:ident, $parse_function:ident) => {
        common::read_task_input_multiline($project_name, $parse_function)
    };
    ($project_name:ident) => {
        common::read_task_input_multiline($project_name, |f| f)
    };
}

pub fn read_test_input(text: &str) -> Option<Vec<String>> {
    Some(text.split("\n").map(|s| s.to_string()).collect())
}

pub struct AOCInput<I> {
    value: I,
}
impl<I> AOCInput<I> {
    pub fn new(idk: I) -> AOCInput<I> {
        AOCInput { value: idk }
    }

    pub fn solve<F, O>(self, f: F) -> AOCInput<O>
    where
        F: FnOnce(I) -> O,
    {
        AOCInput::new(f(self.value))
    }

    pub fn unwrap(self) -> I {
        self.value
    }
}

impl<I: PartialEq + Debug> AOCInput<I> {
    pub fn check(self, expected: I) {
        let expected = AOCInput::new(expected);
        assert_eq!(self.value, expected.value);
    }
}

impl AOCInput<Vec<String>> {
    pub fn test(test_input: &str) -> AOCInput<Vec<String>> {
        let test_input: Vec<String> = test_input
            .split("\n")
            .map(|s| s.trim_start().to_string())
            .collect();
        AOCInput::new(test_input)
    }

    pub fn input(project_name: &str) -> AOCInput<Vec<String>> {
        let input_file = format!("input/{}.txt", project_name);
        let file = read_to_string(input_file).expect("Kek");
        let contents: Vec<String> = file.lines().map(String::from).collect();
        AOCInput::new(contents)
    }

    pub fn convert<B, F>(self, f: F) -> AOCInput<B>
    where
        F: FnOnce(Vec<String>) -> B,
    {
        AOCInput::new(f(self.value))
    }
}
