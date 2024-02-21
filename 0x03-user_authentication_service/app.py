#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask, jsonify, request, abort, redirect, url_for
from auth import Auth

app = Flask(__name__)
Auth = Auth()


@app.route("/", methods=["GET"])
def index():
    """home"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user():
    """Register user"""
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        Auth.register_user(email, password)
        return jsonify({"email": "<registered email>", "message": "user created"})  # nopep8
    except ValueError:
        return jsonify({"message": "email already registered"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")