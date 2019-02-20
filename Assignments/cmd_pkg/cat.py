#!/usr/bin/env python
from subprocess import call


def cat(args):
    if len(args) == 1:
        print("needs more arguments!")
    elif len(args) > 1:
        for i in range(1, len(args)):
            file = open(args[i], 'r')
            for line in file:
                print(line)
