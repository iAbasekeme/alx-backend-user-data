#!/usr/bin/env python3
"""A module that handles session authentication implementations
and holds the class Session auth.
"""
from .auth import Auth
import uuid


class SessionAuth(Auth):
    """A class that implements session authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """A method that creates a session for cookies
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
