import os
import subprocess


def script_updater():
    return True


def check(program, extra_arg=''):
    try:
        devnull = open(os.devnull)
        subprocess.Popen([program, extra_arg], stdout=devnull, stderr=devnull).communicate()
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            return False
    return True
