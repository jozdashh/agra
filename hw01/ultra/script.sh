#!/bin/bash
rm -rf out
time python3 ultra.py < ultra.in > out
printf "\ndiff:\n"
diff out ultra.out
printf "\nDone.\n"
