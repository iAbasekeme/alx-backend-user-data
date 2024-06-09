#!/usr/bin/env python3
"""A module that implements session authentication for every user
that wants to login
"""
from os import getenv
from api.v1.views import app_views
from flask import jsonify, request
from views import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """A route that handles login for a user and
    creates a session for them
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or email == '':
        return jsonify({"error": "email missing"}), 400
    if not password or password == '':
        return jsonify({"error": "password missing"}), 400
    user = User.search({'email': email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    passw = user.is_valid_password(password)
    if passw:
        from api.v1.app import auth
        session_id = auth.create_session(getattr(user, id))
        res = jsonify(user.to_json())
        res.set_cookie(getenv("SESSION_NAME"), session_id)
        return res
    return jsonify({"error": "wrong password"})
