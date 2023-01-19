import pytest
import os
from main import app
from db import db


@pytest.fixture(scope="session")
def client():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    app.config.update({
        'SQLALCHEMY_DATABASE_URI': f"sqlite:///{os.path.join(base_dir, 'test.db')}",
        'JWT_SECRET_KEY': 'test',
        'TESTING': True,
        'DEBUG': True
    })
    db.init_app(app)
    with app.app_context():
        db.create_all()
    client = app.test_client()
    yield client
    with app.app_context():
        db.drop_all()
