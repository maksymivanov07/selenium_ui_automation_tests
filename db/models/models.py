from pony import orm
from pony.orm import Database, sql_debug
from pony.orm import PrimaryKey, Set, Required

db = Database()

db.bind(provider='postgres', user='max', password='9999', host='127.0.0.1', database='postgres')


class Products(db.Entity):
    _table_ = "products"
    id = PrimaryKey(int, auto=True)
    name = Required(str, 20)
    price = Required(float)
    orders = Set("Orders")


class Orders(db.Entity):
    _table_ = 'orders'
    id = PrimaryKey(int, auto=True)
    product = Required('Products', column='product_id')
    quantity = Required(int)


db.generate_mapping(create_tables=True)

with orm.db_session:
    """
    beautiful creation data for tables (variant 1)
    """
    airpods = Products(name='airpods', price=299)
    iphone = Products(name='iphone', price=999)
    macbook = Products(name='macbook', price=2500)
    apple_watch = Products(name='apple watch', price=350)
    magic_mouse = Products(name='magic mouse', price=100)

    airpods.orders.create(quantity=259)
    iphone.orders.create(quantity=300)
    macbook.orders.create(quantity=23)
    apple_watch.orders.create(quantity=545)
    magic_mouse.orders.create(quantity=5)

sql_debug(True)
