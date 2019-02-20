
from cmd_pkg import commands
import threading
import sys
# import readchar  # from https://pypi.org/project/readchar/
# from subprocess import call  # for demo purposes only


def run_command(cmd, args=None, flags=None):
    runBG = False
    if args[-1] == '&':
        runBG = True
        args.pop()

    if args:
        c = threading.Thread(target=cmd, args=(args,))
    else:
        c = threading.Thread(target=cmd)
    c.start()
    if not runBG:
        c.join()


if __name__ == '__main__':
    # at the start of the shell we initialize variables and prepare history
    defaultStdout = sys.stdout  # save default stdout for later use
    doPipe = False  # boolean to check if pipe is being run during this round
    nextCmd = ""                # second cmd for the pipe

    # open file to read previous history.
    # make a list and append all the lines to the history
    file = open("/tempHistory/.history", 'r')
    history = []
    for line in file:
        history.append(line)

    # while running commands
    #
    while True:
        cmd = ""  # keep out of scope of the if statement
        if doPipe == False:  # if we don't have a pipe this round, run as normal
            cmd = input('% ')
            try:
                # do exception handling for the history and !x
                file = open("/tempHistory/.history", 'a')
                file.write(cmd + "\n")
                history.append(cmd)
                if len(cmd) > 0:  # if you have any commands,
                    if "!" in cmd:  # 1st char of command is "!"
                        cmd = cmd.strip(" ")
                        cmd = history[int(cmd.strip("!"))]
            except:
                print("error!")
        # when pipe is true, result of pipe[0] is executed with pipe[1] as
        # singular command
        if doPipe == True:
            cmd = nextCmd + " .temp"
            doPipe = False
            sys.stdout = defaultStdout

        # split the command with a pipe
        pipe = cmd.split("|")
        if len(pipe) > 1:
            cmd = pipe[0]
            # redirect first cmd output to a file
            sys.stdout = open(".temp", "w+")
            doPipe = True  # because pipe is confirmed,
            nextCmd = pipe[1]  # pipe execution is done in the next round

        # commands split to
        cmd = cmd.split()
        # if redirect operator is in command, redirect output into the specified file
        if ">" in cmd:
            sys.stdout = open(cmd[-1], "w+")
            cmd.pop()
            cmd.pop()

# Run the rest of the commands here
        if len(cmd) > 0:
            if cmd[0] == 'ls':
                run_command(commands.ls.ls, cmd)
            elif cmd[0] == 'cat':
                run_command(commands.cat.cat, cmd)
                # print()
            elif cmd[0] == 'grep':
                if(len(cmd) < 3):
                    run_command(commands.grep.grepusage)
                else:
                    run_command(commands.grep.grep, (cmd))
            elif cmd[0] == 'wc':
                run_command(commands.wc.wc, (cmd))
            elif cmd[0] == 'cd':
                run_command(commands.cd.cd, (cmd))
            elif cmd[0] == 'history':
                run_command(commands.history.history, cmd)
            elif cmd[0] == 'mkdir':
                run_command(commands.mkdir.makedir, cmd)
            elif cmd[0] == 'rmdir':
                run_command(commands.rmdir.rmdir, cmd)
            elif cmd[0] == 'pwd':
                run_command(commands.pwd.pwd, cmd)
            elif cmd[0] == 'tail':
                run_command(commands.tail.tail, cmd)
            elif cmd[0] == 'head':
                run_command(commands.head.head, cmd)
            elif cmd[0] == 'cp':
                run_command(commands.cp.cp, (cmd))
            elif cmd[0] == 'mv':
                run_command(commands.mv.mv, (cmd))
            elif cmd[0] == 'rm':
                run_command(commands.rm.rm, (cmd))
            elif cmd[0] == 'sort':
                run_command(commands.sort.sort, (cmd))
            elif cmd[0] == 'man':
                run_command(commands.man.man, (cmd))
            elif cmd[0] == 'less':
                run_command(commands.less.less, (cmd))
            elif cmd[0] == 'exit':
                break
            else:
                print("Command does not exist!")

        sys.stdout = defaultStdout
