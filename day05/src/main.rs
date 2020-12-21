use std::fs::File;
use std::io::{prelude::*, BufReader};

fn get_id(line: String) -> u32 {
    let mut row_max : u32 = 127;
    let mut row_min : u32 = 0;
    let mut col_max : u32 = 7;
    let mut col_min : u32 = 0;
    for letter in line.chars() {
        match letter {
            'F' => row_max = row_max - (row_max - row_min + 1)/ 2,
            'B' => row_min = row_min + (row_max - row_min + 1)/ 2,
            'L' => col_max = col_max - (col_max - col_min + 1)/ 2,
            'R' => col_min = col_min + (col_max - col_min + 1)/ 2,
            _ => break,
        }
    }
    row_min *8 + col_min
}

fn scan_empty_seat(mut ids: Vec<u32>) -> u32 {
    ids.sort_unstable();
    for idx in 0..(ids.len()-2) {
        if ids[idx]+1 != ids[idx+1] {
            return ids[idx]+1
        }
    }
    0   
}

fn main() -> Result<(), std::io::Error> {
    let file = File::open("input")?;
    let mut id_max = 0;
    let mut ids = Vec::new();
    for line in BufReader::new(file).lines() {
        let line = line.expect("Bufreader.lines error");
        let id = get_id(line);
        ids.push(id);
        if id > id_max {
            id_max = id;
        }
    }
    println!("part1: {}", id_max);

    let myseat = scan_empty_seat(ids);
    println!("part2: {}", myseat);
    Ok(())
}
