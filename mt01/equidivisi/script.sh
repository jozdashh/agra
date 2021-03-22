#!/bin/bash
rm -rf out
time python3 equidivisi.py < equidivisi.in > out
printf "\ndiff:\n"
diff -y out equidivisi.out # --suppress-common-lines
printf "\nDone.\n"
