#!/bin/bash

echo "Program: $1";

test=$2
reps_per_core=$3
cores=$4

for core in $(seq $cores)
do
    ./best.sh $1 $test $reps_per_core $core &
done
wait

best=0
for core in $(seq $cores)
do
    output=$(python3 scorer.py datasets/best_$test$core.out < datasets/$test.in)
    score=${output:6}
    if [ $score -gt $best ]
    then
        best=$score
        mv datasets/best_$test$core.out datasets/best_$test.out 
    fi
done

echo "$test: score=$best"
