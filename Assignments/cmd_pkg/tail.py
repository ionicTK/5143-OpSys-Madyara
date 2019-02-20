import sys
import os


def tail(args):
    if len(args) == 1:
        print("needs more arguments!")
    elif len(args) > 1:
        for i in range(1, len(args)):
            with open(args[1]) as f:
                lines = f.readlines()

            print(lines[-3])
