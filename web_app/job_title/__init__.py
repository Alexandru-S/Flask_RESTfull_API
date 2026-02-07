"""
The JobTitle Module.

This module contains the JobTitle Class and logic for the
executions to perform as requested.
"""
# coding=utf-8

from web_app import Resource
from web_app import auth
from web_app import abort
from .models import JOB_TITLE
from web_app.department.models import DEPARTMENT
from web_app.crud import list_all_join, find_by_join_2


class JobTitle(Resource):
    decorators = [auth.login_required]

    def get(self, var1=None):
        if var1 is None:
            """ Function activated when job_titles endpoint is passed
                :param model1: JOB_TITLE instance
                :param model2: DEPARTMENT instance
                :return: json
            """
            result = list_all_join(JOB_TITLE, DEPARTMENT)
            return result
        if var1 is not None:
            """ Function activated when job_titles argumentendpoint is passed
                :param model1: JOB_TITLE instance
                :param model2: DEPARTMENT instance
                :param var1: argument being department name
                :return: json
            """
            result = find_by_join_2(JOB_TITLE, DEPARTMENT, var1)
            if result is None or len(result) == 0:
                abort(422, message="Could not find any job_titles in that department")
            return result
        else:
            abort(404, message="Could not find data with that id")
