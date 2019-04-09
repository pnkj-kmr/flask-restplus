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
api.init_app(app)

# Starting the web server
if __name__ == '__main__':

  args = COMMAND_ARGS
  # SETTING LOG CONFIGURATION
  level = iif('LOG' in args and args['LOG'], args['LOG'], LOG_LEVEL)
  Logger._setup(path=CONF_DIR + os.sep + LOG_CONFIG_FILE_NAME, log_path=LOG_DIR, level=level)

  # REGISTERING MICRO SERVICES
  micros = iif('MICROS' in args, args['MICROS'], [])
  MicroService.register(micros)

  # APPLICATION SETUP
  port = iif('PORT' in args and args['PORT'], args['PORT'], APPLICATION_PORT)
  debug = iif('LOG' in args and args['LOG'] == 'DEBUG', True, False)

  ######################################################
  # STARTING FLASK APPLICATION
  ######################################################
  app.run(host=APPLICATION_HOST, port=port, debug=debug)
  ######################################################



