#!/bin/bash
rm -rf out
time python3 chimp.py < chimp.in > out
printf "\ndiff:\n"
diff -y out chimp.out # --suppress-common-lines
printf "\nDone.\n"
