from flask_restx import Resource, Namespace
from flask_jwt_extended import jwt_required, get_jwt_identity

ns1 = Namespace("ns1", security='jsonWebToken')

@ns1.route("/hello")
class Hello(Resource):
    method_decorators = [jwt_required()]

    # @ns1.doc(security='jsonWebToken')
    def get(self):
        print(get_jwt_identity())
        return {'hello': 'restx'}