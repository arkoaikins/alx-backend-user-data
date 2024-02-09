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
import logging
import os
import mysql.connector


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        filter values in incoming log records using
        filter_datum
        """
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """
    Returns  the log message obfuscated
    """
    for field in fields:
        message = re.sub(field+'=.*?'+separator,
                         field+'='+redaction+separator, message)
    return message


PII_FIELDS = ('password', 'ssn', 'name', 'email', 'phone')


def get_logger() -> logging.Logger:
    """get_logger function"""
    log = logging.getLogger("user_data")
    log.setLevel(logging.INFO)

    log.propagate = False
    handler = logging.StreamHandler()
    style = RedactingFormatter(PII_FIELDS)
    handler.setFormatter(style)
    log.addHandler(handler)
    return log


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    return db connection
    """
    user = os.getenv('PERSONAL_DATA_DB_USERNAME') or "root"
    passwd = os.getenv('PERSONAL_DATA_DB_PASSWORD') or ""
    host = os.getenv('PERSONAL_DATA_DB_HOST') or "localhost"
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')
    conn = mysql.connector.connect(user=user,
                                   password=passwd,
                                   host=host,
                                   database=db_name)
    return conn
