from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Boolean
from db import db
from datetime import datetime


class ToDoModel(db.Model):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True)
    description = Column(String(80), nullable=False)
    user_id = Column(Integer, ForeignKey("user.user_id"))
    created_at = Column(TIMESTAMP, nullable=False)
    last_modified_at = Column(TIMESTAMP, nullable=False, onupdate=datetime.utcnow)
    is_completed = Column(Boolean)

    def __init__(self, description, user_id, is_completed: bool):
        self.description = description
        self.user_id = user_id,
        self.created_at = datetime.utcnow()
        self.last_modified_at = datetime.utcnow()
        self.is_completed = is_completed

    @classmethod
    def get_by_id(cls, _id: int):
        return ToDoModel.query.filter_by(id=_id).first()

    @classmethod
    def get_by_description(cls, description: str):
        return ToDoModel.query.filter_by(description=description).first()

    @classmethod
    def get_todos_for_user(cls, user_id: int):
        return ToDoModel.query.filter_by(user_id=user_id).all()

    @classmethod
    def get_all_todos(cls):
        return ToDoModel.query.all()

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
