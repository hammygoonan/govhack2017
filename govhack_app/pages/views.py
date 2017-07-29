#!/usr/bin/env python
"""Pages endpoint."""

from flask import Blueprint
from flask import render_template


pages_blueprint = Blueprint(
    'pages', __name__, template_folder='templates'
    )


@pages_blueprint.route('/')
def home():
    return render_template('pages/index.html')
