#!/usr/bin/env python3
"""
Module for the Auth class
"""
from flask import request as req
from typing import List, TypeVar


User = TypeVar('User')


class Auth:
    """
    Auth Class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """class method"""
        if path is None or excluded_paths is None or len(excluded_paths) < 1:
            return True
        for excluded_path in excluded_paths:
            if excluded_path[-1] == '*':
                if excluded_path[:-1] in path:
                    return False
            if path in excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """class method"""
        header = request.headers.get('Authorization')
        if not header or request is None:
            return None
        return header

    def current_user(self, request=None) -> User:
        """class method"""
        return None
