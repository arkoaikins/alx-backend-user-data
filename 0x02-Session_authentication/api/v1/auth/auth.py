#!/usr/bin/env python3
"""
A class to manage the API authentication
"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """
    This class is the template for all authentication system
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        checks if authentication is required

        Args:
        path(str): The path that needs to be checked
        excluded_paths(List[str]): These are paths that are excluded
        and does not need to be checked

        Returns:
        False
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                if path.startswith(excluded_path.rstrip('*')):
                    return False
            elif path.rstrip('/') == excluded_path.rstrip('/'):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Will return authorization header for request
        Validates all requests to secure the API

        Args:
        request: This is set to None as default(optional)
        will be the Flask request object

        Returns:
        A string,which is the authorization_header
        """
        if request is None:
            return None

        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return None

        return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Gets the current user that has been authenticated

        Args:
        request: This is set to None as default(optional)
        will be the Flask request object
        """
        return None

    def session_cookie(self, request=None) -> str:
        """
        returns a cookie from a request
        """
        if request is not None:
            cookie_name = os.getenv('SESSION_NAME')
            return request.cookies.get(cookie_name)
