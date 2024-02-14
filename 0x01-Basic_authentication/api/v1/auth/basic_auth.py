#!/usr/bin/env python3
"""
Module for basic Auth that inherits from Auth
"""
from api.v1.auth.auth import Auth


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
