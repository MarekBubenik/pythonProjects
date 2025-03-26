# PyPI / Python Package Index / pypi.org - 3rd party packages
# pip / Package Manager, allow install packages /  apt-get install python3-pip
# pipx / pipx is strongly recommended for installing applications, i.e., when you will primarily use the installed code from the command line.
# venv / For libraries, i.e., when you will use the code primarily by importing it in your own projects. Typically, you should create a virtual environment yourself.

# pipx install cowsay

import cowsay
import sys

if len(sys.argv) == 2:
    #cowsay.cow("hello, " + sys.argv[1])
    cowsay.trex("hello, " + sys.argv[1])

# python3 -m venv .venv
# source .venv/bin/activate
# pip3 install cowsay
# 
# 
# 