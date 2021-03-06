import os
import subprocess
import sys


def run_proc(cmd, **kwargs):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, **kwargs)
    out = p.communicate()[0]
    return (p.returncode, out.strip())


def find_nearest(directory, search):
    directory = os.path.abspath(directory)
    parts = directory.split(os.path.sep)
    for idx in xrange(len(parts)):
        d = os.path.sep.join(parts[:-idx])
        if not d:
            d = os.path.sep.join(parts)
        if os.path.isdir(os.path.join(d, search)):
            return d
    raise OSError


def out(msg):
    sys.stdout.write(msg)
    sys.stdout.flush()


def err(msg):
    sys.stderr.write(msg)
    sys.stderr.flush()


def error(msg, exit=True):
    err("ERROR: %s" % msg)
    if exit:
        sys.exit(1)
