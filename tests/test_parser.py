#!/usr/bin/env python3
import pytest
from bgg.commands import my_first_test


def test_my_first_test():
    assert my_first_test()