#!/usr/bin/env python


def history(args):
    file = open("/tempHistory/.history", 'r')
    counter = 0
    for line in file:
        print(str(counter) + " " + line)
        counter += 1
