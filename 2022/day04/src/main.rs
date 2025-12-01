use regex::Regex;
use std::env;
use std::ops::Range;
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

fn range_contains(r1: &Range<usize>, r2: &Range<usize>) -> bool {
    let mut result: bool = false;
    if r1.start >= r2.start && r1.end <= r2.end {
        result = true;
    } else if r2.start >= r1.start && r2.end <= r1.end {
        result = true;
    }
    return result;
}

fn ranges_overlap(r1: &Range<usize>, r2: &Range<usize>) -> bool {
    let mut result: bool = false;
    if r1.start <= r2.end && r1.end >= r2.start {
        result = true;
    }
    return result;
}

fn main() {
    let input = get_input_string();
    let re = Regex::new(r"(\d+)-(\d+),(\d+)-(\d+)$").unwrap();
    let mut overlaps: i32 = 0;
    let mut full_contains: i32 = 0;
    for line in input.lines() {
        if re.captures_iter(line).count() != 1 {
            println!("Invalid line: {}", line);
            continue;
        }
        // TODO THE RANGE BOUNDS SHOULD BE INCLUSIVE
        for (_, [start_1, end_1, start_2, end_2]) in re.captures_iter(line).map(|c| c.extract()) {
            let range_1: Range<usize> =
                (start_1.parse::<usize>().unwrap())..(end_1.parse::<usize>().unwrap());
            let range_2: Range<usize> =
                (start_2.parse::<usize>().unwrap())..(end_2.parse::<usize>().unwrap());
            if range_contains(&range_1, &range_2) {
                full_contains += 1;
            }
            if ranges_overlap(&range_1, &range_2) {
                println!("{} overlaps {}", line, line);
                overlaps += 1;
            }
        }
    }
    println!("Total full contains: {}", full_contains);
    println!("Total overlaps: {}", overlaps);
}
