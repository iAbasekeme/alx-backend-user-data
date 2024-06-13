#!/usr/bin/env python3
""" A module that tackles authentication
"""
import bcrypt


def _hash_password(password: str):
    """A function that takes a password and hashes the password
    """
    if password:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password
