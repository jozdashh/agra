#!/bin/bash
rm -rf out
time python3 airports.py < airports.in > out
printf "\ndiff:\n"
diff -y --suppress-common-lines out airports.out
printf "\nDone.\n"
