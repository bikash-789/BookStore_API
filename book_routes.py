from flask import Blueprint, jsonify, make_response
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_mysqldb import MySQL

mysql = MySQL()

book_blueprint = Blueprint('book', __name__)

@book_blueprint.route('/books', methods=['GET'])
def getAllBooks():
    msg = ""
    return make_response(jsonify({'message' : msg}))



@book_blueprint.route('/book', methods=['POST'])
def insertBook():

    return 

