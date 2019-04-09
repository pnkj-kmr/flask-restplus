#!/usr/bin/python
import os
import sys
import json
import platform
import logging
import argparse
from .logging import Logger
from .constants import *

DEBUG = True


def getPlatform():
  return platform.system()


LOGGING_MODE = {
  'DEBUG': logging.DEBUG,
  'INFO': logging.INFO,
  'WARN': logging.WARNING,
  'ERROR': logging.ERROR,
  'CRITICAL': logging.CRITICAL
}


# directories declration
BASE_DIR = os.getcwd()
CONF_DIR = BASE_DIR + os.sep + 'config'


# For apache log location
if os.environ.get('APACHE_LOG_DIR', ''):
  LOG_DIR = os.environ['APACHE_LOG_DIR']
else:
  if getPlatform() == 'Windows':
    LOG_DIR = BASE_DIR + os.sep + 'logs'
  else:
    LOG_DIR = BASE_DIR + os.sep + 'logs'


if not os.path.isdir(LOG_DIR):
  os.mkdir(LOG_DIR)


def iif(a, b, c):
  """
  :param a: Expression
  :param b: Value
  :param c: Value
  :return: Value
  """
  if a:
    return b
  return c


def getLogger(name=''):
  if not name:
    name = 'root'
  return logging.getLogger(name)


def app_run_config():
  """
  Finding the run time configuration
  :return: {}
  """
  log_choies = tuple([i for i in LOGGING_MODE])
  parser = argparse.ArgumentParser()
  parser.add_argument('-p', '--port', action='store', dest='PORT', type=int, help='Application Start Port')
  parser.add_argument('-l', '--loglevel', choices=log_choies, action='store', dest='LOG', help='Application Log Level')
  parser.add_argument('-m', '--micro', action='append', dest='MICROS', default=[], help='Application Micro Services')
  parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
  ret = parser.parse_args()

  return {
    'PORT': ret.PORT,
    'LOG': ret.LOG,
    'MICROS': ret.MICROS,
  }

###############################
# DEFAULT CALLING OF RUN CONFIG
COMMAND_ARGS = app_run_config()
###############################


