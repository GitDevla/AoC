#! /bin/bash
source session
DAY=$(date +%d)
day=$(echo $DAY | sed 's/^0*//')
YEAR=$(date +%Y)

function download_latest_input() {
    if [[ -f "input/day$DAY.txt" ]]; then
        echo "Input already downloaded"
        return
    fi

    local day=$(echo $DAY | sed 's/^0*//')
    echo "Downloading input for day $day"
    local input=$(curl -s "https://adventofcode.com/$YEAR/day/$day/input" \
        -H "cookie: session=$AOC_SESSION")
    
    echo -n "$input" > "input/day$DAY.txt"
}

function create_new_project(){
    if [[ -d "day$DAY" ]]; then
        echo "Project already exists"
        return
    fi
    echo "Creating new project for day $DAY"
    cargo new day$DAY --bin

    
    cp common/src/blank.rs day$DAY/src/main.rs
    sed -i "s/dayXX.txt/day$DAY.txt/g" day$DAY/src/main.rs
    echo 'common = {path="../common"}' >> day$DAY/Cargo.toml
    sed -i '$ d' Cargo.toml
    echo -e "\t\"day$DAY\",\n]" >> Cargo.toml
}


download_latest_input
create_new_project
echo "https://adventofcode.com/$YEAR/day/$day"
if [[ $(uname -r) == *WSL* ]]; then
    explorer.exe "https://adventofcode.com/$YEAR/day/$day"
fi