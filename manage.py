#!/usr/bin/python
__license__     = ""
__version__     = "0.1"
__author__      = "Pankaj Kumar"
__email__       = "hellopankaj21@gmail.com"
__copyright__   = "Copyright @2019"
__status__      = "Production/Development"

from core.api import api
from core.app import app
from core.utils import *
from micros.register import MicroService


"""
Initiating the application
"""
app.debug = DEBUG
api.init_app(app)

# Registering the micro services
MicroService.register()

# Starting the web server
if __name__ == '__main__':  

  # Getting host detail
  host = getAppHost()

  # Starting the application server
  app.run(**host)



