# Check env through python

import sys, os, platform

# Python version
print(sys.version)
print(sys.version_info)

# OS
print(platform.system())
print(platform.release())

# Script execution folder
print(os.getcwd())