#!/usr/bin/python
__license__     = ""
__version__     = "0.1"
__author__      = "Pankaj Kumar"
__email__       = "hellopankaj21@gmail.com"
__copyright__   = "Copyright @2019"
__status__      = "Production/Development"

from flask_restplus import Api
from .utils import *

"""
Defining the RESTPlus instance
"""

api = Api(
          None, 
          version=APP_VERSION,
          title=APP_TITLE,
          description=APP_DESCRIPTION,
      )
