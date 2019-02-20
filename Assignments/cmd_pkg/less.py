
import sys
import os
from itertools import islice


def less(args):
    if len(args) == 1:
        print("needs more arguments!")
    elif len(args) == 2:
        page_lines = 20
        with open(args[1], 'r') as input_file:
            while input_file:
                lines_cache = islice(input_file, page_lines)
                for lines in lines_cache:
                    print(lines)

            # count += 1
            # if count == 20:
            #     input("Hit enter to go to next page ")
            #     os.system('clear')
