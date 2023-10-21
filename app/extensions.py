from flask import Blueprint
from flask_restx import Api
from flask_jwt_extended import JWTManager

# blueprint = Blueprint('swagger', __name__, url_prefix='/swagger')
# api = Api(blueprint, doc='/doc/')
api = Api(security='jsonWebToken')
jwt = JWTManager()
