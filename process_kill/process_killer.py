import os
import signal
import subprocess
import time
import psutil


def kill_proc_tree(pid, including_parent=True):
    parent = psutil.Process(pid)
    children = parent.children(recursive=True)
    for child in children:
        child.kill()
    gone, still_alive = psutil.wait_procs(children, timeout=5)
    if including_parent:
        parent.kill()
        parent.wait(5)


if __name__ == '__main__':
    # Part 3, define the commands as a list
    target_script = "C:\work\dst-womb\Library\process_kill\slow_process_runner.py"

    cmds = list()
    cmds += ['python']
    cmds += [target_script]

    timeout = 2

    # Part 4, create the process and run
    start = time.time()
    p = subprocess.Popen(cmds, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         shell=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
    print("Original pid: {}".format(p.pid))

    # Wait until completion
    while p.poll() is None:
        time.sleep(0.5)
        current_duration = time.time() - start
        print("Current duration: {:>.1f} seconds".format(current_duration))

        if current_duration > timeout:
            print("TIME TO KILL")
            parent = psutil.Process(p.pid)
            for child in parent.children(recursive=True):  # or parent.children() for recursive=False
                print("Killing child: PID {}".format(child.pid))
                child.terminate()
            print("Parent status: {}".format(p.poll() is None))
            time.sleep(0.1)
            # print("killing parent: PID {}".format(parent.pid))
            # p.terminate()

    print('<>')

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
