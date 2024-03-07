from src.domains.order import  OrderStatus, Order, OrderStatusName, OrderItem
from src.domains.product import Product
from src.domains.customer import Customer

def test_should_create_customer():

    customer: Customer = Customer(
        name="Guilherme",
        email="gui@gui",
    )

    status: OrderStatus = OrderStatus()

    assert status.name == OrderStatusName.ACCOMPLISHED

    product1: Product = Product(
        name="PS5",
        description="Video Game",
        price=5000
    )
    assert product1.name == "PS5"
    assert product1.description == "Video Game"
    assert product1.price == 5000

    product2: Product = Product(
        name="PS4",
        description="Video Game",
        price=2000
    )
    assert product2.name == "PS4"
    assert product2.description == "Video Game"
    assert product2.price == 2000

    item1: OrderItem = OrderItem(product_id=product1.id, price=product1.price, quantity=1)
    item2: OrderItem = OrderItem(product_id=product2.id, price=product2.price, quantity=2)

    order: Order = Order(customer = customer)
    order.add_status(status)
    order.add_item(item1)
    order.add_item(item2)

    assert len(order.status) == 1
    assert order.status[0].name == OrderStatusName.ACCOMPLISHED
    assert len(order.items) == 2

    #novo status: em preparacao
    status2 = OrderStatus(name=OrderStatusName.IN_PREPARING)
    order.add_status(status2)

    assert len(order.status) == 2
    assert order.status[1].name == OrderStatusName.IN_PREPARING

    #novo status: enviado
    status3 = OrderStatus(name=OrderStatusName.SENT)
    order.add_status(status3)
    
    assert len(order.status) == 3
    assert order.status[2].name == OrderStatusName.SENT

    #novo status: entregue
    status4 = OrderStatus(name=OrderStatusName.DELIVERED)
    order.add_status(status4)
    
    assert len(order.status) == 4
    assert order.status[3].name == OrderStatusName.DELIVERED

        #novo status: finalizado
    status5 = OrderStatus(name=OrderStatusName.FINISHED)
    order.add_status(status5)
    
    assert len(order.status) == 5
    assert order.status[4].name == OrderStatusName.FINISHED

    #verificando total
    assert order.total() == 9000