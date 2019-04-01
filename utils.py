#!/usr/bin/python
import os
import sys
import json
import platform
import logging
from .logging import Logger
from .constants import *

DEBUG = True
LOGGING_MODE = logging.DEBUG

# application host file configuration
HOST_FILE_NAME = "app.json"
LOG_CONFIG = "logging.json"

# directories declration
BASE_DIR = os.getcwd()
# For apache log location
BASE_DIR = "<project/to/path>"
CONFIG_DIR = BASE_DIR + os.sep + 'config'

# default host configuration
LOCAL_HOST = '127.0.0.1'
DEFAULT_PORT = 5000


def getPlatform():
  return platform.system()


if getPlatform() == 'Windows':
  LOG_FOLDER = BASE_DIR + os.sep + 'logs'
else:
  LOG_FOLDER = BASE_DIR + os.sep + 'logs'
if not os.path.isdir(LOG_FOLDER):
  os.mkdir(LOG_FOLDER)
# Setting Logging Configuration by default as
Logger._setup(path=CONFIG_DIR + os.sep + LOG_CONFIG, log_path=LOG_FOLDER, level=LOGGING_MODE)


def getLogger(name=''):
  if not name:
    name = 'root'
  return logging.getLogger(name)


def getAppHost():
  """Function helps to get the host/port detail from configure file
  """
  file_path = CONFIG_DIR + os.sep + HOST_FILE_NAME;
  try:
    config = json.loads(open(file_path).read())
    if config['app_run']:
      return config['app_run']
    return {
      'host': LOCAL_HOST,
      'port': DEFAULT_PORT,
    }
  except:
    pass
  return {}

