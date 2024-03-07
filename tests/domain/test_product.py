from src.domains.product import Product


def test_should_create_customer():
    product: Product = Product(
        name="PS5",
        description="Video Game",
        price=5000
    )
    assert product.name == "PS5"
    assert product.description == "Video Game"
    assert product.price == 5000