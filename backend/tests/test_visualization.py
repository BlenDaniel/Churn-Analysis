import pytest
from fastapi.testclient import TestClient

def test_draw_graphs(client: TestClient):
    response = client.get("/visualization/draw_graphs/")
    assert response.status_code == 200
    assert response.json() == {"message": "Graphs drawn successfully."}
