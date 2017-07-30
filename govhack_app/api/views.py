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


@api_blueprint.route('/age/<int:age>')
def filter(age):
    if age == 1:
        age = '0-4'
    if age == 5:
        age = '5-9'
    if age == 10:
        age = '10-14'
    postcodes = Demand.query.filter_by(age=age).all()
    return jsonify({'postcodes': [pcode.serialise() for pcode in postcodes]})


@api_blueprint.route('/postcode/<int:postcode>/age/<int:age>')
def postcode(postcode, age):
    if age == 1:
        age = '0-4'
    if age == 5:
        age = '5-9'
    if age == 10:
        age = '10-14'
    postcode = Demand.query.join(Postcode).filter(
        Postcode.postcode == postcode, Demand.age == age).first()
    # postcodes = Demand.query.all()
    # print([pcode.serialise() for pcode in postcodes])
    return jsonify(postcode.serialise())
    # return jsonify({'postcodes': [pcode.serialise() for pcode in postcodes]})
