#!/usr/bin/python3
import shutil
import sys

src = sys.argv[1]
dst = sys.argv[2]
shutil.copytree(src, dst)
