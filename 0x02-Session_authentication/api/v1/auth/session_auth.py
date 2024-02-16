#!/usr/bin/env python3
"""
New authentication mechanism
SessionAuth that interits from Auth

"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """new authentication mechanism"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a user_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        returns a User ID based on Session ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        returns a User instance based on cookie value
        """
        cookie_value = self.session_cookie(request, '_my_session_id')
        if cookie_value is None:
            return None

        user_id = self.user_id_for_session_id(cookie_value)
        if user_id is None:
            return None

        return User.get(user_id)
