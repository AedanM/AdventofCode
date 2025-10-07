use std::path::Path;
use std::env;

fn get_input_string() -> String {
    let args: Vec<String> = env::args().collect();
    
    let sample = Path::new("src/sample.txt");
    let input = Path::new("src/input.txt");
    let mut file: &Path = sample;

    if args.len() > 1  && &args[1] == "sample" {
        println!("Using sample.txt");
    } else {
        println!("Using input.txt");
        file = input;
    }

    let content = std::fs::read_to_string(file.to_str().unwrap()).expect("Failed to read input file");
    return content;
}

fn main() {
    let content = get_input_string();

    let mut elfGroups:Vec<i32> = Vec::new();
    let mut currentGroupTotal: i32 = 0;

    for line in content.lines() {
        if line.trim().is_empty() {
            elfGroups.push(currentGroupTotal);
            currentGroupTotal = 0;
        }
        else if line.trim().parse::<i32>().is_ok() {
            currentGroupTotal += line.trim().parse::<i32>().unwrap();
        }
    }
    print!("Max calories: {}\n", elfGroups.iter().max().unwrap());
    elfGroups.sort();
    let top3: i32 = elfGroups.iter().rev().take(3).sum();
    print!("Top 3 total: {}\n", top3);
}
