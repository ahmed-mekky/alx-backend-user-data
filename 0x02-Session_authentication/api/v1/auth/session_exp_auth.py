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
        self.session_duration = getenv('SESSION_DURATION')

    def create_session(self, user_id=None):
        """creating a session aaaaa"""
        session_id = super()
        if not session_id:
            return None
        self.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now()
        }

    def user_id_for_session_id(self, session_id=None):
        """same as before but with duration"""
        if not session_id:
            return None
        elif not session_id in self.user_id_by_session_id.keys():
            return None
        elif not 'created_at' in self.user_id_by_session_id[session_id].keys():
            return None

        created_at = self.user_id_by_session_id[session_id]['created_at']
        user_id = self.user_id_by_session_id[session_id]['user_id']

        if self.session_duration <= 0:
            return user_id
        if created_at + timedelta(seconds=self.session_duration) < datetime.now():
            return None
        return user_id
