from fastapi.testclient import TestClient
from ..controllers import orders as controller
from ..main import app
import pytest
from ..models import orders as model
from ..models import customers as customer_model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_order(db_session):
    # Create a sample order
    order_data = {
        "customer_name": "John Doe",
        "customer_id": 1,
        "description": "Test order"
    }

    order_object = model.Order(**order_data)

    # Mock customer lookup so controller.create() sees a valid customer
    db_session.query.return_value.filter.return_value.first.return_value = customer_model.Customer(
        id=1,
        name="John Doe",
        phone="919-555-1234",
        email="john@example.com",
        address="123 Test St",
        card_type="Visa",
        card_number="1111222233334444"
    )

    # Call the create function
    created_order = controller.create(db_session, order_object)

    # Assertions
    assert created_order is not None
    assert created_order.customer_name == "John Doe"
    assert created_order.customer_id == 1
    assert created_order.description == "Test order"
