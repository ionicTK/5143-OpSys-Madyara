import sys
import os


def man(args):
    if len(args) == 1:
        print("needs more arguments!")
    elif len(args) > 1:
        if args[1] == 'ls':
            print("Command 'ls' lists files and directories")
        elif args[1] == 'mkdir':
            print("Command 'mkdir' makes a directory")
        elif args[1] == 'cd':
            print("Command 'cd' changes to the named directory")
        elif args[1] == 'cp':
            print("Command 'cp' copies one file and renames it as another")
        elif args[1] == 'pwd':
            print("Command 'pwd' prints a working directory")
        elif args[1] == 'mv':
            print("Command 'mv' moves a file or renames it")
        elif args[1] == 'rm':
            print("Command 'rm' removes a file")
        elif args[1] == 'rmdir':
            print("Command 'rmdir' removes a directory")
        elif args[1] == 'cat':
            print("Command 'cat' displays files entered")
        elif args[1] == 'less':
            print("Command 'less' displays a file one page at a time")
        elif args[1] == 'head':
            print("Command 'head' displays the first few lines of a file")
        elif args[1] == 'tail':
            print("Command 'tail' displays the last few lines of a file")
        elif args[1] == 'grep':
            print(
                "Command 'grep' searches a file (or files) for keywords and prints lines where they are found")
        elif args[1] == 'wc':
            print("Command 'wc' counts number of lines/words/characters in a file")
        elif args[1] == 'sort':
            print("Command 'sort' sorts data")
        elif args[1] == 'history':
            print("Command 'history' shows a history of all your commands")
        elif args[1] == '!x':
            print(
                "Command '!x' loads command 'x' from your history so you can run it again")
        else:
            print("Command doesn't exist")
