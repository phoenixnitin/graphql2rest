authorizations = {
    'api_key': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'x-access-token'
    },
    'OAuth2': {
            'type': 'oauth2',
            'flow': 'implicit',
            'authorizationUrl': 'https://idp.example.com/authorize?audience=https://app.example.com',
            'clientId': 'MyClientId',
            'scopes': {
                'openid': 'Get ID token',
                'profile': 'Get identity',
                'read': 'Read',
                'write': 'Write',
            }
        }
}
