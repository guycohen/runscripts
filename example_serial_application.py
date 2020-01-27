#!/usr/bin/env python
"""
Simple example of a serial application.
Author: Guy Cohen, Tel Aviv University

"""
from sys import argv
from time import sleep

# Read in the parameter file:
if (len(argv) == 1):
    exec(open('run.param').read())
elif (len(argv) == 2):
    exec(open(argv[1]).read())

# Pretend to do something:
sleep(0.2)

# Output something:
f = open('output.dat', 'w')
f.write(str(A + epsilon * mu) + '\n')

# Print something:
print("Finished running!")
