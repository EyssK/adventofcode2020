use std::fs::File;
use std::io::{prelude::*, BufReader};
use std::collections::{HashSet, HashMap};

fn count_yes(group: &String) -> usize {
    // remove doublons
    let set : HashSet<char> = group.chars().collect();
    // need to remove '\n'
    set.len() - 1
}

fn count_all_yes(group: &String) -> usize {
    // We count elements that are present the "number of line" times.
    let mut sets = HashMap::new();
    let mut peoplenb = 0;
    let mut count = 0;
    for line in group.lines() {
        peoplenb += 1;
        for ch in line.chars() {
            let counter = sets.entry(ch).or_insert(0);
            *counter += 1; 
        }
    }
    for (_,val) in sets.iter() {
        if val == &peoplenb {
            count += 1;
        }
    }
    count
}

fn get_groups(input: &String) -> Vec<String> {
    let mut groups = Vec::new();
    let mut group = String::new();
    let file = File::open(input).expect("Error opening file");

    for line in BufReader::new(file).lines() {
        let line = line.expect("Bufreader.lines error") ;
        if line.len() > 0 {
            // BufReader removes the terminal \n
            group.push_str(&(line+ "\n"));
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
    for group in &groups {
        sum_yes += count_yes(&group);
    }
    println!("Part1: {}", sum_yes);

    let mut sum_yes = 0;
    for group in &groups {
        sum_yes += count_all_yes(&group);
    }
    println!("Part2: {}", sum_yes);

    Ok(())
}
