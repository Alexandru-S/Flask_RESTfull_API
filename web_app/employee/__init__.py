"""The Employee Module.

This module contains the Employee Class and logic for the
executions to perform as requested.
"""
# coding=utf-8


from flask_restful import Resource, abort, reqparse
from .models import EMPLOYEE
from web_app.job_title.models import JOB_TITLE
from web_app.department.models import DEPARTMENT
from web_app.crud import check_with_var1, find_by_join, list_all_employees
from web_app import auth


db_get_args = reqparse.RequestParser()
db_get_args.add_argument("department_name",
type=str,
help="Value of key not int")


class Employee(Resource):
    decorators = [auth.login_required]

    def get(self, var1=None):
        args = db_get_args.parse_args()
        if args.department_name is not None:
            """ Function activated when employees endpoint is passed and
               department_name is given.
                :param model: EMPLOYEE instance
                :param model: JOB_TITLE instance
                :param model: DEPARTMENT instance
                :param var1: department_name as string
                :return: json
            """
            result = find_by_join(
                EMPLOYEE, JOB_TITLE, 
                DEPARTMENT, 
                args.department_name)
            if result is None or len(result) == 0:
                abort(422, message="No employees found in that department")
            return result
        if var1 is None:
            """ Function activated when employees endpoint is passed and
                we only want a list of all employees returned back
                :param model: EMPLOYEE instance
                :param model: JOB_TITLE instance
                :param model: DEPARTMENT instance
                :return: json
            """
            result = list_all_employees(EMPLOYEE, JOB_TITLE, DEPARTMENT)
            return result
        if var1 == 'active':
            """ Function activated when employees endpoint is passed and
               active argument is given
                :param model: EMPLOYEE instance
                :param model: JOB_TITLE instance
                :param model: DEPARTMENT instance
                :param var1: active argument as string
                :return: json
            """
            result = check_with_var1(EMPLOYEE,
            JOB_TITLE,
            DEPARTMENT,
            EMPLOYEE.leave_date,
            None)
            if result is None or len(result) == 0:
                abort(404, message="Could not find any active employees")
            return result
        else:
            abort(404, message="Could not find data with that id")
