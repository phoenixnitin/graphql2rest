from functools import wraps
from flask import session, request, url_for


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        # print(*args.__dict__)
        print(request)
        if 'logged_in' in session:
            session.pop('logged_in')
            return f(*args, **kwargs)
        else:
            session['logged_in'] = True
            return 'login first at ' + url_for('api.path/myapi_hello'), 401
    return wrap
