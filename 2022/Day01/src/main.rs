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

fn main() {
    let content = get_input_string();

    let mut elf_groups: Vec<i32> = Vec::new();
    let mut curr_group: i32 = 0;

    for line in content.lines() {
        if line.trim().is_empty() {
            elf_groups.push(curr_group);
            curr_group = 0;
        } else if line.trim().parse::<i32>().is_ok() {
            curr_group += line.trim().parse::<i32>().unwrap();
        }
    }
    print!("Max calories: {}\n", elf_groups.iter().max().unwrap());
    elf_groups.sort();
    let top3: i32 = elf_groups.iter().rev().take(3).sum();
    print!("Top 3 total: {}\n", top3);
}
