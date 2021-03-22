#!/bin/bash
rm -rf out
time python3 dna.py < dna.in > out
printf "\ndiff:\n"
diff -y --suppress-common-lines out dna.out
printf "\nDone.\n"
