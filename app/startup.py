from flask import Flask
from app.service.api_service import blueprint_v1, blueprint_v2
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# To be able to use flask sessions
app.secret_key = 'myapp'


app.config.SWAGGER_UI_OAUTH_CLIENT_ID = 'MyClientId'
app.config.SWAGGER_UI_OAUTH_REALM = '-'
app.config.SWAGGER_UI_OAUTH_APP_NAME = 'Demo'

app.register_blueprint(blueprint_v1)
app.register_blueprint(blueprint_v2)


@app.errorhandler(Exception)
def global_error_handler(e):

    if isinstance(e, HTTPException):
        return {"error": {'message': 'HTTPException', 'exception': str(e)}}
    return {"error": {'message': 'Other Exception', 'exception': str(e)}}


if __name__ == '__main__':
    app.run()
