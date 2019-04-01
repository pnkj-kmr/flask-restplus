#!/usr/bin/python
#
# Module help to set flask with python3
#
# TODO
# 1. Give the proper path for LOG_FOLDER
# 2. Allow privilege to folder with 777
#


import sys
import logging
logging.basicConfig(stream=sys.stderr)

# Setting the environment with virtualenv command
activate_this = '<path/to/project/env>/venv/bin/activate_this.py'
with open(activate_this) as file_:
  exec(file_.read(), dict(__file__=activate_this))

# Importing the path of application
sys.path.insert(0, '<path/to/project>')

# Import flask application instance
from manage import app as application


