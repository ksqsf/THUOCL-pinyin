#!/bin/bash

set -u
set -e

dictionaries=(
    IT
    animal
    caijing
    car
    chengyu
    diming
    food
    law
    lishimingren
    medical
    poem
)

doit(){
    echo "dictionary $1: started"
    python3 process.py "data/THUOCL_$1.txt" "output/$1.csv"
    echo "dictionary $1: finished"
}

for dictionary in "${dictionaries[@]}"
do
    doit $dictionary &
done

wait
