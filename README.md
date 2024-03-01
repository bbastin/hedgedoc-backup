<!--
SPDX-FileCopyrightText: 2024 Benedikt Bastin

SPDX-License-Identifier: CC-BY-SA-4.0
-->

# Simple HedgeDoc backup tool

## About

This project is a small and simple backup tool that allows backups from
HedgeDoc. It can be configured using the three global variables, which specify
the download location, the interval after which the markdown files should be
re-downloaded and the valid HedgeDoc instances.

## Installation

You can install all necessary dependencies using

```bash
pip install -r requirements.txt
```

. If you want to, you can create a virtual environment beforehand using

```bash
python -m venv .venv
source .venv/bin/activate
```

or the appropiate other activation script for your shell,
if you are not using bash. The first line only has to be run once,
whereas the second line has to be run for each new session where you
want to run the script.

## Usage

To start, you have to download one Markdown document into the download location
(by default, **./download**, which you have to create beforehand). When running
the script, it will extract all matching links and try to download them. On
subsequent runs, the newly downloaded files will also be checked.

To run the document, use

```bash
python backup.py
```

The scripts checks for already downloaded files. You can define an interval
after which files will be re-downloaded; by default, this is set to one day
(86400 seconds).

## Authors and Acknowledgment

This README is inspired by [makeareadme.com](https://www.makeareadme.com/).

## License

The code of this project is licensed under the **AGPL 3.0 or later**. The
documentation is licensed under **CC-BY-SA 4.0**. Some small configuration
files (which probably do not reach the [**threshold of originality**][
threshold]) are given a license with no conditions under **CC0 1.0**.

See [LICENSES](LICENSES) for more information.


[makeareadme]: https://www.makeareadme.com/
[threshold]: https://en.wikipedia.org/wiki/Threshold_of_originality
