#!/usr/bin/env python
"""
Basic CLI interfact for application.

To run application simply call manage.py followed by single argument which corresponds to
function name
"""

import sys
from govhack_app import create_app


def runserver():
    """Runs development server."""
    app = create_app('config.development')
    app.run()


if __name__ == "__main__":
    manage = sys.modules[__name__]
    if hasattr(manage, sys.argv[1]):
        result = getattr(manage, sys.argv[1])()
    else:
        raise ValueError('This operation does not exist')
