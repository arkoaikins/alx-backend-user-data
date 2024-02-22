#!/usr/bin/env python3
"""
The authentication module
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """
    hash password

    Args:
    password: a password string

    Return:
    Returns bytes
    """
    salt = bcrypt.gensalt()
    user_password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(user_password, salt)
    return hashed_password


def _generate_uuid() -> str:
    """
    Return string representation of a new
    uuid
    """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Checks if user alredy exists
        Args:
        Email: Users email
        Password: Users password

        Return:
        User object
        """
        try:
            existing_user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password).decode("utf-8")
            user = self._db.add_user(email, hashed_password)
            return user
        raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """
        Credentials validation
        Args:
        email: Email of the user
        Password: Password of the user

        Return"
        True if it a valid user else return false
        """
        try:
            user = self._db.find_user_by(email=email)
            password = password.encode('utf-8')
            if (type(user.hashed_password) == str):
                encode_hash = user.hashed_password.encode('utf-8')
            return bcrypt.checkpw(password, encode_hash)
        except NoResultFound:
            return False
