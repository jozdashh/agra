#!/bin/bash
rm -rf out
time python3 interval.py < interval.in > out
printf "\ndiff:\n"
diff -y --suppress-common-lines out interval.out
printf "\nDone.\n"
