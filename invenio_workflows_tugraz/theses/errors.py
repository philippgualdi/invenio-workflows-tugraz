# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-workflows-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Common Errors handling for Theses."""

from flask_babelex import lazy_gettext as _
from werkzeug.exceptions import HTTPException


class ThesesIDNotFoundError(HTTPException):
    """HTTP exception responsible for mapping search engine errors."""

    def __init__(self):
        """Parse RequestError."""
        self.code = 404
        super().__init__(description=_("Thesis id not found!"))
