#!/usr/bin/env python
"""Tests for `text_match` package."""

import pytest
from click.testing import CliRunner

from text_match import cli
from text_match.normalizer import NormalizerOptions
from text_match.text_match import contains_substring


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    del response


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "text-match" in result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output


def test_contains_substring_command():
    """Test the contains substring command."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["contains", "Hello, world!", "world"])

    # contains "    Hello, world!   " "lo, worl" --options "remove_whitespace,ignore_case"
    result = runner.invoke(
        cli.main,
        [
            "contains",
            "  Hello, world!   ",
            "lo, worl",
            "--options",
            "trim_whitespace,ignore_case",
        ],
    )
    assert result.exit_code == 0
    assert "True" in result.output


def test_contains_substring():
    """Test the contains substring function."""
    options = NormalizerOptions.enable_all()
    assert contains_substring("你好，世界！", "你好", options)
    assert not contains_substring("你好，世界！", "Hello", options)
    assert contains_substring("計算機", "计算", options)
    assert not contains_substring("計算機", "Ji", options)
    assert contains_substring("歌曲（伴奏）！，。", "(伴奏)", options)
