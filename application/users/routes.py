from flask import Blueprint

users = Blueprint('users', __name__)

@users.route('/')
def index():
    return "<h1>hello world</h1>"