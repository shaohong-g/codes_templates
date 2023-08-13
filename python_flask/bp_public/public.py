import jwt
from flask import Blueprint, jsonify, request, current_app
from common.utlis import test, create_jwt_token

public = Blueprint('public', __name__)

# /api/0/
@public.route('/')
def initialize_data():
    return jsonify({'message': 'Public Endpoint!', 'status': 200})




@public.route('/test', methods = ["GET", "POST", "PATCH"])
def publicTest():
    return test()

@public.route('/token', methods = ["GET"])
def getJwtToken():

    # Get information from args (can be from json as well)
    dict_data = dict(request.args)
    expiry_time = int(dict_data.get("expiry", 5))
    token = create_jwt_token(dict_data, expiry_time, current_app.config.get('SECRET_KEY', None))

    return {"token": token, "data": dict_data, "expiry_time": expiry_time, "Secret Key": current_app.config.get('SECRET_KEY')}

@public.route('/decode', methods = ["GET"])
def decodeToken():
    token = request.args.get("token")
    return jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])

