import logging.config

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
    }
})

logger = logging.getLogger('example')
logger.info('Hello')  # 出力される

