#!/bin/sh

for i in {0..9}; do
  python make_folds.py $i
  echo "Folds ${i}"
done