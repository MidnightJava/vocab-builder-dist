#!/bin/env python

import os
import pathlib
import subprocess

FILE_TYPES = ["msi", "exe", "dmg", "AppImage"]

for file in os.listdir('.'):
  ext = pathlib.Path(file).suffix[1:]
  if ext in FILE_TYPES:
     output = subprocess.run(["sha256sum", file], stdout=subprocess.PIPE, text=True)
     with open(f"{file}.sha256", 'w') as f:
       f.write(output.stdout)

     