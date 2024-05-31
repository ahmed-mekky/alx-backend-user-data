#!/usr/bin/env python3
"""auth stuff"""
from bcrypt import hashpw, gensalt
from db import DB
from user import User


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """init"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """read the function name"""
        try:
            self._db.find_user_by(email=email)
        except Exception:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError("User <user's email> already exists")


def _hash_password(password: str) -> bytes:
    """security stuff"""
    salt = gensalt(rounds=12)
    return hashpw(password.encode(), salt)
