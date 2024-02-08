#!/usr/bin/env python3
"""
Function that returns the log message obfuscated
Args:
fields: a list of strings representing all fields of obfuscate
redaction: a string representing by what the field will be obfuscated
message: a string representing by which character is seperating all
        fields in the log line(message)
"""
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """
    Returns  the log message obfuscated
    """
    for field in fields:
        message = re.sub(field+'=.*?'+separator,
                             field+'='+redaction+separator, message)
    return message
