# Table of Contents

1. [Demonstration Project: Testing a Product Basket](#demonstration-project-testing-a-product-basket)  
2. [Test Checklist](#test-checklist)  
    - [Positive Tests](#positive-tests)  
    - [Boundary Tests](#boundary-tests)  
    - [Negative Tests](#negative-tests)
3. [Project Launch Instructions](#project-launch-instructions)  

# Demonstration Project: Testing a Product Basket

## Description
This project is an implementation of a product basket system for a marketplace.  
It includes two classes:

- **Product** — represents a product in the marketplace (name, unique identifier, price, weight).
- **Basket** — represents a shopping basket where products can be added, removed, listed, and where the total price and shipping cost can be calculated.

As part of the project, **full test coverage** has been developed, including positive, boundary, and negative tests.

To improve readability and code reusability, the tests are implemented using parameterization.

The project is written in **Python** using **pytest** for testing.

The `tests/conftest.py` file contains a key fixture:
- **Fixture for initializing an empty basket** — used to create a new empty basket before each test to ensure a clean initial state and to avoid the influence of previous tests.


## Test Results
A screenshot of successful test execution is located in the `screenshots` directory of the project.

---

## Features
- The product price cannot be less than **1 unit**.
- Maximum total weight of products in the basket: **100 units**.
- Maximum number of products in the basket: **30 items**.
- Shipping cost:
  - If the total price is less than 500 units → shipping costs **250 units**.
  - If the total price is between 500 and 999 units → shipping costs **100 units**.
  - If the total price is 1000 units or higher → shipping is **free**.

---

# Test Checklist

## Positive Tests

### Checking properties of an empty basket (`test_empty_basket_properties`)
- [x] Total price (`total_price`) is 0.
- [x] Total weight (`total_weight`) is 0.
- [x] Shipping cost (`get_shipping_cost`) is 0.
- [x] Final price (`get_price`) is 0.
- [x] Product list (`list_products`) is empty.

### Adding a single product with different parameters (`test_add_single_product`)
- [x] Successfully adding a product with the specified price and weight.
- [x] Correct calculation of shipping cost depending on the price.

### Deleting a product from the basket (`test_delete_product`)
- [x] Successfully deleting a product from the basket.
- [x] Checking the absence of the deleted product in the list.

### Adding a product and checking final parameters (`test_add_product`)
- [x] Successfully adding a product to the basket.
- [x] Recalculating the final basket price.
- [x] Recalculating the total basket weight.
- [x] Checking that the product appears in the product list.
- [x] Correct calculation of shipping cost.

### Adding multiple different products (`test_add_multiple_products`)
- [x] Successfully adding multiple different products.
- [x] Correct calculation of the total price of products.
- [x] Correct calculation of the total weight of products.
- [x] Correct shipping cost.

### Sequential basket usage (adding and removing) (`test_sequential_usage`)
- [x] Adding multiple products.
- [x] Deleting one type of product.
- [x] Correct updating of final parameters (price, weight, number of products).

### Sequential operations (`test_sequential_operations`)
- [x] Sequentially adding products.
- [x] Deleting products.
- [x] Re-adding products.
- [x] Correct updating of the basket's state after sequential operations.

### Mixed operations with products (`test_mixed_operations`)
- [x] Alternating adding, deleting, and re-adding products.
- [x] Correct basket behavior under a complex sequence of actions.

### Checking that `list_products` returns a copy (`test_list_products_returns_copy`)
- [x] A copy of the product list is returned.
- [x] Modifying the copy does not affect the internal state of the basket.

### Checking that each call to `list_products` returns a new instance (`test_list_products_multiple_calls_return_new_instance`)
- [x] Each call returns a new list instance.
- [x] Modifying one list does not affect another.

### Checking product ID uniqueness (`test_unique_product_ids`)
- [x] Each product has a unique identifier.

### Checking ID uniqueness after deletion/addition operations (`test_sequential_operations_unique_ids`)
- [x] Create product A and delete it.
- [x] Create products B and C.
- [x] Verify that the IDs of products B and C are unique and do not match the deleted product A's ID.

## Boundary Tests

### Immutability of `Product` properties (`test_product_immutability`)
- [x] `Product` properties are read-only.

### Checking shipping cost at boundary price values (`test_shipping_cost`)
- [x] Correct calculation of shipping cost when crossing price thresholds.

### Adding 30 products (item limit boundary) (`test_reaching_max_items_limit`)
- [x] Successfully adding 30 products.
- [x] Attempting to add the 31st product raises an exception.

### Adding products up to the maximum weight (100 units) (`test_reaching_max_weight_limit`)
- [x] Successfully adding products until the total weight reaches 100 units.
- [x] Attempting to exceed the weight limit raises an exception.

### Working with extreme price and weight values (`test_extreme_values`)
- [x] Creating a product with an extremely high price and minimal weight.
- [x] Verifying correct total basket price calculation.
- [x] Verifying correct total basket weight calculation.
- [x] Confirming free shipping for an extremely high price.
- [x] Checking that the final price matches the product price without extra charges.

## Negative Tests

### Attempt to create a product with invalid parameters (price or weight = 0) (`test_invalid_product_creation`)
- [x] Attempt to create a product with a price of 0 raises an error.
- [x] Attempt to create a product with a weight of 0 raises an error.
- [x] Attempt to create a product with both price and weight equal to 0 raises an error.

### Adding zero products to the basket (`test_add_zero_products`)
- [x] Attempting to add zero products should be rejected or ignored.

### Adding a negative quantity of products (`test_negative_quantity`)
- [x] Attempting to add a negative quantity of products raises an error or is rejected.

### Passing invalid data types to basket methods (`test_invalid_data_in_basket_methods`)
- [x] Attempting to pass invalid data types to basket methods is handled correctly.

### Deleting a non-existent product (`test_delete_nonexistent_product`)
- [x] Attempting to delete a product that is not in the basket does not cause errors and does not change the basket state.

### Deleting a product with an invalid ID type (`test_delete_product_invalid_type`)
- [x] Attempting to delete a product with an incorrect ID type (e.g., a string) is ignored without errors.

### Deleting a product with a valid but inappropriate hashable key (`test_delete_product_invalid_hashable_key`)
- [x] Attempting to delete a product with a `float` or `tuple` as a key does not cause errors but does not modify the basket.

### Deleting a product with an invalid (unhashable) key, raising `TypeError` (`test_delete_product_invalid_unhashable_key`)
- [x] Attempting to delete a product with a `list` or `dict` as a key raises a `TypeError`.
- [x] The basket remains unchanged after the exception is raised.

# Project Launch Instructions

## 1. Installing Python

Make sure you have Python version 3.10 or higher installed:

    python3 --version

If your Python version is below 3.10, update Python before proceeding.

## 2. Installing Poetry

Check if Poetry is installed:

    poetry --version

If Poetry is not installed, install it with the following command:

    curl -sSL https://install.python-poetry.org | python3 -
    export PATH="$HOME/.local/bin:$PATH"

> If the `poetry` command is not recognized, make sure you have added Poetry to your `PATH`.

## 3. Cloning the Repository

Clone the project and navigate into its directory:

    git clone git@gitlab.com:Vikgur/product-basket-tests-english-version.git
    cd product-basket-tests-english-version

## 4. Setting Up the Virtual Environment

Create a virtual environment based on Python 3:

    poetry env use python3

Install the project dependencies:

    poetry install --with dev

> The `poetry.lock` file is included in the repository to synchronize dependency versions.

## 5. Running Tests

### Full test run with detailed output for parameterized data and coverage reporting

    poetry run coverage run -m pytest tests/test_*.py -v
    poetry run coverage report -m | grep "tests/test_"

- The `-v` flag enables detailed output for all parameterized tests.
- `grep` filters the report to show only lines related to the test files for easier viewing.

### Running without detailed (`-v`) output

    poetry run coverage run -m pytest tests/test_*.py
    poetry run coverage report -m | grep "tests/test_"

### Regular test run without coverage

    poetry run pytest

