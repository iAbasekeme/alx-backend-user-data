#!/usr/bin/env python3
"""Basic route module for the API
"""
from api.v1.auth.auth import Auth
import base64
import binascii

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
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            res =  base64.b64decode(
                base64_authorization_header,
                validate=True
            )
            return res.decode('utf-8')
        except (binascii.Error, UnicodeDecodeError):
            return None
