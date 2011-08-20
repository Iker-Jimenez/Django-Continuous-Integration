#!/usr/bin/env python

import os.path
import sys
import subprocess
import argparse

DEFAULT_VIRTUALENV_PATH = "./env"

def setup_virtualenv(dest_dir):
    print "   Installing virtualenv"
    subprocess.call(
        ["pip", "install", "virtualenv"]
    )

    print "   Setting up new virtualenv in %s" % dest_dir
    subprocess.call(
        ["virtualenv", "--no-site-packages", "--distribute", dest_dir]
    )

def setup_dependencies(virtualenv):
    subprocess.call(
        ["pip", "install", "-E", virtualenv, "-r", "req.txt"]
    )

def main(args):
    setup_virtualenv(args.virtualenv)
    setup_dependencies(args.virtualenv)


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
