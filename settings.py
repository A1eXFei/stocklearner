import logging
import os
import os.path
from dotenv import load_dotenv
from collections import OrderedDict
from util import logger_name,parse_log_args

logging.getLogger(logger_name(__name__))
BASEDIR = os.path.dirname(os.path.realpath(__file__))
PATH = os.path.join(BASEDIR, '.env')

# load environmental variable from .env file, if file exists
if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    load_dotenv(PATH)
    print(f'load environmental varialbe from {PATH}')
else:
    print(
        f'skip loading environmental variable from {PATH}, since it does not exist'
    )

class Config:
    LOGGGING_FOLDER = os.getenv('LOGGING_FOLDER')

class LoggingConfig:
    ENV_VAR_NAMES = OrderedDict({
        'LOGGING_WARNING': logging.WARNING,
        'LOGGING_INFO': logging.INFO,
        'LOGGING_DEBUG': logging.DEBUG
    })

    LOGGING_CONFIG = OrderedDict()
    for env_name in ENV_VAR_NAMES:
        config_str = os.getenv(env_name)
        if config_str:
            LOGGING_CONFIG[ENV_VAR_NAMES[env_name]] = parse_log_args(
                config_str)
