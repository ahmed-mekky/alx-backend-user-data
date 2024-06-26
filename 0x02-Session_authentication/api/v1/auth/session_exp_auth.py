#!/usr/bin/env python3
"""
Module for the SessionAuth  class
"""
from .session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """Session auth class with expiration"""
    def __init__(self):
        """init"""
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
            if not self.session_duration:
                self.session_duration = 0
        except TypeError:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """creating a session aaaaa"""
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        self.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """same as before but with duration"""
        if not session_id:
            return None
        elif session_id not in self.user_id_by_session_id.keys():
            return None
        elif 'created_at' not in self.user_id_by_session_id[session_id].keys():
            return None

        created_at = self.user_id_by_session_id[session_id]['created_at']
        user_id = self.user_id_by_session_id[session_id]['user_id']
        duration_sec = timedelta(seconds=self.session_duration)

        if self.session_duration <= 0 or not self.session_duration:
            return user_id
        if created_at + duration_sec < datetime.now():
            return None
        return user_id
