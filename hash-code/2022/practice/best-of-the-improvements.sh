#!/bin/bash

echo "Program: $1";

test=$2
cores=$3

for core in $(seq $cores)
do
    python3 $1 datasets/$test.out <datasets/$test.in 2>&1 >datasets/$test$core.out &
done
wait

best=0
for core in $(seq $cores)
do
    output=$(python3 scorer.py datasets/$test$core.out < datasets/$test.in)
    score=${output:6}
    if [ $score -gt $best ]
    then
        best=$score
        mv datasets/$test$core.out datasets/best_$test.out 
    fi
done

echo "$test: score=$best"
