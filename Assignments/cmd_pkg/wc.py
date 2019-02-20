"""
open a file,
count the number of times a spcific word within the file
return result
"""
import sys
import os


def wc(args):
    numLines = 0
    numWords = 0
    numChars = 0
    if len(args) == 1:
        print("needs more arguments!")
    elif len(args) > 1:
        filename = args[1]
        file = open(filename, 'r')
        for line in file:
            wordList = line.split()
            numWords += len(wordList)
            numChars += len(line)
            numLines += 1
        print(numLines, numWords, numChars)
    # elif len(args) == 2:
    elif len(args) == 3:
        if args[2] == '-w':
            print(numWords)
        elif args[2] == '-l':
            print(numLines)
        elif args[2] == '-m':
            print(numChars)
