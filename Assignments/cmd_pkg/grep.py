import sys

"""
Params:
  pattern [string] - search pattern
  file(s) [string] - name of file or files (directory or wildcard pattern)
"""


def grep(args):
    colours = {"default": "",
               "blue":   "\x1b[01;34m",
               "cyan":   "\x1b[01;36m",
               "green":  "\x1b[01;32m",
               "red":    "\x1b[01;05;37;41m"}

    noColor = "\x1b[00m"
    if len(args) == 1:
        print("needs more arguments!")
    elif len(args) > 1:

        pattern = args[1]
        filename = args[2]
        # creates a list with one line per entry
        lines = open(filename).readlines()
        for line in lines:
            location = line.find(pattern)
            if location > 0:
                print(line[:location])
                print(colours['red']+pattern+noColor)
                print(line[location+len(pattern):])

#read line by line, split line by space
# then search for the word 
# def greperror():
#     pass

# def grepusage():
#     print("Usage: grep pattern file[s]...")
