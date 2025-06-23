from typing import Any, Hashable, Union

import pytest

from product_basket import Product


# Positive tests
def test_empty_basket_properties(basket):
    """
    Test for an empty basket.

    Verifies that:
    - Total price (total_price) is 0.
    - Total weight (total_weight) is 0.
    - Shipping cost (get_shipping_cost) is 0.
    - Final price (get_price) is 0.
    - List of products (list_products) is empty.
    """
    assert (
        basket.total_price == 0
    ), f"The total price of an empty basket should be 0, but got {basket.total_price}"
    assert (
        basket.total_weight == 0
    ), f"The total weight of an empty basket should be 0, but got {basket.total_weight}"
    assert (
        basket.get_shipping_cost == 0
    ), f"The shipping cost for an empty basket should be 0, but got {basket.get_shipping_cost}"
    assert (
        basket.get_price == 0
    ), f"The final price of an empty basket should be 0, but got {basket.get_price}"
    assert (
        basket.list_products == []
    ), f"The product list of an empty basket should be empty, but got {basket.list_products}"


import pytest


@pytest.mark.parametrize(
    "price, weight, expected_shipping_cost",
    [
        (300, 5, 250),
        (500, 10, 100),
    ],
)
def test_add_single_product(
    basket, price: int, weight: int, expected_shipping_cost: int
):
    """Test adding a single product with different characteristics and checking shipping cost."""
    product = Product("Hairdryer", price, weight)
    basket.add_product(product)

    assert (
        len(basket.list_products) == 1
    ), f"The number of products should be 1, but got {len(basket.list_products)}"
    assert (
        basket.total_price == price
    ), f"The total price should be {price} units, but got {basket.total_price}"
    assert (
        basket.total_weight == weight
    ), f"The total weight should be {weight} units, but got {basket.total_weight}"
    assert (
        basket.get_shipping_cost == expected_shipping_cost
    ), f"The shipping cost should be {expected_shipping_cost} units, but got {basket.get_shipping_cost}"
    assert (
        basket.get_price == price + expected_shipping_cost
    ), f"The final price should be {price + expected_shipping_cost} units, but got {basket.get_price}"


def test_delete_product(basket):
    """Test deleting a product from the basket."""
    product = Product("Vacuum Cleaner", 1200, 15)
    basket.add_product(product, 1)

    basket.delete_product(product.id)

    assert (
        len(basket.list_products) == 0
    ), f"The basket should be empty, but contains {len(basket.list_products)} products"
    assert (
        basket.total_price == 0
    ), f"The total price should be 0 units, but got {basket.total_price}"
    assert (
        basket.total_weight == 0
    ), f"The total weight should be 0 units, but got {basket.total_weight}"
    assert (
        basket.get_shipping_cost == 0
    ), f"The shipping cost should be 0 units, but got {basket.get_shipping_cost}"
    assert (
        basket.get_price == 0
    ), f"The final price should be 0 units, but got {basket.get_price}"


def test_add_product(basket):
    """Test adding a product to the basket, checking the final price, weight, product list, and shipping cost."""
    product = Product("Microwave", 500, 10)
    basket.add_product(product, 2)

    assert (
        len(basket.list_products) == 2
    ), f"The number of products in the basket should be 2, but got {len(basket.list_products)}"
    assert all(
        p.name == "Microwave" for p in basket.list_products
    ), "The basket should contain only microwaves"
    assert (
        basket.total_price == 1000
    ), f"The total price should be 1000 units, but got {basket.total_price}"
    assert (
        basket.total_weight == 20
    ), f"The total weight should be 20 units, but got {basket.total_weight}"
    assert (
        basket.get_shipping_cost == 0
    ), f"The shipping cost should be free (0 units), but got {basket.get_shipping_cost}"
    assert (
        basket.get_price == 1000
    ), f"The final price should be 1000 units, but got {basket.get_price}"


def test_add_multiple_products(basket):
    """Test adding multiple different products and verifying the final values."""
    tv = Product("TV", 800, 20)
    laptop = Product("Laptop", 1200, 5)
    phone = Product("iPhone", 700, 2)

    basket.add_product(tv, 1)
    basket.add_product(laptop, 1)
    basket.add_product(phone, 2)

    expected_price = 800 + 1200 + (700 * 2)
    expected_weight = 20 + 5 + (2 * 2)
    expected_shipping = 0

    assert (
        len(basket.list_products) == 4
    ), f"The number of products should be 4, but got {len(basket.list_products)}"
    assert (
        basket.total_price == expected_price
    ), f"The total price should be {expected_price} units, but got {basket.total_price}"
    assert (
        basket.total_weight == expected_weight
    ), f"The total weight should be {expected_weight} units, but got {basket.total_weight}"
    assert (
        basket.get_shipping_cost == expected_shipping
    ), f"The shipping cost should be {expected_shipping} units, but got {basket.get_shipping_cost}"
    assert (
        basket.get_price == expected_price
    ), f"The final price should be {expected_price} units, but got {basket.get_price}"


def test_sequential_usage(basket):
    """
    Test sequential usage of the basket:
    - Add several different products.
    - Remove one type of product.
    - Verify that the total values (price, weight, and number of products)
      update correctly.
    """
    tv = Product("TV", 800, 20)
    laptop = Product("Laptop", 1200, 5)
    flash_drive = Product("Flash Drive", 100, 1)

    basket.add_product(tv, 1)
    basket.add_product(laptop, 2)
    basket.add_product(flash_drive, 3)

    expected_total_price = 800 + 2400 + 300
    expected_total_weight = 20 + 10 + 3
    expected_count = 1 + 2 + 3

    assert (
        basket.total_price == expected_total_price
    ), f"The total price should be {expected_total_price} units, but got {basket.total_price}"
    assert (
        basket.total_weight == expected_total_weight
    ), f"The total weight should be {expected_total_weight} units, but got {basket.total_weight}"
    assert (
        len(basket.list_products) == expected_count
    ), f"There should be {expected_count} products in the basket, but found {len(basket.list_products)}"

    basket.delete_product(laptop.id)

    expected_total_price = 800 + 300
    expected_total_weight = 20 + 3
    expected_count = 1 + 3

    assert basket.total_price == expected_total_price, (
        f"After removing laptops, the total price should be {expected_total_price} units, "
        f"but got {basket.total_price}"
    )
    assert basket.total_weight == expected_total_weight, (
        f"After removing laptops, the total weight should be {expected_total_weight} units, "
        f"but got {basket.total_weight}"
    )
    assert len(basket.list_products) == expected_count, (
        f"After removing laptops, there should be {expected_count} products in the basket, "
        f"but found {len(basket.list_products)}"
    )


def test_sequential_operations(basket):
    """Test sequential adding, deleting, and re-adding products."""
    camera = Product("Camera", 700, 5)

    basket.add_product(camera, 2)
    assert (
        len(basket.list_products) == 2
    ), f"The number of products should be 2, but got {len(basket.list_products)}"

    basket.delete_product(camera.id)
    assert (
        len(basket.list_products) == 0
    ), f"After deleting products, the basket should be empty, but contains {len(basket.list_products)} products"

    basket.add_product(camera, 1)
    assert (
        len(basket.list_products) == 1
    ), f"After re-adding, there should be 1 product, but got {len(basket.list_products)}"


def test_mixed_operations(basket):
    """Test alternating adding, deleting, and re-adding products."""
    fridge = Product("Fridge", 1500, 50)
    kettle = Product("Kettle", 300, 3)
    toaster = Product("Toaster", 400, 4)

    basket.add_product(fridge, 1)
    assert (
        len(basket.list_products) == 1
    ), f"There should be 1 product in the basket, but got {len(basket.list_products)}"

    basket.add_product(kettle, 2)
    assert (
        len(basket.list_products) == 3
    ), f"There should be 3 products in the basket, but got {len(basket.list_products)}"

    basket.delete_product(fridge.id)
    assert (
        len(basket.list_products) == 2
    ), f"After removing the fridge, there should be 2 products left, but got {len(basket.list_products)}"

    basket.add_product(toaster, 1)
    assert (
        len(basket.list_products) == 3
    ), f"There should be 3 products in the basket, but got {len(basket.list_products)}"

    basket.delete_product(kettle.id)
    assert (
        len(basket.list_products) == 1
    ), f"After removing the kettle, there should be 1 product left, but got {len(basket.list_products)}"

    expected_price = toaster.price
    assert (
        basket.total_price == expected_price
    ), f"The final price should be {expected_price} units, but got {basket.total_price}"


def test_list_products_returns_copy(basket):
    """Test that `list_products` returns a copy of the product list, not the internal list itself.

    After retrieving and modifying the list of products, the internal state of the basket should remain unchanged.
    """
    product = Product("iPhone", 100, 10)
    basket.add_product(product, 2)

    products_copy = basket.list_products
    products_copy.clear()

    assert len(basket.list_products) == 2, (
        f"The internal list of products should remain unchanged after modifying the copy, "
        f"but found {len(basket.list_products)} products in the basket"
    )


def test_list_products_multiple_calls_return_new_instance(basket):
    """
    Test that each call to list_products returns a new list instance.

    Modifying one instance should not affect another retrieved by a subsequent call.
    """
    product = Product("Vacuum Cleaner", 100, 10)
    basket.add_product(product, 2)

    products_first_call = basket.list_products
    products_first_call.append("robot")
    products_second_call = basket.list_products

    assert (
        products_first_call is not products_second_call
    ), "Each call to list_products should return a new instance, but got the same object"
    assert (
        len(products_second_call) == 2
    ), f"The second call to list_products should return 2 products, but got {len(products_second_call)}"


def test_unique_product_ids():
    """Test that each product has a unique identifier."""
    product1 = Product("iPhone 14", 100, 1)
    product2 = Product("iPhone 15", 200, 2)
    product3 = Product("iPhone 16", 300, 3)
    ids = {product1.id, product2.id, product3.id}
    assert len(ids) == 3, "Each product must have a unique identifier."


def test_sequential_operations_unique_ids(basket):
    """Test sequential operations with different products and ensure unique IDs.

    1. Add product A and delete it.
    2. Add two new products (B and C).
    3. Verify that B and C have unique IDs.
    4. Verify that their IDs do not match the deleted product A's ID.
    """
    product_a = Product("Hairdryer", 300, 2)
    basket.add_product(product_a)
    id_a = product_a.id
    basket.delete_product(id_a)

    product_b = Product("Robot Vacuum", 10, 1)
    product_c = Product("Curling Iron", 20, 1)
    basket.add_product(product_b)
    basket.add_product(product_c)

    assert product_b.id != product_c.id, (
        f"The IDs of new products must be unique, but {product_b} ({product_b.id}) "
        f"and {product_c} ({product_c.id}) have the same ID"
    )
    assert (
        product_b.id != id_a
    ), f"New product {product_b} should not have the same ID as the deleted product ({id_a}), but got {product_b.id}"
    assert (
        product_c.id != id_a
    ), f"New product {product_c} should not have the same ID as the deleted product ({id_a}), but got {product_c.id}"


# Boundary tests
def test_product_immutability():
    """Test that Product properties are read-only."""
    product = Product("Laptop", 1200, 5)
    with pytest.raises(AttributeError):
        product.price = 1500
    with pytest.raises(AttributeError):
        product.weight = 10
    with pytest.raises(AttributeError):
        product.name = "New Laptop"


@pytest.mark.parametrize(
    "total_price, expected_shipping", [(499, 250), (500, 100), (999, 100), (1000, 0)]
)
def test_shipping_cost(basket, total_price: int, expected_shipping: int):
    """Test the calculation of shipping cost at boundary values."""
    product = Product("Air Conditioner", total_price, 20)
    basket.add_product(product)

    assert (
        basket.get_shipping_cost == expected_shipping
    ), f"The shipping cost should be {expected_shipping} units, but got {basket.get_shipping_cost}"


def test_reaching_max_items_limit(basket):
    """Test adding products up to the maximum limit (30 items), then attempting to add one more, expecting an exception."""
    product = Product("Keyboard", 50, 2)

    basket.add_product(product, 30)
    assert (
        len(basket.list_products) == 30
    ), f"There should be 30 products in the basket, but got {len(basket.list_products)}"

    with pytest.raises(
        ValueError, match="Exceeded maximum number of items in the basket"
    ):
        basket.add_product(product, 1)


def test_reaching_max_weight_limit(basket):
    """Test adding products up to the maximum total weight (100 units), then attempting to add more, expecting an exception."""
    product = Product("Heater", 200, 10)

    basket.add_product(product, 10)
    assert (
        basket.total_weight == 100
    ), f"The total weight should be 100 units, but got {basket.total_weight}"

    with pytest.raises(
        ValueError, match="Exceeded maximum weight of products in the basket"
    ):
        basket.add_product(product, 1)


def test_extreme_values(basket):
    """Test handling of extreme values for price and weight.

    1. Create a product with a very high price (`10**9`) and minimal valid weight (`1`).
    2. Add the product to the basket.
    3. Verify that:
       - The total price in the basket matches the expected extreme price.
       - The total weight in the basket is correctly accounted for.
       - Shipping remains free (since the product price exceeds 1000 units).
       - The final basket price equals the product price without any extra charges.
    """
    extreme_price = 10**9
    extreme_weight = 1
    product = Product("Super-duper Product", extreme_price, extreme_weight)
    basket.add_product(product)

    assert (
        basket.total_price == extreme_price
    ), f"The total price should be {extreme_price} units, but got {basket.total_price}"
    assert (
        basket.total_weight == extreme_weight
    ), f"The total weight should be {extreme_weight} units, but got {basket.total_weight}"
    assert (
        basket.get_shipping_cost == 0
    ), f"The shipping cost should be free (0 units), but got {basket.get_shipping_cost}"
    assert (
        basket.get_price == extreme_price
    ), f"The final price should equal the product price {extreme_price} units, but got {basket.get_price}"


from typing import Any

# Negative tests
import pytest


@pytest.mark.parametrize("price, weight", [(0, 1), (1, 0), (0, 0)])
def test_invalid_product_creation(price: int, weight: int):
    """Test creating a product with invalid parameters."""
    with pytest.raises(
        ValueError,
        match="Product price must be at least 1 unit|Product weight must be at least 1 unit",
    ):
        Product("Defective Product", price, weight)


@pytest.mark.parametrize(
    "invalid_price, invalid_weight",
    [("1000", 5), (1000, "5"), (None, 10), (200, None), ([], 5), (100, {})],
)
def test_invalid_data_types(invalid_price: Any, invalid_weight: Any):
    """Test passing invalid data types when creating a product."""
    with pytest.raises(TypeError, match=".*"):
        Product("Invalid Product", invalid_price, invalid_weight)


def test_add_zero_products(basket):
    """Test adding zero products to the basket."""
    product = Product("Electric Kettle", 100, 3)

    with pytest.raises(TypeError, match="Expected a positive integer, got int"):
        basket.add_product(product, 0)


def test_negative_quantity(basket):
    """Test adding a negative quantity of a product."""
    product = Product("iPhone", 700, 5)
    with pytest.raises(TypeError, match="Expected a positive integer"):
        basket.add_product(product, -3)


from typing import Any, Union

import pytest


@pytest.mark.parametrize(
    "invalid_product, invalid_quantity",
    [
        ("TV", 2),
        ([], 1),
        (Product("Kettle", 300, 3), "two"),
        (Product("Laptop", 1200, 5), None),
        (Product("Flash Drive", 100, 1), {}),
    ],
)
def test_invalid_data_in_basket_methods(
    basket, invalid_product: Any, invalid_quantity: Union[int, Any]
):
    """Test passing invalid data types to basket methods."""
    with pytest.raises(TypeError, match=".*"):
        basket.add_product(invalid_product, invalid_quantity)


def test_delete_nonexistent_product(basket):
    """Test deleting a non-existent product."""
    basket.delete_product(999)

    assert (
        len(basket.list_products) == 0
    ), f"The basket should be empty, but contains {len(basket.list_products)} products"


def test_delete_product_invalid_type(basket):
    """Test deleting a product using an invalid ID type.

    Since delete_product does not perform type checking,
    the basket should remain unchanged.
    """
    product = Product("Air Fryer", 100, 1)
    basket.add_product(product)
    count_before = len(basket.list_products)
    basket.delete_product("invalid_id")
    assert (
        len(basket.list_products) == count_before
    ), "When passing an invalid ID type, the basket should remain unchanged"


@pytest.mark.parametrize("invalid_key", [1.5, (1,)])
def test_delete_product_invalid_hashable_key(basket, invalid_key: Hashable):
    """Test deleting a product using non-integer but hashable identifiers.

    1. A product is added to the basket.
    2. `delete_product()` is called with a `float` or `tuple` as the key.
    3. Verify that the basket remains unchanged because:
       - The `delete_product()` method should ignore invalid keys without raising exceptions.
       - The number of products in the basket should not change.
    """
    product = Product("Hairdryer", 100, 10)
    basket.add_product(product)
    count_before = len(basket.list_products)

    basket.delete_product(invalid_key)

    assert len(basket.list_products) == count_before, (
        f"The basket should remain unchanged when deleting with a non-integer key, "
        f"but the number of products changed from {count_before} to {len(basket.list_products)}"
    )


@pytest.mark.parametrize("invalid_key", [[1], {1: "a"}])
def test_delete_product_invalid_unhashable_key(basket, invalid_key: Any):
    """Test deleting a product using unhashable (invalid) identifiers.

    1. A product is added to the basket.
    2. `delete_product()` is called with a `list` or `dict` as the key.
    3. Verify that:
       - The `delete_product()` method raises a `TypeError`.
       - The basket remains unchanged after the exception is raised.
    """
    product = Product("Fridge", 100, 10)
    basket.add_product(product)
    count_before = len(basket.list_products)

    with pytest.raises(TypeError, match=".*"):
        basket.delete_product(invalid_key)

    assert len(basket.list_products) == count_before, (
        f"The basket should remain unchanged after attempting to delete with an unhashable key, "
        f"but the number of products changed from {count_before} to {len(basket.list_products)}"
    )
