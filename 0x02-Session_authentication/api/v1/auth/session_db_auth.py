#!/usr/bin/env python3
"""
Module for the SessionAuth  class
"""
from .session_exp_auth import SessionExpAuth
from os import getenv
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """Session auth class with expiration in db"""

    def create_session(self, user_id=None):
        """creating a session thing"""
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """same as before but with duration"""
        user_session = UserSession.search({'session_id': session_id})[0]
        return user_session.user_id

    def destroy_session(self, request=None):
        """random func"""
        session_id = request.cookies.get(getenv('SESSION_NAME'))
        user_session = UserSession.search({'session_id': session_id})[0]
        user_session.remove()
