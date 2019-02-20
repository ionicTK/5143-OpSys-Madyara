import sys
import os
import shutil


def mv(args):
    if len(args) == 1:
        print("need more arguments!")
    elif len(args) > 1:
        file1 = args[1]
        file2 = args[2]
        shutil.move(file1, file2)
