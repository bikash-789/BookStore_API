from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_mysqldb import MySQL
from flask_mysqldb import MySQLdb

user_blueprint = Blueprint('user', __name__)
mysql = MySQL()

@user_blueprint.route('/login', methods=['POST'])
def login():
    msg = 'Please register!'
    if request.is_json:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = %s AND password = %s', (email, password))
        account = cursor.fetchone()
        if account:
            access_token = create_access_token(identity=email)
            status_code = 200
            msg = 'Logged in successfully!'
            response = make_response(jsonify({'message': msg, 'access_token': access_token, 'email': email}), status_code)
        else:
            msg = 'Incorrect username / password !'
            status_code = 404
            response = make_response(jsonify({'message': msg}), status_code)
    return response

@user_blueprint.route('/register', methods=['POST'])
def register():
    msg = 'OK'
    if request.is_json:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = %s', (email,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        else:
            cursor.execute('INSERT INTO user (email, password) VALUES (%s, %s)', (email, password))
            mysql.connection.commit()
            msg = 'You have successfully been registered !'
    else:
        msg = 'Please provide JSON data.'
    return {'message': msg}
