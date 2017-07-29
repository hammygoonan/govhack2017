#!/usr/bin/env python
"""Bottle views API endpoint."""

from flask import Blueprint
from flask import jsonify
from govhack_app.location.models import Postcode


api_blueprint = Blueprint(
    'api', __name__
    )


@api_blueprint.route('/')
def home():
    postcodes = Postcode.query.all()
    return jsonify({'postcodes': [pcode.serialise() for pcode in postcodes]})
