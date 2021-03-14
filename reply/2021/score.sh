#!/bin/bash

# create dataset scores log
> score.log

for i in a b c d e f
do
    ./score.py $i data/$i.out < data/$i.in 2>&1 | tee -a score.log &
done
wait

# compute total score
awk '{total+=$2} END {printf "TOTAL: %.0f\n", total}' score.log
