import os
import errno


def cd(args):
    if len(args) == 1:
        print("needs more arguments!")
    elif len(args) == 2:
        newDir = args[1]

        try:
            if newDir == '~':
                os.chdir(os.path.expanduser(newDir))
            else:
                os.chdir(newDir)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
