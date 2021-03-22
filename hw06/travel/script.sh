#!/bin/bash
rm -rf out
time python3 travel.py < travel.in > out
printf "\ndiff:\n"
diff -y --suppress-common-lines out travel.out
printf "\nDone.\n"
