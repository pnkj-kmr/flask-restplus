#!/usr/bin/python
__license__     = "Logging"
__version__     = "0.1"
__author__      = "Pankaj Kumar"
__email__       = "hellopankaj21@gmail.com"
__copyright__   = "Copyright @2019"
__status__      = "Production/Development"

from .utils import *
from logging.config import dictConfig


class Logger:
  """
  Class helps to set the logging mechanism
  based on the configurations
  """

  @staticmethod
  def _setup(path='logging.json', log_path='', level=logging.INFO, env_key='LOG_CFG'):
    """Setup logging configuration
    """
    # currently skipping env_key
    # value = os.getenv(env_key, None)
    # if value:
    #   path = value
    if os.path.exists(path):
      config = {}
      with open(path, 'rt') as f:
        config = json.load(f)
      path_check = config.get('handlers', {}).get('info_file_handler', {}).get('filename', '')
      if path_check:
        config['handlers']['info_file_handler']['filename'] = log_path + os.sep + 'main.log'
      path_check = config.get('handlers', {}).get('error_file_handler', {}).get('filename', '')
      if path_check:
        config['handlers']['error_file_handler']['filename'] = log_path + os.sep + 'main_error.log'
      log_level = config.get('root', {}).get('level', '')
      if log_level:
        config['root']['level'] = level
      # print("LOGGING : ", json.dumps(config, indent=2))
      dictConfig(config)
    else:
      logging.basicConfig(level=level)