from flask_restx import Namespace
from app.resource import Hello

ns = Namespace('path/myapi', 'All api')
ns.add_resource(Hello, '/hello-ns1')
