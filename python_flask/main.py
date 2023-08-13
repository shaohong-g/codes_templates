import uuid
from flask import Flask, jsonify #, make_response, request
from flask_cors import CORS
# import jwt
# from datetime import datetime, timedelta
# from functools import wraps
# from werkzeug.security import generate_password_hash, check_password_hash

# from utils import config, create_jwt_token, setup
# from models import db_session, Company, Client, Investor, Transactions, ReturnDebt

app = Flask(__name__)
cors = CORS(app)

##########################################
# Secret Key for jwt token
##########################################
app.config['SECRET_KEY'] = uuid.uuid4().hex


##########################################
# Exception Handlers
##########################################
# Return this if we return InvalidAPIUsage Object
import json
from common.custom_exception import InvalidAPIUsage
from werkzeug.exceptions import HTTPException

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(e):
    print(e.get_response(), "test")

    return jsonify(e.to_dict()), e.status_code

##########################################
# import all blueprints
##########################################
from bp_private.private import private
from bp_public.public import public

# register all blueprints
app.register_blueprint(private, url_prefix='/api/1')
app.register_blueprint(public, url_prefix='/api/0')


##########################################
# Healthcheck
##########################################
@app.route('/health')
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(port=8000, debug=True, host='0.0.0.0')