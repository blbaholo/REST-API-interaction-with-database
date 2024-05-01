import pytest
import json
from src import create_app
from src.models import db


@pytest.fixture()
def app():
    app = create_app(test_config=True)
    ctx = app.app_context()
    ctx.push()
    db.create_all()
    session = db.session
    session.bind = db.engine
    yield app
    session.remove()
    db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def post_request_add_new_computer(client):
    computer_details_dict = {
        "hard_drive_type": "SSD",
        "processor": "Intel Core i7 7202UD",
        "ram_amount": 4,
        "maximum_ram": 8,
        "hard_drive_space": 512,
        "form_factor": "Mini-ITX",
    }
    return client.post("/computers/", json=computer_details_dict)


def decode_json_data(response):
    return json.loads(response.data.decode("utf8"))


def test_list_computers(client, post_request_add_new_computer):
    post_request_add_new_computer
    response = client.get("/computers")
    assert response.status_code == 200
    assert [
        {
            "form_factor": "Mini-ITX",
            "hard_drive_space": 512,
            "hard_drive_type": "SSD",
            "id": 1,
            "maximum_ram": 8,
            "processor": "Intel Core i7 7202UD",
            "ram_amount": 4,
        }
    ] == decode_json_data(response)


def test_add_computers(post_request_add_new_computer):
    response = post_request_add_new_computer
    assert response.status_code == 200
    assert "MESSAGE: Computer details successfully added" in response.text


def test_delete_computer(post_request_add_new_computer, client):
    post_request_add_new_computer
    response = client.delete("/computers/1")
    assert response.status_code == 200
    assert "MESSAGE: Computer entry successfully deleted" in response.text


def test_update_computer(post_request_add_new_computer, client):
    post_request_add_new_computer
    response = client.patch("/computers/1", json={"hard_drive_type": "HDD"})
    assert response.status_code == 200
    assert {
        "form_factor": "Mini-ITX",
        "hard_drive_space": 512,
        "hard_drive_type": "HDD",
        "id": 1,
        "maximum_ram": 8,
        "processor": "Intel Core i7 7202UD",
        "ram_amount": 4,
    } == decode_json_data(response)
