#!/usr/bin/env python3
# Collection of functions for parsing Slack JSON data.


def strip_username(text: str):
    stripped = text.split(' ', maxsplit=1)
    return stripped[1] if len(stripped) == 2 else ''

