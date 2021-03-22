#!/bin/bash
rm -rf out
time python3 war.py < war.in > out
printf "\ndiff:\n"
diff -y --suppress-common-lines out war.out
printf "\nDone.\n"
