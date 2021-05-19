import pytest

from tests.fixtures.client import db, restrict


@restrict.modal
class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    super = restrict.Permission("all")
    admin = restrict.Permission(["can_view", "can_update", "can_delete"])
    user = restrict.Permission(["can_view", "can_post"])


@restrict.modal
class CatModel(db.Model):
    __tablename__ = "cats"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    super = restrict.Permission("all")
    admin = restrict.Permission(["can_view", "can_update", "can_delete"])
    user = restrict.Permission(["can_view", "can_post"])
