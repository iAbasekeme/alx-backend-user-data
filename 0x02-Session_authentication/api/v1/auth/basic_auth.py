#!/usr/bin/env python3
"""Basic route module for the implementations of autthentication API
"""
import base64
import binascii
from typing import TypeVar

from .auth import Auth
from models.user import User


class BasicAuth(Auth):
    """Basic authentication class that inherits from the Auth class
    """

    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:

        """A method that returns the Base64 part of the Authorization
        header for a Basic Authentication
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        # Check if header starts with "Basic " (case-insensitive)
        if not authorization_header.lower().startswith("basic "):
            return None

        # Extract the Base64 part after skipping "Basic "
        return authorization_header[6:].strip()

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:

        """A method that that returns the decoded value of a
        Base64 string base64_authorization_header:
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            res = base64.b64decode(
                base64_authorization_header,
                validate=True
            )
            return res.decode('utf-8')
        except (binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
            ) -> (str, str):

        """A method returns the user email and password from
        the Base64 decoded value.
        """
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if decoded_base64_authorization_header is None:
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        email, password = decoded_base64_authorization_header.split(':', 1)
        return (email, password)

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):

        """Retrieves a user based on the user's authentication credentials.
        """
        if type(user_email) == str and type(user_pwd) == str:
            try:
                users = User.search({'email': user_email})
            except Exception:
                return None
            if len(users) <= 0:
                return None
            if users[0].is_valid_password(user_pwd):
                return users[0]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """A class that overloads Auth and retrieves the
        User instance for a request:
        """
        auth_header = self.authorization_header(request)
        b64_auth_token = self.extract_base64_authorization_header(auth_header)
        auth_token = self.decode_base64_authorization_header(b64_auth_token)
        email, password = self.extract_user_credentials(auth_token)
        return self.user_object_from_credentials(email, password)
