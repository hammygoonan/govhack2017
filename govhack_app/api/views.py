#!/usr/bin/env python
"""Bottle views API endpoint."""

from flask import Blueprint
from flask import jsonify


api_blueprint = Blueprint(
    'api', __name__
    )


@api_blueprint.route('/')
def home():
    return jsonify({'message': 'Hello World'})
