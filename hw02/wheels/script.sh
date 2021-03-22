#!/bin/bash
rm -rf out
time python3 wheels.py < wheels.in > out
printf "\ndiff:\n"
diff -y out wheels.out #--suppress-common-lines
printf "\nDone.\n"
