from fastapi.testclient import TestClient
from ..controllers import orders as controller
from ..main import app
import pytest
from ..models import orders as model
from ..controllers import customer as controller
from ..models import customers as model
from fastapi import HTTPException

client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_read_all_customers(db_session):
    customer_data_1 = {
        "id": 1,
        "name": "Jane Smith",
        "phone": "704-555-9876",
        "email": "jane@example.com",
        "address": "456 Oak Ave",
        "card_type": "Mastercard",
        "card_number": "5555666677778888"
    }
    customer_data_2 = {
        "id": 2,
        "name": "Bob Jones",
        "phone": "704-555-1111",
        "email": "bob@example.com",
        "address": "789 Pine Rd",
        "card_type": "Visa",
        "card_number": "4444333322221111"
    }

    fake_customers = [model.Customer(**customer_data_1), model.Customer(**customer_data_2)]
    db_session.query.return_value.all.return_value = fake_customers

    result = controller.read_all(db_session)

    assert result is not None
    assert len(result) == 2
    assert result[0].name == "Jane Smith"
    assert result[1].name == "Bob Jones"


def test_read_one_customer(db_session):
    customer_data = {
        "id": 1,
        "name": "Jane Smith",
        "phone": "704-555-9876",
        "email": "jane@example.com",
        "address": "456 Oak Ave",
        "card_type": "Mastercard",
        "card_number": "5555666677778888"
    }

    customer_object = model.Customer(**customer_data)
    db_session.query.return_value.filter.return_value.first.return_value = customer_object

    result = controller.read_one(db_session, item_id=1)

    assert result is not None
    assert result.id == 1
    assert result.name == "Jane Smith"
    assert result.email == "jane@example.com"
