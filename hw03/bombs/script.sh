#!/bin/bash
rm -rf out
time python3 bombs.py < bombs.in > out
printf "\ndiff:\n"
diff -y out bombs.out #--suppress-common-lines
printf "\nDone.\n"
