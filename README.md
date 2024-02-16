<!--
SPDX-FileCopyrightText: 2024 Benedikt Bastin

SPDX-License-Identifier: CC-BY-SA-4.0
-->

# Simple HedgeDoc backup tool

This project is a small and simple backup tool that allows backups from
HedgeDoc. It can be configured using the three global variables, which specify
the download location, the interval after which the markdown files should be
re-downloaded and the valid HedgeDoc instances.

To start, you have to download one Markdown document into the download location
(by default, **./download**, which you have to create beforehand). When running
the script, it will extract all matching links and try to download them. On
subsequent runs, the newly downloaded files will also be checked.

The scripts checks for already downloaded files. You can define an interval
after which files will be re-downloaded; by default, this is set to one day
(86400 seconds).
