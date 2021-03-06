#!/bin/bash

echo "Program: $1";

for i in a b c d e
do
    python3 $1 $i < datasets/$i.in > datasets/$i.out &
done
wait
