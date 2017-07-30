#!/usr/bin/env python
"""
Basic CLI interfact for application.

To run application simply call manage.py followed by single argument which corresponds to
function name
"""

import sys
from govhack_app import create_app
# from data.lga import import_lga
# from data.example_data import example_data


def runserver():
    """Runs development server."""
    app = create_app('config.development')
    app.run()


def lga_data():
    """imports LGA data."""
    from data.lga import import_lga
    app = create_app('config.development')
    with app.app_context():
        import_lga()


def example():
    """imports LGA data."""
    from data.example_data import example_data
    app = create_app('config.development')
    with app.app_context():
        example_data()


def create_db():
    """imports LGA data."""
    from govhack_app import create_app
    from govhack_app import db
    from govhack_app.location.models import Lga, Postcode, Demand
    app = create_app('config.development')
    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    manage = sys.modules[__name__]
    if hasattr(manage, sys.argv[1]):
        result = getattr(manage, sys.argv[1])()
    else:
        raise ValueError('This operation does not exist')
