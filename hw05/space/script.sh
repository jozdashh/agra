#!/bin/bash
rm -rf out
time python3 space.py < space.in > out
printf "\ndiff:\n"
diff -y --suppress-common-lines out space.out
printf "\nDone.\n"
