import sys
import glob

plugins = glob.glob("plugins/*.py")

for p in plugins:
    if p[:-3].split('/')[1] != '__init__':
        __import__('.'.join(p[:-3].split('/')))
