#!/usr/bin/env python3
"""
Module for the BasicAuth class
"""
from .auth import Auth
import base64
from typing import Tuple, TypeVar
from models.user import User


class BasicAuth(Auth):
    """Basic auth class"""
    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """extracts base64 header"""
        auth_header = str(authorization_header).split()
        if type(authorization_header) != str or auth_header[0] != 'Basic':
            return None
        return auth_header[1]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """decode base64 header"""
        if type(base64_authorization_header) != str:
            return None
        try:
            base64_header = base64.b64decode(
                base64_authorization_header, validate=True)
        except Exception:
            return None
        return base64_header.decode('utf-8')

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """function to extract_user_credentials"""
        if type(decoded_base64_authorization_header) != str:
            return (None, None)
        base64_header = str(decoded_base64_authorization_header).split(':')
        if len(base64_header) < 2:
            return (None, None)
        return (base64_header[0], base64_header[1])

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """function to get user_object"""
        if type(user_email) != str or type(user_pwd) != str or not User.all():
            return None
        users = User.search({'email': user_email})
        if users:
            user = users[0]
            if user.is_valid_password(user_pwd):
                return user
        return None
