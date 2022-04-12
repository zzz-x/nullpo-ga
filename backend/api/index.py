from flask import make_response, render_template, session
from flask_restful import Resource

from .utils import authz_required


class Index(Resource):
    @authz_required
    def get(self):
        casdoorUser = session.get('casdoorUser')
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html', title='title', username=casdoorUser.get('name')), 200, headers)
