from flask_restx import Resource
from app.service import login_required, required_scope
from flask import request


class Hello(Resource):
    @login_required
    @required_scope('get')
    def get(self):
        print(request.user)
        return {'result': 'hello resource', **request.user}

    @login_required
    @required_scope('post')
    def post(self):
        print(request.user)
        return {'result': 'hello post resource', **request.user}
