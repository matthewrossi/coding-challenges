#!/bin/bash

echo "Program: $1";

for i in a b c d e f
do
    python3 $1 $i < datasets/$i.in &
done
wait
