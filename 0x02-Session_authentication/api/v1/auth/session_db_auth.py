#!/usr/bin/env python3
"""
Module for the SessionAuth  class
"""
from .session_exp_auth import SessionExpAuth
from os import getenv
from models.user_session import UserSession
from datetime import timedelta, datetime


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
        if not session_id:
            return None
        user_sessions = UserSession.search({'session_id': session_id})
        if not user_sessions:
            return None

        user_session = user_sessions[0]
        created_at = user_session.created_at
        user_id = user_session.user_id
        duration_sec = timedelta(seconds=self.session_duration)

        if self.session_duration <= 0 or not self.session_duration:
            return user_id
        if created_at + duration_sec < datetime.now():
            return None
        return user_id

    def destroy_session(self, request=None):
        """random func"""
        session_id = request.cookies.get(getenv('SESSION_NAME'))
        user_session = UserSession.search({'session_id': session_id})[0]
        user_session.remove()
        return True
