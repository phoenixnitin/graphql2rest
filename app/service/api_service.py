from flask import Blueprint
from flask_restx import Api
from app.configuration import authorizations
from app.namespace import ns1, ns2

blueprint_v1 = Blueprint('api', __name__, url_prefix='/api/v1')

api_v1 = Api(blueprint_v1,
             authorizations=authorizations,
             title='My Title',
             version='1.0',
             description='A description',
             # All API metadatas
             security=['api_key', {'OAuth2': ['read', 'write']}],
             doc='swagger'
             )
api_v1.add_namespace(ns1)


@blueprint_v1.before_request
def before_request():
    print('Before blueprint v1')


blueprint_v2 = Blueprint('api2', __name__, url_prefix='/api/v2')
api_v2 = Api(blueprint_v2,
             title='My Title',
             version='1.0',
             description='A description',
             # All API metadatas
             )
api_v2.add_namespace(ns2)


@blueprint_v2.before_request
def before_request():
    print('Before blueprint v2')
