from flask_restx import Resource
from app.service import login_required


class Hello(Resource):
    @login_required
    def get(self):
        return {'result': 'hello resource'}

    @login_required
    def post(self):
        return {'result': 'hello post resource'}
