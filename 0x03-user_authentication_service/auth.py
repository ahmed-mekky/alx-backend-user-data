#!/usr/bin/env python3
"""auth stuff"""
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    salt = gensalt(rounds=12)
    return hashpw(password.encode(), salt)
