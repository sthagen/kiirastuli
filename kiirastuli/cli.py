import argparse
import pathlib
import sys
from typing import List, Union

import kiirastuli.kiirastuli as api
from kiirastuli import APP_ALIAS, APP_NAME, log, parse_csl


def parse_request(argv: List[str]) -> Union[int, argparse.Namespace]:
    """DRY."""
    parser = argparse.ArgumentParser(
        prog=APP_ALIAS, description=APP_NAME, formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '--purge',
        '-p',
        dest='folders',
        default='',
        help='Folders to visit and purge files from. Optional\n(default: positional purge value)',
        required=False,
    )
    parser.add_argument(
        'folders_pos',
        nargs='?',
        default='',
        help='Folders to visit and purge files from. Optional\n(default: value of purge option)',
    )
    parser.add_argument(
        '--human',
        '-H',
        dest='human',
        default=False,
        action='store_true',
        help='choose units to represent values optimized for humans (default: False)',
    )
    parser.add_argument(
        '--verbose',
        '-v',
        dest='verbose',
        default=False,
        action='store_true',
        help='work logging more information along the way (default: False)',
    )
    parser.add_argument(
        '--debug',
        '-d',
        dest='debug',
        default=False,
        action='store_true',
        help='be even more vrbose to support debugging (default: False)',
    )
    if not argv:
        parser.print_help()
        return 0

    options = parser.parse_args(argv)

    if not options.folders:
        if options.folders_pos:
            options.folders = options.folders_pos

    options.folders = parse_csl(options.folders)

    if all(pathlib.Path(folder).is_dir() for folder in options.folders):
        return options

    log.error(f'some in {options.folders} do not exist or are no folders')
    return 1


def main(argv: Union[List[str], None] = None) -> int:
    """Delegate processing to functional module."""
    argv = sys.argv[1:] if argv is None else argv
    options = parse_request(argv)
    if isinstance(options, int):
        return 0
    return api.main(options)  # type: ignore
