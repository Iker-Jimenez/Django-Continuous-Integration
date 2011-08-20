#!/usr/bin/env python

import sys
import subprocess

DEFAULT_VIRTUALENV_PATH = "../env"

def setup_virtualenv(dest_dir=DEFAULT_VIRTUALENV_PATH):
    print "   Installing virtualenv"
    subprocess.call(
        ["pip", "install", "virtualenv"]
    )

    print "   Setting up new virtualenv in %s" % dest_dir
    subprocess.call(
        ["virtualenv", "--no-site-packages", dest_dir]
    )

def activate_virtualenv(virtual_env=DEFAULT_VIRTUALENV_PATH):
    if sys.platform == 'win32':
        activate = "Scripts\\activate.bat"
    else:
        activate = 'bin/activate'

    print "   Activating virtualenv in %s" % virtual_env


if __name__ == "__main__":
    setup_virtualenv()
