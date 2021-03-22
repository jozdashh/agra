#!/bin/bash
rm -rf out
time python3 nod.py < nod.in > out
printf "\ndiff:\n"
diff -y --suppress-common-lines out nod.out # --suppress-common-lines
printf "\nDone.\n"
