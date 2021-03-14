#!/bin/bash

echo "Program: $1";

for i in a b c d e f
do
    ./$1 $i < data/$i.in > data/$i.out &
done
wait
