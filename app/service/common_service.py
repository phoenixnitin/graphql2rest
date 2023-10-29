from functools import wraps
from flask import session, request, url_for
from uuid import uuid4


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        # print(*args.__dict__)
        print(request)
        print(request.headers)
        print(session)
        if 'logged_in' in session:
            request.user = {'uuid': str(uuid4()), 'scopes': ['get']}
            session.pop('logged_in')
            return f(*args, **kwargs)
        else:
            session['logged_in'] = True
            return 'login first at ' + url_for('api.path/myapi_hello'), 401
    return wrap


def required_scope(*scopes):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if len(set(request.user.get('scopes', list())).intersection(set(scopes))) > 0:
                return f(*args, **kwargs)
            return {'error': 'Unauthorized'}, 403
        return wrapper
    return decorator