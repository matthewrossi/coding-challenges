#!/bin/bash

test=$2
reps=$3
core=$4

best=0
for run in $(seq $reps)
do
    output=$(python3 $1 <datasets/$test.in 2>&1 >datasets/$test$core$run.out)
    score=${output:6}
    if [ $score -gt $best ]
    then
        best=$score
        mv datasets/$test$core$run.out datasets/best_$test$core.out 
    fi
done
