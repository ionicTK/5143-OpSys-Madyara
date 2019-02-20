import sys
import os
import shutil


def cp(args):
    if len(args) == 1:
        print("need more arguments!")
    elif len(args) > 1:
        file1 = args[1]
        file2 = args[2]
        shutil.copy(file1, file2)
