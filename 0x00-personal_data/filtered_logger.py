#!/usr/bin/env python3
"""
python file
"""
import logging.handlers
import re
from typing import List
import logging
s = str
ls = List[s]
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: ls):
        """constructor"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """formatting"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: ls, redaction: s, message: s, separator: s) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        reg = rf'{field}=[^{separator}]+'
        message = re.sub(reg, f'{field}={redaction}', message)
    return message

def get_logger() -> logging.Logger:
    """returns a logging object"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=("name", "email", "phone", "ssn", "password"))
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

