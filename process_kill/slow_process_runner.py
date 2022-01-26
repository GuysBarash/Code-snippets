import os
import signal
import subprocess
import time
import psutil

if __name__ == '__main__':
    # Part 3, define the commands as a list
    target_script = "C:\work\dst-womb\Library\process_kill\slow_process.py"

    cmds = list()
    cmds += ['python']
    cmds += [target_script]

    # Part 4, create the process and run
    start = time.time()
    p = subprocess.Popen(cmds, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         shell=True)

    # get stout and return code
    std_out, std_err = p.communicate()
    if std_err == '':
        std_err = '<NO ERROR>'

    return_code = p.poll()

    # Done
    print("ERROR MSG:")
    print(std_err)
    print("")
    print("TEXT:")
    print(std_out)
    print("")
    print("Return Code: {}".format(return_code))
