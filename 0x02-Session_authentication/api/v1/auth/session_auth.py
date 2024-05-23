#!/usr/bin/env python3
"""
Module for the SessionAuth  class
"""
from .auth import Auth
from uuid import uuid4


class SessionAuth (Auth):
    """Basic auth class"""
    user_id_by_session_id = {}
    def create_session(self, user_id: str = None) -> str:
        if not isinstance(user_id, str):
            return None
        session_id = uuid4()
        self.user_id_by_session_id[session_id] = user_id
        return session_id
