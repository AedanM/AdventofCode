use std::collections::HashMap;
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
    let mut scores = HashMap::new();
    scores.insert("A", 1);
    scores.insert("B", 2);
    scores.insert("C", 3);
    scores.insert("X", 1);
    scores.insert("Y", 2);
    scores.insert("Z", 3);

    let content = get_input_string();
    let mut total_score = 0;
    for line in content.lines() {
        let mut split = line.split(" ");
        let player: &str = split.next().unwrap_or("");
        let other: &str = split.next().unwrap_or("");

        let player_score = scores[player];
        let other_score = scores[other];

        let won: bool = player_score > other_score || (player_score == 1 && other_score == 3);
        let draw: bool = player_score == other_score;

        total_score += player_score;
        if won {
            total_score += 6
        }
        if draw {
            total_score += 3;
        }

        print!("{} -> {}\n", player_score, other_score)
    }
    print!("Total: {}", total_score);
}
