import jwt
from flask import jsonify, request, current_app
from datetime import datetime, timedelta
from functools import wraps

def test():
    """
    print(request.args)
    print(request.form)
    print(request.files)
    print(request.values)
    print(request.json)
    """
    result = {}

    result = {
        "Secret Key": current_app.config.get('SECRET_KEY'),
        "method": request.method,
        "content_type": request.content_type,
        "Authorization": request.headers.get("Authorization", None),
        "host": request.host,
        "path": request.path,
        "args": dict(request.args),
        "form" : dict(request.form),
        "values" : dict(request.values),
        "files": None
    }
    
    if request.content_type == "application/json":
        result["json"] = dict(request.json)

    if len(request.files) > 0 :
        filesDict = dict(request.files)
        for key in filesDict.keys():
            filesDict[key] = filesDict[key].filename
        result["files"] = filesDict

    return jsonify(result)

def create_jwt_token(dict_data, expiry_time=5, secret_key=None):
    """Create a JWT token
    :param dict_data: dict data to be encoded in the token
    :param expiry_time: token expiry time in minutes
    :param secret_key: secret key to encode the token
    :return: encoded token
    """
    dict_data['expiration'] = str(datetime.utcnow() + timedelta(minutes=expiry_time))
    print(secret_key)
    token = jwt.encode(dict_data, secret_key, algorithm='HS256')

    return token # token.decode('UTF-8')

def token_required(func):
    """Wrapper function for authentication"""
    @wraps(func)
    def decorated(*args, **kwargs):
        # token = request.args.get('token')

        token = None

        # Retrieve token from headers (might be in Authorization)
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing!', 'status': 401}), 401

        # Check and validate token
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            """
            e.g. {'user': 'admin', 'expiration': '2022-08-26 22:54:16.293247'}
            """
            exp = data.get("expiration")

            if exp is None or  datetime.strptime(exp, "%Y-%m-%d %H:%M:%S.%f") < datetime.utcnow():
                raise Exception("Token is None or passed the expiry time!")
            
        except Exception as e:
            return jsonify({'message': f'Invalid token: {e}', 'status': 401}), 401
        print(data)
        return func(data, *args, **kwargs)

    return decorated