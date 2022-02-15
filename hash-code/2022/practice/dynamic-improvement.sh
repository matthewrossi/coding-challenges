#!/bin/bash

test=$2
reps=$3

for run in $(seq $reps)
do
    python3 $1 < datasets/$test.in > datasets/$test$run.out datasets/$test$(($run-1)).out
done
