#!/usr/bin/env python
"""API endpoint."""

from flask import Blueprint
from flask import jsonify
from govhack_app.location.models import Demand, Postcode


api_blueprint = Blueprint(
    'api', __name__
    )


@api_blueprint.route('/')
def index():
    postcodes = Demand.query.all()
    return jsonify({'postcodes': [pcode.serialise() for pcode in postcodes]})


@api_blueprint.route('/age/<age>')
def filter(age):
    postcodes = Demand.query.filter_by(age=age).all()
    return jsonify({'postcodes': [pcode.serialise() for pcode in postcodes]})


@api_blueprint.route('/postcode/<int:postcode>/age/<age>')
def postcode(postcode, age):
    postcode = Demand.query.join(Postcode).filter(
        Postcode.postcode == postcode, Demand.age == age).first()
    return jsonify(postcode.serialise())
