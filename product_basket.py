import itertools


class Product:
    """A class representing a product on a marketplace."""

    _id_counter = itertools.count(1)  # Unique ID generator

    def __init__(self, name: str, price: int, weight: int) -> None:
        """
        Initialize a product.

        :param name: Name of the product
        :param price: Price of the product (positive integer)
        :param weight: Weight of the product (positive integer)
        :raises ValueError: if price or weight is less than 1
        """
        if price < 1:
            raise ValueError("Product price must be at least 1 unit.")
        if weight < 1:
            raise ValueError("Product weight must be at least 1 unit.")

        self._id = next(self._id_counter)
        self._name = name
        self._price = price
        self._weight = weight

    @property
    def id(self) -> int:
        """Returns the unique ID of the product."""
        return self._id

    @property
    def name(self) -> str:
        """Returns the name of the product."""
        return self._name

    @property
    def price(self) -> int:
        """Returns the price of the product."""
        return self._price

    @property
    def weight(self) -> int:
        """Returns the weight of the product."""
        return self._weight


class Basket:
    """A class representing a shopping basket."""

    MAX_WEIGHT = 100  # Maximum total weight of products in the basket
    MAX_ITEMS = 30  # Maximum number of products in the basket

    def __init__(self) -> None:
        """Initialize the basket."""
        self._products: dict[int, list[Product]] = {}

    def add_product(self, product: Product, quantity: int = 1) -> None:
        """
        Adds a product to the basket.

        :param product: An instance of the Product class
        :param quantity: Quantity of the product (default is 1)
        :raises TypeError: if input types are incorrect
        :raises ValueError: if adding the product exceeds basket limits
        """
        if not isinstance(product, Product):
            raise TypeError(f"Expected a Product object, got {type(product).__name__}")

        if not isinstance(quantity, int) or quantity < 1:
            raise TypeError(
                f"Expected a positive integer, got {type(quantity).__name__}"
            )

        if len(self.list_products) + quantity > self.MAX_ITEMS:
            raise ValueError(
                "Exceeded maximum number of items in the basket (30 units)."
            )

        if self.total_weight + product.weight * quantity > self.MAX_WEIGHT:
            raise ValueError(
                "Exceeded maximum weight of products in the basket (100 units)."
            )

        if product.id not in self._products:
            self._products[product.id] = []

        self._products[product.id].extend([product] * quantity)

    def delete_product(self, product_id: int) -> None:
        """
        Removes a product entirely from the basket.

        :param product_id: The product's ID
        """
        self._products.pop(product_id, None)

    @property
    def list_products(self) -> list[Product]:
        """Returns a list of all products in the basket."""
        return [item for sublist in self._products.values() for item in sublist]

    @property
    def total_price(self) -> int:
        """Returns the total price of all products in the basket."""
        return sum(product.price for product in self.list_products)

    @property
    def total_weight(self) -> int:
        """Returns the total weight of all products in the basket."""
        return sum(product.weight for product in self.list_products)

    @property
    def get_shipping_cost(self) -> int:
        """Returns the shipping cost based on the total price of products."""
        if self.total_price == 0:
            return 0
        if self.total_price < 500:
            return 250
        elif 500 <= self.total_price < 1000:
            return 100
        return 0

    @property
    def get_price(self) -> int:
        """Returns the final basket price including shipping."""
        return self.total_price + self.get_shipping_cost
