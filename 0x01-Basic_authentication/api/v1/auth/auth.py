#!/usr/bin/env python3
"""
Module for the Auth class
"""
from flask import request
from typing import List, TypeVar


User = TypeVar('User')


class Auth:
    """
    Auth Class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """class method"""
        if (
            path is None or excluded_paths is None or len(excluded_paths) < 1
            or all(path != excluded_path
                   and path != excluded_path[:-1]
                   for excluded_path in excluded_paths)
        ):
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """class method"""
        return None

    def current_user(self, request=None) -> User:
        """class method"""
        return None
