from pony.orm import db_session, select
from db.models.models import Products


class ProductsRepository:

    def __init__(self):
        self.__model = Products

    @db_session
    def select_from_products(self):
        products = select(order for order in Products)
        for product in products:
            print(f"id: {product.id}, product_id: {product.name}, quantity: {product.price}")


if __name__ == '__main__':
    products_repo = ProductsRepository()
    products_repo.select_from_products()
