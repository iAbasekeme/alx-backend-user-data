#!/usr/bin/env python3
"""A module that holds a flask application
"""
from flask import Flask, jsonify, request
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def start():
    """A mehod that handles the root of a route
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register() -> str:
    """A route that implements registering users and saving them.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or password is None:
        return jsonify({"message": "Input your email and password"}), 400
    try:
        Auth.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")