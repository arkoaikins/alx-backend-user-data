#!/usr/bin/env python3
"""
Module for basic Auth that inherits from Auth
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """Basic auth class"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Args:
        authorization_header(str): the autorization header

        Returns:
        returns the Base64 part of the Authorization header for
        a Basic Authentication
        """
        if authorization_header is None or not isinstance(authorization_header,
                                                          str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        base64_credentials = authorization_header[6:]
        return base64_credentials

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str) -> str:  # nopep8
        """
        Args:
        base64_authorization_header(str):the base64_authorization_header

        Returns:
        returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None or not isinstance(base64_authorization_header, str):  # nopep8
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except base64.binascii.Error:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str) -> (str, str):  # nopep8
        """
        Args:
        decoded_base64_authorization_header: The decoded base64
        autorization header

        Returns:
        Returns the user email and password from the Base64 decoded
        value
        """
        if decoded_base64_authorization_header is None or not isinstance(decoded_base64_authorization_header, str):  # nopep8
            return (None, None)

        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(self,
                                     user_email: str, user_pwd: str) -> TypeVar('User'):  # nopep8
        """
        Args:
        user_email: E-mail of the user
        user_pwd: Password of the user

        Returns:
        Returns the User instance based on his email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        users = User.search({"email": user_email})
        if not users or users == []:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None
