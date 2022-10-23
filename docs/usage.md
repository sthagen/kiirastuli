# Usage

**Caveat emptor**: Maybe wait until some later version before using this tool on files you might care for.

## Help

```console
❯ kiirastuli
usage: kiirastuli [-h] [--purge FOLDERS] [--human] [--verbose] [--debug] [folders_pos]

Purgatory (Finnish: kiirastuli) - purge like hell to stay out of trouble.

positional arguments:
  folders_pos           Folders to visit and purge files from. Optional
                        (default: value of purge option)

options:
  -h, --help            show this help message and exit
  --purge FOLDERS, -p FOLDERS
                        Folders to visit and purge files from. Optional
                        (default: positional purge value)
  --human, -H           choose units to represent values optimized for humans (default: False)
  --verbose, -v         work logging more information along the way (default: False)
  --debug, -d           be even more vrbose to support debugging (default: False)
```

## Purge

You have been warned!

Some files in a folder following a monotonically increasing scheme.

```console
❯ tree away/these/
away/these/
├── 1234.data
├── 1235.data
├── 1236.data
├── 1237.data
├── 1238.data
├── 1239.data
└── 1240.data

0 directories, 7 files
```

Some carry the same content, one is empty, some carry other content:

```console
❯ md5sum away/these/* | amend
847676261680bff61c72961c8198abc0  away/these/1234.data  # same - shall stay
847676261680bff61c72961c8198abc0  away/these/1235.data  # same
847676261680bff61c72961c8198abc0  away/these/1236.data  # same
847676261680bff61c72961c8198abc0  away/these/1237.data  # same - shall stay
d41d8cd98f00b204e9800998ecf8427e  away/these/1238.data  # empty
795f3202b17cb6bc3d4b771d8c6c9eaf  away/these/1239.data  # other - shall stay
795f3202b17cb6bc3d4b771d8c6c9eaf  away/these/1240.data  # other - shall stay
```

Warning: Empty files will also be removed!

```console
❯ kiirastuli --verbose --purge away/these
2022-10-23T20:23:48.465440+00:00 DEBUG [KIIRASTULI]: KEEP file 1234.data
2022-10-23T20:23:48.465500+00:00 DEBUG [KIIRASTULI]: KEEP file 1237.data
2022-10-23T20:23:48.465518+00:00 DEBUG [KIIRASTULI]: KEEP file 1239.data
2022-10-23T20:23:48.465532+00:00 DEBUG [KIIRASTULI]: KEEP file 1240.data
2022-10-23T20:23:48.465545+00:00 DEBUG [KIIRASTULI]: REMOVE file 1235.data
2022-10-23T20:23:48.465656+00:00 DEBUG [KIIRASTULI]: REMOVE file 1236.data
2022-10-23T20:23:48.465762+00:00 DEBUG [KIIRASTULI]: REMOVE file 1238.data
2022-10-23T20:23:48.465810+00:00 INFO [KIIRASTULI]: removed 3 redundant objects or 10 combined bytes from folder at away/these
2022-10-23T20:23:48.465838+00:00 INFO [KIIRASTULI]: removed 3 total redundant objects or 10 total bytes from folders at ['away/these'] in 0.002 seconds
```

The remaining ranges of identical non-empty content:

```console
❯ tree away/these/
away/these/
├── 1234.data
├── 1237.data
├── 1239.data
└── 1240.data

0 directories, 4 files
```

Missing functionality: Pattern purge keeping only specific files after (or maybe better before) purge.

Roadmap: Next version
