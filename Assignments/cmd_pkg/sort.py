import sys
import os
import errno


def sort(args):
       if len(args) == 1:
       print("need more arguments!")
   elif len(args) > 1:
       filename = args[1]
       file = open(filename, 'r')
       word_list = []
       for line in file:
           word_list.extend(line.split())
       if word_list[0] is int:
           for x in range(0,len(word_list)):
               word_list[x]= int(word_list[x])

       word_list.sort()
       print(word_list)
