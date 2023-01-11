from sqlalchemy import Column, Integer, String
from db import db


class UserModel(db.Model):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True)
    password = Column(String(12), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def get_user_by_username(cls, username: str):
        return UserModel.query.filter_by(username=username).first()

    @classmethod
    def get_all_users(cls):
        return UserModel.query.all()

    def insert(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
