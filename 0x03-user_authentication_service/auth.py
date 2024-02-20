#!/usr/bin/env python3
"""
The authentication module
"""

import bcrypt


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
