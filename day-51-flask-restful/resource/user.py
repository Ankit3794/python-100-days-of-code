from flask_restful import Resource, reqparse, fields, marshal_with, abort
from model.usermodel import UserModel
from flask_jwt_extended import create_access_token, jwt_required

post_put_req_parser = reqparse.RequestParser()
post_put_req_parser.add_argument("username", required=True, help="username is mandatory")
post_put_req_parser.add_argument("password", required=True, help="password is mandatory")

user_fields = {
    "username": fields.String,
    "password": fields.String
}


class User(Resource):
    @jwt_required()
    @marshal_with(fields=user_fields)
    def get(self, username: str = None):
        if username:
            user = UserModel.get_user_by_username(username)
            if user:
                return user
            else:
                return abort(404, message="user not found")
        else:
            return UserModel.get_all_users()

    @marshal_with(fields=user_fields)
    def post(self):
        args = post_put_req_parser.parse_args()
        user = UserModel.get_user_by_username(args.get("username"))
        if user:
            return abort(409, message="user already exists")
        else:
            user = UserModel(args.get("username"), args.get("password"))
            user.insert()
            return user, 201

    @jwt_required()
    def delete(self, username: str):
        user = UserModel.get_user_by_username(username)
        if user:
            user.delete()
            return {"message": "user deleted successfully"}
        else:
            return abort(404, message=f"{username} doesn't exist")

    @marshal_with(fields=user_fields)
    def put(self):
        args = post_put_req_parser.parse_args()
        user = UserModel.get_user_by_username(args.get("username"))
        if user:
            user.password = args["password"]
            user.update()
        else:
            user = UserModel(args["username"], args["password"])
            user.insert()
        return user, 201


class Login(Resource):
    def post(self):
        args = post_put_req_parser.parse_args()
        user = UserModel.get_user_by_username(args["username"])
        if user.password != args["password"]:
            return abort(401, message="credentials didn't match")
        access_token = create_access_token(identity=user.username)
        return {"message": "login successfully", "auth": access_token}
