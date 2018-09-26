# -*- coding: utf-8 -*-

import os

try:
    # Python 3
    from urllib.parse import urlparse

except ImportError:
    # Python 2
    from urlparse import urlparse


class Config(object):
    """
    Describe class
    """

    def __init__(self):
        pass

    def __get_database_url_var(self):
        """
        Describe
        """
        return os.environ["DATABASE_URL"]

    def config(self):
        """
        Get database config from environment var (DATABASE_URL) automatically.
        """
        pass

    def parse(self, url=None):
        """
        Parses a database URL.
        """

        config = {}

        if url is None:
            return

        return urlparse(url)

    @property
    def orator(self):
        """
        Method to parser for orator format.
        """

        url = self.__get_database_url_var()
        url = self.parse(url)

        config = {
            f"{url.scheme}": {
                "driver": url.scheme,
                "host": url.hostname,
                "database": url.path[1:],
                "user": url.username,
                "password": url.password,
                "prefix": "",
            }
        }

        return config


config = Config()
