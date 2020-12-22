use std::fs::File;
use std::io::{prelude::*, BufReader};
use std::collections::HashSet;

fn count_yes(group: &String) -> usize {
    // println!("{}", group);
    let set : HashSet<char> = group.chars().collect();
    set.len()
}

fn get_groups(input: &String) -> Vec<String> {
    let mut groups = Vec::new();
    let mut group = String::new();
    let file = File::open(input).expect("Error opening file");

    //let mut lines = Vec::new();
    //lines.push("abc");
    //lines.push("");
    //lines.push("a");
    //lines.push("b");
    //lines.push("c");
    //lines.push("");
    //lines.push("ab");
    //lines.push("ac");
    //lines.push("");
    //lines.push("a");
    //lines.push("a");
    //lines.push("a");
    //lines.push("a");
    //lines.push("");
    //lines.push("b");

    for line in BufReader::new(file).lines() {
    //for line in lines {
        let line = line.expect("Bufreader.lines error");
        if line.len() > 0 {
            group.push_str(&line);
        }
        else {
            groups.push(group);
            group = String::new();
        }
    }
    groups.push(group);
    groups
}

fn main() -> Result<(), std::io::Error> {

    let groups = get_groups(&"input".to_string());
    println!("group nb: {}", groups.len());
    let mut sum_yes = 0;
    for group in groups {
        sum_yes += count_yes(&group);
    }
    println!("Part1: {}", sum_yes);

    Ok(())
}
