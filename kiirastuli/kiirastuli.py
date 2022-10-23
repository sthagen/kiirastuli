"""Purge monotonically named files in folders keeping range endpoints.

Implementation uses sha256 hashes for identity and assumes that
the natural order relates to the notion of fresher or better.
"""
import argparse
import datetime as dti
import logging
import os
import typing

from puhdistusalue.puhdistusalue import read_folder, triage_hashes  # type: ignore
from puristaa.puristaa import prefix_compression  # type: ignore

from kiirastuli import log

BUFFER_BYTES = 2 << 15


@typing.no_type_check
def humanize_mass(total_less_bytes: int):
    """DRY"""
    if total_less_bytes >= 1e9:
        return f'{round(total_less_bytes / 1024 / 1024 / 1024, 3) :.3f}', 'total gigabytes'
    if total_less_bytes >= 1e6:
        return f'{round(total_less_bytes / 1024 / 1024, 3) :.3f}', 'total megabytes'
    if total_less_bytes >= 1e3:
        return f'{round(total_less_bytes / 1024, 3) :.3f}', 'total kilobytes'

    return f'{total_less_bytes :d}', 'total bytes'


@typing.no_type_check
def humanize_duration(duration_seconds: float):
    """DRY"""
    if duration_seconds >= 3600:
        return f'{round(duration_seconds / 60 / 60, 3) :.3f}', 'hours'
    if duration_seconds >= 60:
        return f'{round(duration_seconds / 60, 3) :.3f}', 'minutes'
    if duration_seconds >= 1:
        return f'{round(duration_seconds, 3) :.3f}', 'seconds'

    return f'{round(duration_seconds * 1e3, 3) :.3f}', 'millis'


@typing.no_type_check
def list_dir(folder_path):
    """Access the dir and yield the local names inside."""
    return os.listdir(folder_path)


@typing.no_type_check
def elements_of_gen(folder_path):
    """Prefix names in folder path and yield sorted pairs of names and file paths."""
    for name in sorted(name for name in list_dir(folder_path)):
        yield name, os.path.join(folder_path, name)


@typing.no_type_check
def main(options: argparse.Namespace) -> int:
    """Process the files separately per folder."""
    start_time = dti.datetime.utcnow()
    verbose = options.verbose
    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    human = options.human
    folders = options.folders
    total_removed, total_less_bytes = 0, 0
    for a_path in folders:
        hash_map = {}
        try:
            hash_map = read_folder(a_path)
        except FileNotFoundError as err:
            log.warning(f'WARNING: Skipping non-existing path ({a_path}) -> "{err}"')
        if hash_map:
            keep_these, remove_those = triage_hashes(hash_map)
            for this in keep_these:
                log.debug(f'KEEP file {this}')
            folder_removed, folder_less_bytes = 0, 0
            for that in remove_those:
                log.debug(f'REMOVE file {that}')
                target = os.path.join(a_path, that)
                folder_less_bytes += os.path.getsize(target)
                os.remove(target)
                folder_removed += 1

            if verbose:
                log.info(
                    f'removed {folder_removed} redundant objects or {folder_less_bytes}'
                    f' combined bytes from folder at {a_path}'
                )
            total_less_bytes += folder_less_bytes
            total_removed += folder_removed

    prefix, rel_paths = prefix_compression(folders, policy=lambda x: x == '/')
    if len(rel_paths) > 5:
        folders_disp = f"{prefix}[{', '.join(rel_paths[:3])}, ... {rel_paths[-1]}]"
    else:
        folders_disp = f'{folders}' if folders else '[<EMPTY>]'

    duration_seconds = (dti.datetime.utcnow() - start_time).total_seconds()
    if human:
        m_quantity, m_unit = humanize_mass(total_less_bytes)
        d_quantity, d_unit = humanize_duration(duration_seconds)
    else:
        m_quantity, m_unit = f'{total_less_bytes :d}', 'total bytes'
        d_quantity, d_unit = f'{round(duration_seconds, 3) :.3f}', 'seconds'

    log.info(
        f'removed {total_removed} total redundant objects or'
        f' {m_quantity} {m_unit} from folders at {folders_disp}'
        f' in {d_quantity} {d_unit}'
    )
    return 0
