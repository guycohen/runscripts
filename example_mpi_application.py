#!/usr/bin/env python
"""
Simple example of a parallel application.
Author: Guy Cohen, Tel Aviv University

"""
from mpi4py import MPI
from sys import argv
from time import sleep

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Read in the parameter file:
if rank == 0:
    if (len(argv) == 1):
        execfile('run.param')
    elif (len(argv) == 2):
        execfile(argv[1])
else:
    A = None
    epsilon = None
    mu = None
A = comm.bcast(A, root=0)
epsilon = comm.bcast(epsilon, root=0)
mu = comm.bcast(mu, root=0)


# Pretend to do something:
myval = rank * A + epsilon * mu
vals = comm.gather(myval, root=0)
sleep(0.2)

# Output something:
if rank == 0:
    f = open('output.dat', 'w')
    f.write(str(sum(vals)) + '\n')

# Print something:
print "Finished running on rank %d!" % rank
