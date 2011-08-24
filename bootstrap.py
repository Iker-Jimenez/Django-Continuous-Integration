#!/usr/bin/env python

import os.path
import sys
import subprocess
import argparse

DEFAULT_VIRTUALENV_PATH = "./env"
DEPENDENCIES = ["pip", "virtualenv"]

def check_dependencies():
    for dependency in DEPENDENCIES:
        try:
            __import__(dependency)
        except ImportError:
            print "Dependency missing: %s is not installed" % dependency
            sys.exit(1)
    print "All dependencies found"

def setup_virtualenv(dest_dir):
    print "   Setting up new virtualenv in %s" % dest_dir
    subprocess.call(
        ["virtualenv", "--no-site-packages", "--distribute", dest_dir]
    )

def setup_dependencies(virtualenv):
    subprocess.call(
        (virtualenv + "/bin/pip install -r req.txt").split(' ')
    )

def display_activate_warning(virtualenv):
    if sys.platform == 'win32':
        activate = "Scripts\\activate.bat"
        command = ""
    else:
        activate = 'bin/activate'
        command = "source"

    path = os.path.join(virtualenv, activate)

    print "\nYou can now activate the virtual environment by running:\n" \
            "%s %s\n" % (command, path)

def main(args):
    check_dependencies()
    if os.path.exists(args.virtualenv):
        print "Environment seems to be setup at %s, exiting" % args.virtualenv
    else:
        setup_virtualenv(args.virtualenv)
        setup_dependencies(args.virtualenv)
        display_activate_warning(args.virtualenv)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--virtualenv","-v",
        metavar="V",
        help="Path for the virtualenv",
        default=DEFAULT_VIRTUALENV_PATH,
        required=False)

    args = parser.parse_args()

    main(args)
