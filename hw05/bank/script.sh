#!/bin/bash
rm -rf out
time python3 bank.py < bank.in > out
printf "\ndiff:\n"
diff -y --suppress-common-lines out bank.out
printf "\nDone.\n"
