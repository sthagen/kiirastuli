"""Purgatory (Finnish: kiirastuli) - purge like hell to stay out of trouble."""
import os
from typing import List

APP_NAME = 'Purgatory (Finnish: kiirastuli) - purge like hell to stay out of trouble.'
APP_ALIAS = 'kiirastuli'
APP_ENV = 'KIIRASTULI'
DEBUG = bool(os.getenv(f'{APP_ENV}_DEBUG', ''))
VERBOSE = bool(os.getenv(f'{APP_ENV}_VERBOSE', ''))
QUIET = False
STRICT = bool(os.getenv(f'{APP_ENV}_STRICT', ''))
ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'
DEFAULT_CONFIG_NAME = '.kiirastuli.json'
DEFAULT_LF_ONLY = 'YES'

# [[[fill git_describe()]]]
__version__ = '2022.7.30+parent.9c02148f'
# [[[end]]] (checksum: 1543c5af69cff54e3f27eec8f5963a17)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
__all__: List[str] = []
