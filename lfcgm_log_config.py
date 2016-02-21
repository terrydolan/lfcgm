"""Logger config for lfcgm."""

dictLogConfig = {
    'version': 1,
    'handlers': {
        'fileHandler': {
            'class': 'logging.FileHandler',
            'level': 'INFO',
            'formatter': 'myFileFormatter',
            'filename': 'lfcgm.log'
        },
        'consoleHandler': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'myConsoleFormatter'
        }
    },
    'loggers': {
        'lfcgm': {
            'handlers': ['consoleHandler'],
            'level': 'DEBUG'
        }
    },
    'formatters': {
        'myFileFormatter': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'myConsoleFormatter': {
            'format': '%(name)s - %(levelname)s - %(message)s'
        }
    }
}
