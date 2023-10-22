from flask_restx import Namespace, Resource

ns = Namespace('mynamespace2', 'Namespace Description2')


@ns.route("/hello-ns2")
class Myclass(Resource):
    def get(self):
        return 'hello ns2'

    def post(self):
        raise Exception('Test Exception')
