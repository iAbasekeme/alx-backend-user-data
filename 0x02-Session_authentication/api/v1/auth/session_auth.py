#!/usr/bin/env python3
"""A module that handles session authentication implementations
and holds the class Session auth.
"""
from .auth import Auth
import uuid
from models.user import User

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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """A method that that returns a User ID based
        on a Session ID:
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """A method that returns a User instance based on a cookie value
        """
        if request is None:
            return None
        session_id = Auth.session_cookie(request)
        if not session_id:
            return None
        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return None
        user = User.get(user_id)
        return user
