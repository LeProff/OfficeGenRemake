#!/usr/bin/python3

import os
import multiprocessing as mp
from re import X
from svglib import SVG
from company import Company

# Imports all required modules. If they are not installed, it will install them.
try:
    import yaml
except:
    os.system("pip3 install --upgrade pyyaml")

    import yaml



