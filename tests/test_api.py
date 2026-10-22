from http import HTTPStatus

import httpx
from fastapi.testclient import TestClient

from api import app

client = TestClient(app)


def get_fib(n: int | str) -> httpx.Response:
    return client.get(f"/api/v1/fibonacci/{n}")


def test_fibonacci_happy_path():
    response = get_fib(5)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == [0, 1, 1, 2, 3]


def test_fibonacci_negative_number():
    response = get_fib(-10)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_fibonacci_non_numeric():
    response = get_fib("tomato")
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
