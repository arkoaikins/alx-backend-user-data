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
        session_cookie = self.session_cookie(request)
        if session_cookie:
            user_id = self.user_id_for_session_id(session_cookie)
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """
        Deletes the user session/logout
        """
        if request is None or not self.session_cookie(request):
            return False
        session = self.session_cookie(request)
        if not self.user_id_for_session_id(session):
            return False
        del self.user_id_by_session_id[session]
        return True
