import logging.config

logger = logging.getLogger('example')

logging.config.dictConfig({
    'version': 1,
    'handlers': {
        'default': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'stream': 'ext://sys.stderr',
            }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['default'],
    },
    'disable_existing_loggers': False,
})

logger.info('Hello')  # 出力される
