#!/usr/bin/env python3
"""
Module for basic Auth that inherits from Auth
"""
from api.v1.auth.auth import Auth
import base64


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
