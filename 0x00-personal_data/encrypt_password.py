#!/usr/bin/env python3
"""Module that encrypts password"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Encrypts passwords"""
    mypassword = password.encode('utf-8')
    return bcrypt.hashpw(mypassword, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """checks validity of password"""
    mypassword = password.encode('utf-8')
    return bcrypt.checkpw(mypassword, hashed_password)
