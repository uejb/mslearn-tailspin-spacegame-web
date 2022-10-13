#!/usr/bin/env python3

import sys
import subprocess

def main():
    """main function to prepare dev-environment"""
    subprocess.run(["apt update"])
    subprocess.run(["apt install python3"])
    subprocess.run(["python3 -m pip install -r requirements.txt"])
    print(done)
    sys.exit(0)

if __name__=="__main__":
    main()