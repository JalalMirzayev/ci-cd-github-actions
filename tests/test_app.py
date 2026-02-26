#!/usr/bin/env python3
"""
Test suite for the app module.
"""

from src.app import hello


def test_hello():
    """
    Test for the hello function in the app module.
    """
    assert hello() == "Hello, World!"
