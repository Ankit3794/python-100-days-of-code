from flask import Flask
from flask_restful import Api
from resource.user import User, Login
import os
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PWD')}@{os.getenv('DB_URL')}:5432/flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")

jwt = JWTManager(app)
api = Api(app)

api.add_resource(User, '/user/<string:username>', '/user')
api.add_resource(Login, '/login')


@app.before_first_request
def create_db():
    db.create_all()


if __name__ == "__main__":
    from db import db

    db.init_app(app)
    app.run(debug=True)
