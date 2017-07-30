#!/usr/bin/env python
"""API endpoint."""

from flask import Blueprint
from flask import jsonify
from govhack_app.location.models import Postcode


api_blueprint = Blueprint(
    'api', __name__
    )


@api_blueprint.route('/')
def index():
    postcodes = Postcode.query.all()
    return jsonify({'postcodes': [pcode.serialise() for pcode in postcodes]})


@api_blueprint.route('/age/<age>')
def filter(age):
    postcodes = Postcode.query.all()
    return jsonify({'postcodes': [pcode.serialise() for pcode in postcodes]})


@api_blueprint.route('/postcode/<postcode>/age/<age>')
def postcode(postcode, age):
    postcode = Postcode.query.filter_by(postcode=postcode).first()
    return jsonify(postcode.serialise())
