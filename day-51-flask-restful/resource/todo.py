from flask_restful import Resource, reqparse, abort, fields, marshal_with
from model.todomodel import ToDoModel
from flask_jwt_extended import jwt_required, get_jwt_identity

todo_req_parser = reqparse.RequestParser()
todo_req_parser.add_argument("description", required=True, help="description is mandatory")
todo_req_parser.add_argument("is_completed")

todo_fields = {
    "id": fields.Integer,
    "user_id": fields.Integer,
    "description": fields.String,
    "created_at": fields.DateTime,
    "last_modified_at": fields.DateTime,
    "is_completed": fields.Boolean
}


class ToDo(Resource):
    @jwt_required()
    @marshal_with(todo_fields)
    def get(self):
        return ToDoModel.get_todos_for_user(get_jwt_identity())

    @jwt_required()
    @marshal_with(todo_fields)
    def post(self):
        args = todo_req_parser.parse_args()
        todo = ToDoModel.get_by_description(args['description'])
        if todo:
            return abort(409, message="Todo with same description already exists")
        else:
            is_completed = bool(args.get("is_completed")) if args.get("is_completed") else False
            todo = ToDoModel(description=args['description'], user_id=get_jwt_identity(),
                             is_completed=is_completed)
            todo.add()
            return todo, 201

    @jwt_required()
    @marshal_with(todo_fields)
    def put(self, _id: int):
        args = todo_req_parser.parse_args()
        todo = ToDoModel.get_by_id(_id)
        if todo:
            if todo.user_id == int(get_jwt_identity()):
                todo.description = args['description']
                if args.get("is_completed"):
                    todo.is_completed = bool(args['is_completed'])
                todo.update()
            else:
                abort(401, message=f"Todo ID {_id} is not owned by you")
        else:
            is_completed = args.get("is_completed") if args.get("is_completed") else False
            todo = ToDoModel(description=args['description'], user_id=get_jwt_identity(),
                             is_completed=args.get("is_completed", is_completed))
            todo.add()
        return todo, 201

    @jwt_required()
    def delete(self, _id: int):
        todo = ToDoModel.get_by_id(_id)
        if todo:
            if todo.user_id == int(get_jwt_identity()):
                todo.delete()
                return {"message": "todo deleted successfully"}
            else:
                abort(401, message=f"Todo ID {_id} is not owned by you")
        else:
            return abort(404, message=f"Todo with ID {_id} doesn't exist")
