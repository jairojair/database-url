# -*- coding: utf-8 -*-

import os

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse


def config():
    """
    Get database config from environment var (DATABASE_URL) automatically.
    """
    pass


def parse(url=None):
    """
    Parses a database URL.
    """

    config = {}

    if url is None:
        return

    return urlparse(url)
