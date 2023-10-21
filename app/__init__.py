from flask import Flask
from .extensions import api, jwt #, blueprint
from .resources import ns1
from flask_jwt_extended import jwt_required

def create_app():
    app = Flask(__name__)

    app.config['JWT_SECRET_KEY'] = 'thisisasecret'

    app.config.SWAGGER_UI_OAUTH_CLIENT_ID = 'MyClientId'
    app.config.SWAGGER_UI_OAUTH_REALM = '-'
    app.config.SWAGGER_UI_OAUTH_APP_NAME = 'Demo'

    api.init_app(app)
    api.authorizations = {
        'OAuth2': {
            'type': 'oauth2',
            'flow': 'implicit',
            'authorizationUrl': 'https://idp.example.com/authorize?audience=https://app.example.com',
            'clientId': app.config.SWAGGER_UI_OAUTH_CLIENT_ID,
            'scopes': {
                'openid': 'Get ID token',
                'profile': 'Get identity',
            }
        },
        'jsonWebToken': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    }
    jwt.init_app(app)
    api.add_namespace(ns1)

    @app.before_request
    def before():
        jwt_required()

    # app.register_blueprint(blueprint)

    return app