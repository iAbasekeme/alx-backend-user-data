#!/usr/bin/env python3
"""A module that holds a flask application
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def start():
    """A mehod that handles the root of a route
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
