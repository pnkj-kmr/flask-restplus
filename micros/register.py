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
import os
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
  def register(micros=[]):
    """Module load by given service name
    """
    logger.warn("Micro services is loading...")
    count = 0
    services = micros
    # print("Services as : ", services, type(services))
    logger.warn(f"Micro services  {services}")

    if services:

      for module in services:
        try:
          command_module = __import__("apps.%s.namespace" % module)
          count += 1
          logger.warn(f"Micro service - {module}")
        except ImportError:
          # print(traceback.print_exc())
          logger.error("Exception occured at:", exc_info=True)
          raise ImportError

    else:

      # Importing all application by default
      app_list = filter(lambda a: a not in ['__pycache__', '__init__.py'], os.listdir(os.getcwd() + os.sep + 'apps'))
      # demo = __import__('apps.demo.namespace')
      for module in app_list:
        __import__('apps.%s.namespace' % module)
        count += 1
        logger.warn(f"Micro service - {module}")
      
    logger.warn(f'Micros loaded ({count}) - successfully')
      


