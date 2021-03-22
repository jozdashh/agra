#!/bin/bash
rm -rf out
time python3 knight.py < knight.in > out
printf "\ndiff:\n"
diff -y --suppress-common-lines out knight.out
printf "\nDone.\n"
