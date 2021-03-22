#!/bin/bash
rm -rf out
time python3 emacs.py < emacs.in > out # < small.in > out
printf "\ndiff:\n"
diff -y --suppress-common-lines out emacs.out # out small.out
printf "\nDone.\n"
