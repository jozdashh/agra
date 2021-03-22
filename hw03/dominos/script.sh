#!/bin/bash
rm -rf out
time python3 dominos.py < dominos.in > out
printf "\ndiff:\n"
diff -y out dominos.out #--suppress-common-lines
printf "\nDone.\n"
