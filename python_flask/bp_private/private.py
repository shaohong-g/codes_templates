import jwt
from flask import Blueprint, jsonify, request, current_app
from common.utlis import test, create_jwt_token, token_required

private = Blueprint('private', __name__)

# /api/1/

@private.route('/')
@token_required
def initialize_data(*args, **kwargs):
    return jsonify({'message': 'Private Endpoint!', 'status': 200, "args": args, "kwargs": kwargs})


