import sys
import os
import errno


def rm(args):
    if len(args) == 1:
        print("need more arguments!")
    elif len(args) > 1:
        directory = os.path.dirname(os.getcwd())

        try:
            os.rm(args[1])
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
