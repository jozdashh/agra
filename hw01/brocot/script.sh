#!/bin/bash
rm -rf out
time python3 brocot.py < brocot.in > out
printf "\ndiff:\n"
diff brocot.out out
printf "\nDone.\n"
