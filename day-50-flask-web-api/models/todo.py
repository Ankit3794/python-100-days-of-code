from flask_restful import Resource, reqparse, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

db = SQLAlchemy()


class ToDo(db.Model):
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)


todo_post_parser = reqparse.RequestParser()
todo_post_parser.add_argument("description", type=str, help="Todo description", required=True)


class ToDoSimple(Resource):
    @marshal_with({"id": fields.Integer, "description": fields.String})
    def get(self):
        return ToDo.query.all()

    @marshal_with({"id": fields.Integer, "description": fields.String})
    def post(self):
        args = todo_post_parser.parse_args()
        todo = ToDo(description=args["description"])
        db.session.add(todo)
        db.session.commit()
        return todo, 201


