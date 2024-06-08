#!/usr/bin/env python3
"""A class for managing the API authentication
"""
from typing import List, TypeVar
import requests
User = TypeVar('User')


class Auth:
    """A class that performs a simple authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """This method is a placeholder for future
        implementation of access control
        based on path and excluded paths. For now,
        it always returns False.
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Ensure path ends with a '/'
        normalized_path = path if path.endswith('/') else path + '/'

        # Check if the normalized path is in the excluded paths
        for excluded_path in excluded_paths:
            if normalized_path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """This method retrieves the authorization
        header from the Flask request object
        if provided. Otherwise, it returns None.
        """
        if request is not None:
            auth = requests.headers.get('Authorization', None)
        return auth

    def current_user(self, request=None) -> User:
        """This method is a placeholder for
        future implementation of user retrieval
        based on the authorization header. For now,
        it always returns None.
        """
        return None
