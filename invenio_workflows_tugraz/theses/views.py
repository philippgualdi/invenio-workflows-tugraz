# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
#
# Copyright (C) 2021 Graz University of Technology.
#
# Invenio-Records-Marc21 is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.


"""Blueprint definitions."""

from flask import Blueprint, redirect, render_template

from .decorators import pass_record_from_pid
from .errors import ThesesIDNotFoundError


@pass_record_from_pid
def record_from_pid(record=None, **kwargs):
    """Redirect to record's latest version page."""
    return redirect(record["links"]["self_html"], code=301)


def handle_thesis_id_not_found_exception(e):
    """Function: handle_thesis_id_not_found_exception render template for a requested thesis."""
    return (
        render_template(
            "invenio_workflows_theses/thesis_not_found.html",
            code=e.code,
            description=e.description,
        ),
        e.code,
    )


def create_blueprint(app):
    """Register blueprint routes on app."""
    blueprint = Blueprint(
        "invenio_workflows_tugraz_theses",
        __name__,
        url_prefix="/theses",
        template_folder="templates/",
    )

    blueprint.add_url_rule("/<path:pid_value>", view_func=record_from_pid)
    app.register_error_handler(
        ThesesIDNotFoundError, handle_thesis_id_not_found_exception
    )
    return blueprint
