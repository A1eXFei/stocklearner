import pathlib
from datetime import datetime
import logging
import logging.config
from settings import LoggingConfig, Config
from app import TRAINING_NAME
from util import logger_name

pathlib.Path(Config.LOGGGING_FOLDER).mkdir(parents=True, exist_ok=True)

LOG_FILE_NAME = f"{TRAINING_NAME}-{datetime.now().strftime('%Y%m%d%H%M%S')}.log"

DICT_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'simpleFormatter',
            'filename': Config.LOGGGING_FOLDER + LOG_FILE_NAME
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simpleFormatter',
            'stream': 'ext://sys.stdout'
        }
    },
    'formatters': {
        'simpleFormatter': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'INFO'
        }
    }
}

logging.config.dictConfig(DICT_CONFIG)

for _level in LoggingConfig.LOGGING_CONFIG:
    module_configs = LoggingConfig.LOGGING_CONFIG[_level]
    for mod in module_configs:
        if mod == '*':
            logging.getLogger(TRAINING_NAME).setLevel(_level)
        else:
            mod = logger_name(mod)
            logging.getLogger(mod).setLevel(_level)
