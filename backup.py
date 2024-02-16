#!/usr/bin/env python

# SPDX-FileCopyrightText: 2024 Benedikt Bastin
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import requests
import re
from typing import List, Optional
from urllib.parse import urlparse
from pathlib import Path
import os
from datetime import datetime

# The location where the Markdown files should be looked for and downloaded to
download_folder = "download/"

# The number of seconds after which Markdown files should be re-downloaded
check_interval = 86400

# The URLs of valid HedgeDoc servers, terminated by a single slash
hedgedoc_servers = [
    "https://demo.hedgedoc.org/",
]


def download_document(url: str) -> Optional[str]:
    """Download a Markdown document from a HedgeDoc server."""

    download_url = url + "/download"

    print(f'Downloading "{download_url}"')
    r = requests.get(download_url, allow_redirects=False)
    if r.status_code != 200:
        return None

    return r.text


def extract_links(document: str) -> List[str]:
    """Extract all links from a markdown document using the valid hedgedoc_servers."""

    hits = []
    for server in hedgedoc_servers:
        hits += re.findall(f"({server}[^\\s)#?]+)", document)

    return hits


def main():
    unix_timestamp = (datetime.now() - datetime(1970, 1, 1)).total_seconds()

    # Open all files in the download folder
    for file in os.listdir(download_folder):
        with open(download_folder + file, "r") as file:
            data = file.read()

        links = extract_links(data)

        # Check and download each linked document
        for link in links:
            doc_id = urlparse(link).path[1:]
            if "/" in doc_id:
                continue

            filename = Path(download_folder + doc_id + ".md")

            if (
                filename.is_file()
                and (unix_timestamp - filename.stat().st_mtime) < check_interval
            ):
                print(
                    f'File "{doc_id}" downloaded within the last {check_interval} seconds, skipping'
                )
                continue

            doc = download_document(link)
            if doc == None:
                print(f'Error downloading "{doc_id}"')
            with open(filename, "w") as file:
                file.write(str(doc))
                print(f'Successfully downloaded "{doc_id}"')


if __name__ == "__main__":
    main()
