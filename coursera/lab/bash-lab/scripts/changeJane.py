#!/usr/bin/env python3

import sys
import subprocess


with open(sys.argv[1], mode='r',encoding='UTF-8') as file:
    for f in  file.readlines():
      newfile = f.strip().replace("jane","jdoe")

      subprocess.run(["mv",f,newfile])

    file.close()


