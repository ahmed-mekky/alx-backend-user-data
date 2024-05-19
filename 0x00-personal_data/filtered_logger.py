#!/usr/bin/env python3
"""
python file
"""
import re


def filter_datum(fields, redaction, message, separator):
    """returns the log message obfuscated"""
    for field in fields:
        reg = rf'{field}=[^{separator}]+'
        message = re.sub(reg, f'{field}={redaction}', message)
    return message
