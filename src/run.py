import os
import sys
# Disable compiled .pyc files
sys.dont_write_bytecode = True

sys.path.insert(1, os.path.join(os.path.abspath('.'), 'lib'))
import application

