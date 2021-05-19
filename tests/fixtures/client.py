import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_restrict.restrict import Restrict

test_app = Flask(__name__)
test_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(test_app)

FLASK_RESTRICT_PERMS = [("super", 1), ("admin", 2), ("user", 3)]

restrict = Restrict()
restrict.init()


@test_app.route("/")
def home():
    return {
        "data": "results",
    }, 200


@pytest.fixture
def client():
    from tests.fixtures.models import UserModel, CatModel

    with test_app.test_client() as client:
        db.create_all()
        yield client
        # db.session.remove()
        # db.drop_all()
