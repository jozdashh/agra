#!/bin/bash
rm -rf out
time python3 maze.py < maze.in > out
printf "\ndiff:\n"
diff -y --suppress-common-lines out maze.out
printf "\nDone.\n"
