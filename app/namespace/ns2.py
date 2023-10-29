from flask_restx import Namespace, Resource
import socket


ns = Namespace('mynamespace2', 'Namespace Description2')


@ns.route("/hello-ns2")
class Myclass(Resource):
    def get(self):
        return {'message': 'hello ns2', 'hostname': socket.gethostname()}, 200

    def post(self):
        raise Exception('Test Exception')
