#!/bin/bash

for i in a b c d e
do
    python3 scorer.py datasets/$i.out $i < datasets/$i.in  &
done
wait
