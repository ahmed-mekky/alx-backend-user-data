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
        """creates a session"""
        if not isinstance(user_id, str):
            return None
        session_id = uuid4()
        self.user_id_by_session_id[session_id] = user_id
        return session_id
    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns the in-session user id"""
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
