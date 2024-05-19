#!/usr/bin/env python3
"""
python file
"""
import re
from typing import List
import logging
s = str
ls = List[s]


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: ls):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        return filter_datum(self.fields, self.REDACTION, super().format(record), self.SEPARATOR)


def filter_datum(fields: ls, redaction: s, message: s, separator: s) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        reg = rf'{field}=[^{separator}]+'
        message = re.sub(reg, f'{field}={redaction}', message)
    return message
