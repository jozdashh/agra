#!/bin/bash
rm -rf out
time python3 arithmetic.py < arithmetic.in > out
printf "\ndiff:\n"
diff -y out arithmetic.out # --suppress-common-lines
printf "\nDone.\n"
