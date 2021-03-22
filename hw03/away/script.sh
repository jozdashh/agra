#!/bin/bash
rm -rf out
time python3 away.py < away.in > out
printf "\ndiff:\n"
diff -y out away.out # --suppress-common-lines
printf "\nDone.\n"
