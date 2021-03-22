#!/bin/bash
rm -rf out
time python3 order.py < order.in > out
printf "\ndiff:\n"
diff -y out order.out # --suppress-common-lines
printf "\nDone.\n"
