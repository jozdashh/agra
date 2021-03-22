#!/bin/bash
rm -rf out
time python3 summing.py < summing.in > out
printf "\ndiff:\n"
diff -y --suppress-common-lines out summing.out
printf "\nDone.\n"
