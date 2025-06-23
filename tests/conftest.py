import pytest

from product_basket import Basket


@pytest.fixture
def basket():
    """Fixture for initializing an empty basket."""
    return Basket()
