#!/usr/bin/python
__license__     = "Logging"
__version__     = "0.1"
__author__      = "Pankaj Kumar"
__email__       = "hellopankaj21@gmail.com"
__copyright__   = "Copyright @2019"
__status__      = "Production/Development"

import os
import logging
from .constants import LOG_FILE_NAME, LOG_ERR_FILE_NAME
from logging.config import dictConfig
import json


class Logger:
  """
  Class helps to set the logging mechanism
  based on the configurations
  """

  @staticmethod
  def _setup(path='logging.json', log_path='', level='INFO'):
    """Setup logging configuration
    """
    # config file check
    if os.path.exists(path):
      config = {}
      with open(path, 'rt') as f:
        config = json.load(f)
      # print(json.dumps(config, indent=2))
      # File configuration
      check_ = config.get('handlers', {}).get('file', {})
      if check_.get('filename', ''):
        config['handlers']['file']['filename'] = log_path + os.sep + LOG_FILE_NAME
      if check_.get('level', ''):
        config['handlers']['file']['level'] = level
      # Error file configuration
      check_ = config.get('handlers', {}).get('error_file', {})
      if check_.get('filename', ''):
        config['handlers']['error_file']['filename'] = log_path + os.sep + LOG_ERR_FILE_NAME
      # Root log level configuration
      check_ = config.get('root', {})
      if check_.get('level', ''):
        config['root']['level'] = level
      # print("LOGGING : ", json.dumps(config, indent=2))
      dictConfig(config)
    else:
      logging.basicConfig(level=level)

