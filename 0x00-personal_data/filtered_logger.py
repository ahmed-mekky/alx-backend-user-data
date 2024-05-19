#!/usr/bin/env python3
"""
python file
"""
import re
from typing import List
s = str
ls = List[s]


def filter_datum(fields: ls, redaction: s, message: s, separator: s) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        reg = rf'{field}=[^{separator}]+'
        message = re.sub(reg, f'{field}={redaction}', message)
    return message
