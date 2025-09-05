import sys
import os

# ensure project root is in PYTHONPATH *before* importing app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_add(client):
    res = client.get("/add?a=2&b=3")
    assert res.get_json()["result"] == 5


def test_subtract(client):
    res = client.get("/subtract?a=5&b=2")
    assert res.get_json()["result"] == 3


def test_multiply(client):
    res = client.get("/multiply?a=4&b=3")
    assert res.get_json()["result"] == 12


def test_divide(client):
    res = client.get("/divide?a=6&b=2")
    assert res.get_json()["result"] == 3


def test_divide_by_zero(client):
    res = client.get("/divide?a=6&b=0")
    assert res.status_code == 400
