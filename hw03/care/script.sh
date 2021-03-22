#!/bin/bash
rm -rf out
time python3 care.py < care.in > out
printf "\ndiff:\n"
diff -y out care.out #--suppress-common-lines
printf "\nDone.\n"
