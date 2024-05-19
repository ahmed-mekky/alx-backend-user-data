#!/usr/bin/env python3
"""
python file
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        reg = rf'{field}=[^{separator}]+'
        message = re.sub(reg, f'{field}={redaction}', message)
    return message
