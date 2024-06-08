#!/usr/bin/env python3
"""Basic route module for the API
"""
from api.v1.auth.auth import Auth

class BasicAuth:
    """Basic authentication class
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """returns the Base64 part of the Authorization
        header for a Basic Authentication
        """
        startWithBasic = authorization_header.startswith('Basic ')
        if authorization_header and isinstance(authorization_header, str) and startWithBasic:
            return startWithBasic[6:]
        return None