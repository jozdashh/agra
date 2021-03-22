#!/bin/bash
rm -rf out
time python3 bill.py < bill.in > out
printf "\ndiff:\n"
diff -y --suppress-common-lines out bill.out
printf "\nDone.\n"
