import pytest

from py_database_url import parse


def test_parse_without_url():

    assert parse() is None


def test_parse_database_url():
    """
    Describe
    """

    url = "postgres://user:password@hostname:5432/database-name"

    config = parse(url)

    assert config.username == "user"
    assert config.password == "password"
    assert config.hostname == "hostname"
    assert config.port == 5432
