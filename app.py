from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_mysqldb import MySQL
from config import Config
from user_routes import user_blueprint
from book_routes import book_blueprint


app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)

jwt = JWTManager(app)

app.register_blueprint(user_blueprint, url_prefix='/api/user')
app.register_blueprint(book_blueprint, url_prefix='/api/book')


if __name__ == "__main__":
    app.run(host="localhost", port=int("3000"))
