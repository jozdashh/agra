#!/bin/bash
rm -rf out
time python3 jams.py < jams.in > out
printf "\ndiff:\n"
diff -y out jams.out # --suppress-common-lines
printf "\nDone.\n"
