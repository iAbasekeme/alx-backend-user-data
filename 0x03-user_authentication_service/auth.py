#!/usr/bin/env python3
""" A module that tackles authentication
"""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """A function that takes a password and hashes the password
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        user = self._db.find_user_by(email=email)
        if user:
            raise ValueError('User ${email} already exists')
        else:
            hashed_password =  _hash_password(password)
            self._db.add_user(email, hashed_password)
