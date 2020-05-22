#!/usr/bin/env python3
""" Module of auth
"""
from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ auth method
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ auth method
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ auth method
        """
        return None