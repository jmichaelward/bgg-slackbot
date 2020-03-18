#!/usr/bin/env python3
# Tests for the slack/parser module.

from slack.parser import *


def test_it_strips_a_username():
    text = "<@UVD0SF9M5> latest thegermwar"

    assert strip_username(text) == "latest thegermwar"