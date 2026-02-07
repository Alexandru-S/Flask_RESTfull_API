"""
The CRUD Module

This module uses sqlalchemy and flask_sqlalchemy as an ORM to
perform SQL queries on the instances retrieved and convert them to
json objects.
"""

import json
import datetime
import requests
from web_app import db
from sqlalchemy import and_, or_


def add_keys_helper(model2, model3, result):
    query2 = dict(model2.query.with_entities(model2.job_title_code, model2.job_title_name).distinct().all())
    for x in result:
        if 'job_title_code' in x.keys():
            x['job_title'] = query2[x['job_title_code']]
            x.pop('job_title_code')

        if 'job_title' in x.keys():
            dep_code = model2.query.filter(model2.job_title_name == x['job_title']).first().department_code
            dep_name = model3.query.filter(model3.department_code == dep_code).first().department_name
            x['department_name'] = dep_name
    return result


def date_converter(o):
    """ Function converts instance where date format is present to string
        :param o: DB instance
        :return: str
    """
    if isinstance(o, datetime.date):
        return o.__str__()


def from_sql(row):
    """ Function converts DB instance to json object
        :param row: DB instance
        :return: json
    """
    data = row.__dict__.copy()
    data.pop('_sa_instance_state')
    new_data = json.dumps(data, default=date_converter)
    new_new_data = json.loads(new_data)
    if 'country_code' in new_new_data.keys():
        URL = ('https://restcountries.eu/rest/v2/alpha?codes={code1};{code1};{code1}').format(code1=row.country_code)
        data = requests.get(url=URL).json()
        new_new_data['country'] = data[0]['name']
        new_new_data.pop('country_code')
    return new_new_data


def list_all(model):
    query = model.query.all()
    result = list(map(from_sql, query))
    return result


def list_all_employees(model1, model2, model3):
    query = model1.query.all()
    result = add_keys_helper(model2, model3, list(map(from_sql, query)))
    return result


def list_all_join(model1, model2):
    query = db.session.query(model1).filter(model2.department_code == model1.department_code).all()
    result = list(map(from_sql, query))
    query2 = dict(model2.query.with_entities(model2.department_name, model2.department_code).distinct().all())
    for x in result:
        if 'department_code' in x.keys():
            x['department_name'] = list(query2.keys())[list(query2.values()).index(x['department_code'])]
            x.pop('department_code')
    return result


def list_with_number(model, keyz, varnum):
    query = model.query.filter(keyz == varnum).all()
    result = list(map(from_sql, query))
    return result


def list_with_var1(model, keyz, date_limit, var1):
    query = model.query.filter(and_(keyz == var1, date_limit > datetime.date.today())).all()
    result = list(map(from_sql, query))
    return result


def check_with_var1(model, model2, model3, date_limit, var1):
    query = model.query.filter(or_(date_limit == var1, date_limit < datetime.date.today())).all()
    result = add_keys_helper(model2, model3, list(map(from_sql, query)))
    return result


def find_by_join(model1, model2, model3, var2):
    query = db.session.query(model1).filter(model3.department_name == var2).filter(model3.department_code == model2.department_code).filter(model2.job_title_code == model1.job_title_code).all()
    result = add_keys_helper(model2, model3, list(map(from_sql, query)))
    return result


def find_by_join_2(model1, model2, var1):
    query = db.session.query(model1).filter(model2.department_name == var1).filter(model2.department_code == model1.department_code).all()
    result = list(map(from_sql, query))
    query2 = dict(model2.query.with_entities(model2.department_name, model2.department_code).distinct().all())
    for x in result:
        if 'department_code' in x.keys():
            x['department_name'] = list(query2.keys())[list(query2.values()).index(x['department_code'])]
            x.pop('department_code')
    return result
