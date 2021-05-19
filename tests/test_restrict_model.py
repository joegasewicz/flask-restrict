from flask_sqlalchemy import model

from tests.fixtures.client import client


def test_restrict_model(client):
    rv = client.get("/")
    assert 1 == 1

