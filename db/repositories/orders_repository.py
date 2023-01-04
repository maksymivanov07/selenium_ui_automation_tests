from pony.orm import db_session, select, left_join
from db.models.models import Orders, Products


class OrdersRepository:

    def __init__(self):
        self.__model = Orders

    @db_session
    def add_order(self, product, quantity):
        self.__model(product=product, quantity=quantity)

    @db_session
    def select_from_orders(self):
        orders = self.__model.select()
        for order in orders:
            print(f"id: {order.id}, product_id: {order.product}, quantity: {order.quantity}")

    @db_session
    def left_join(self):
        query = left_join((p.name, p.price, o.quantity, (p.price * o.quantity)) for p in Products for o in p.orders)
        query.show()


if __name__ == '__main__':
    orders_repo = OrdersRepository()
    orders_repo.left_join()
