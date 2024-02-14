"""
A class to manage the API authentication
"""
from flask import request
from typing import List, TypeVar


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
        return False

    def authorization_header(self, request=None) -> str:
        """
        Will return authorization header for request

        Args:
        request: This is set to None as default(optional)
        will be the Flask request object

        Returns:
        A string,which is the authorization_header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Gets the current user that has been authenticated

        Args:
        request: This is set to None as default(optional)
        will be the Flask request object
        """
        return None
