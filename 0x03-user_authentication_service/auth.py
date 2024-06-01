#!/usr/bin/env python3
"""auth stuff"""
from bcrypt import hashpw, gensalt, checkpw
from db import DB
from user import User
from uuid import uuid4


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
        raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """check user's password"""
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            return False
        return checkpw(password.encode(), user.hashed_password)

    def create_session(self, email: str) -> str:
        """create a session"""
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            return None
        user.session_id = _generate_uuid()
        return user.session_id


def _hash_password(password: str) -> bytes:
    """security stuff"""
    salt = gensalt(rounds=12)
    return hashpw(password.encode(), salt)


def _generate_uuid() -> str:
    """uuids"""
    return str(uuid4())
