"""The Badge Module.

This module contains the Badge Class and logic for the
executions to perform as requested.
"""
# coding=utf-8

from flask_restful import Resource, reqparse, abort
from web_app import auth
from .models import BADGE
from web_app.crud import list_all, list_with_var1, list_with_number


db_get_args = reqparse.RequestParser()
db_get_args.add_argument(
    "badge_number",
    type=int,
    help="Value of key not int")  # sets arguments to look for


class Badge(Resource):
    decorators = [auth.login_required]

    def get(self, var1=None):
        args = db_get_args.parse_args()  # parses arguments passed

        if args.badge_number is not None:
            """
            If badge number was passed
                :param model: BADGE instance
                :param value: BADGE badge_number #for comparison
                :param args: number passed from url
                :return:
                    if found:
                    :return: json
                    else:
                    :return: error
            """
            result = list_with_number(BADGE,
            BADGE.badge_number,
            args.badge_number)
            if result is None or len(result) == 0:
                abort(404, message="Could not find any badges with that id")
            return result

        if var1 is None:
            '''
            If viewing all badges, use the list_all function
                :param model: BADGE instance
                :return: json
            '''
            result = list_all(BADGE)
            return result

        if var1 == 'active':
            result = list_with_var1(
                BADGE,
                BADGE.badge_status,
                BADGE.badge_expiry_date,
                "Active")
            """
            If active parameter passed
                :param model: BADGE instance
                :param value: BADGE status #for comparison
                :param value: BADGE expiry date #for comparison
                :param args: string passed from url
                :return:
                    if found:
                    :return: json
                    else:
                    :return: error
            """
            if result is None or len(result) == 0:
                abort(404, message="Could not find any active badges")
            return result
        else:
            abort(404, message="Could not find data with that id")
