#!/usr/bin/env python3
""" Module of SessionAuth views
"""
from api.v1.views import app_views
from flask import jsonify, make_response, request, abort
from models.user import User
from os import getenv
from typing import Tuple


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login() -> str:
    """POST /api/v1/auth_session/login):"""
    email = request.form.get("email")
    password = request.form.get("password")
    if not email or email == '':
        return jsonify({"error": "email missing"}), 400
    if not password or password == '':
        return jsonify({"error": "password missing"}), 400
    try:
        users = User().search({"email": email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404
    if len(users) < 1:
        return jsonify({"error": "no user found for this email"}), 404
    if not users[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    session_id = auth.create_session(users[0].id)
    response = make_response(jsonify(users[0].to_json()))
    cookie = getenv('SESSION_NAME')
    response.set_cookie('_my_session_id', session_id)
    return response


@app_views.route(
    '/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout() -> Tuple[str, int]:
    """
    Deletes session ID
    """
    from api.v1.app import auth
    destroyed_session = auth.destroy_session(request)
    if not destroyed_session:
        abort(404)
    return jsonify({})
