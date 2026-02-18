from http import HTTPStatus

from fastapi.testclient import TestClient

from demo.app import app


def test_root():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"msg": "hello world"}


def test_document_request():
    client = TestClient(app)

    response = client.post(
        "/enrich",
        json={"documents": ["doc1", "doc2"], "flags": {"flag1": True, "flag2": False}},
    )

    assert response.status_code == HTTPStatus.OK
