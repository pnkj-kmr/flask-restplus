#!/usr/bin/python
__license__     = ""
__version__     = "0.1"
__author__      = "Pankaj Kumar"
__email__       = "hellopankaj21@gmail.com"
__copyright__   = "Copyright @2019"
__status__      = "Production/Development"

"""
This module helps to register the application
"""
import sys
import traceback
from core.utils import getLogger

logger = getLogger(__name__)


class MicroService:
  """
  Class helps to maintain the micro service based
  input which given at the run time
  """

  def __init__(self):
    pass

  @staticmethod
  def register():
    """Module load by given service name
    """
    services = sys.argv[1:]
    # print("Services as : ", services, type(services))
    logger.debug(f"Services List as : {services}")

    if services:

      for module in services:
        try:
          command_module = __import__("apps.%s.namespace" % module)
          logger.debug(f"Imported - {module}")
        except ImportError:
          # print(traceback.print_exc())
          logger.error("Exception occured at:", exc_info=True)
          raise ImportError

    else:

      logger.debug("Importing all modules of apps")
      # Importing all application by default
      demo = __import__('apps.demo.namespace')
      logger.debug("Imported - demo")


