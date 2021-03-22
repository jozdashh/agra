#!/bin/bash
rm -rf out
time python3 xplosives.py < xplosives.in > out
printf "\ndiff:\n"
diff -y out xplosives.out # --suppress-common-lines
printf "\nDone.\n"
