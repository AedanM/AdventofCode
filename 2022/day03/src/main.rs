use std::collections::HashSet;
use std::env;
use std::path::Path;

fn get_input_string() -> String {
    let args: Vec<String> = env::args().collect();

    let sample = Path::new("src/sample.txt");
    let input = Path::new("src/input.txt");
    let mut file: &Path = sample;

    if args.len() > 1 && &args[1] == "sample" {
        println!("Using sample.txt");
    } else {
        println!("Using input.txt");
        file = input;
    }

    let content =
        std::fs::read_to_string(file.to_str().unwrap()).expect("Failed to read input file");
    return content;
}

fn convert_to_priority(value: char) -> i32 {
    let lowercase_range = 97..=122;
    let uppercase_range = 65..=90;
    let mut result = value as i32;
    if uppercase_range.contains(&result) {
        result -= 65;
        result += 27;
    } else if lowercase_range.contains(&result) {
        result -= 97;
        result += 1;
    }

    return result;
}

fn part_1() {
    let input = get_input_string();
    let mut score: i32 = 0;
    for line in input.lines() {
        if line.len() % 2 != 0 {
            println!(
                "Something went wrong, line ({}) has {} elements",
                line,
                line.len()
            )
        }
        let mut matched: HashSet<char> = HashSet::new();
        let section_len = line.len() / 2;
        let second_half = &line[section_len..line.len()];
        for index in 0..section_len {
            let c: char = line.as_bytes()[index] as char;
            if second_half.contains(c) {
                matched.insert(c);
            }
        }
        for value in matched {
            score += convert_to_priority(value);
        }
    }
    println!("Part 1 {}", score);
}

fn part_2() {
    let input = get_input_string();
    let mut score: i32 = 0;
    let lines: Vec<&str> = input.lines().collect();
    for line_num in (0..lines.len()).step_by(3) {
        let line_1 = lines[line_num];
        let line_2 = lines[line_num + 1];
        let line_3 = lines[line_num + 2];
        let mut matched: HashSet<char> = HashSet::new();

        for index in 0..line_1.len() {
            let c: char = line_1.as_bytes()[index] as char;
            if line_2.contains(c) && line_3.contains(c) {
                matched.insert(c);
            }
        }
        for value in matched {
            score += convert_to_priority(value);
        }
    }
    println!("Part 2 {}", score);
}

fn main() {
    part_1();
    part_2();
}
