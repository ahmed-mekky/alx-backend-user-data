#!/usr/bin/env python3
"""
Module for the BasicAuth class
"""
from .auth import Auth
import base64


class BasicAuth(Auth):
    """Basic auth class"""
    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """extracts base64 header"""
        try:
            auth_header = str(authorization_header).split()
            if not authorization_header or auth_header[0] != 'Basic':
                return None
        except ValueError:
            return None
        return auth_header[1]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """decode base64 header"""
        if not base64_authorization_header:
            return None
        try:
            base64_header = base64.b64decode(
                str(base64_authorization_header), validate=True)
        except Exception:
            return None
        return base64_header.decode('utf-8')
