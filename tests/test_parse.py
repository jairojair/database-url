import pytest

from py_database_url import config


def test_config_without_url():

    assert config.parse() is None


def test_parse_database_url():
    """
    Describe
    """

    url = "postgres://user:password@hostname:5432/db-name"

    ret = config.parse(url)

    assert ret.username == "user"
    assert ret.password == "password"
    assert ret.hostname == "hostname"
    assert ret.port == 5432


def test_config_database_url_orator():

    expected = {
        "postgres": {
            "database": "database-name",
            "driver": "postgres",
            "host": "hostname",
            "user": "user",
            "password": "password",
            "prefix": "",
        }
    }

    assert config.orator == expected
