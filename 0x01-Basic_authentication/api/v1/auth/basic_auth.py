#!/usr/bin/env python3
"""Basic route module for the API
"""
from api.v1.auth.auth import Auth
import base64
import binascii
from models.user import User


class BasicAuth(Auth):
    """Basic authentication class
    """

    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """returns the Base64 part of the Authorization
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
        """A method that decodes a base64 algorithm
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
        """ A method returns the user
        email and password from the Base64 decoded value.
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
            user_email: str, user_pwd: str) -> TypeVar('User'):
        """A method that returns
        the User instance based on his email and password.
        """
        if user_email is None:
            return None
        if user_pwd is None:
            return None
        users = User.search(email=user_email)

        # Check if a user is found
        if not users:
            return None

        # Validate password against the first matching user (assuming unique emails)
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None
