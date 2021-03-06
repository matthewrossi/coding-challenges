#!/bin/bash

test=$1
reps=$2

for run in $(seq $reps)
do
    python3 randomize.py < datasets/$test.in > datasets/$test$run.out datasets/$test$(($run-1)).out
done
