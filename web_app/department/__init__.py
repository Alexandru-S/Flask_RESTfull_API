"""The Department Module.

This module contains the Department Class and logic for the
executions to perform as requested.
"""
# coding=utf-8

from web_app import Resource
from web_app import auth
from web_app import abort
from .models import DEPARTMENT
from web_app.crud import list_all


class Department(Resource):
    decorators = [auth.login_required]

    def get(self):
        """Function activated when departments endpoint is passed
        :param model: DEPARTMENT instance
        :return: json
        """
        result = list_all(DEPARTMENT)
        if result is None or len(result) == 0:
            abort(404, message="Could not find any badges with that id")
        return result
