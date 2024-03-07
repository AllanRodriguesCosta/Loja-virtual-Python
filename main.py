from src.factories.customer_factory import CustomerFactory
from src.domains.customer import CustomerRegistration

service = CustomerFactory.create_mock()

customer = CustomerRegistration(
    name = "Allan",
    email = "allan@gmail.com",
    password = "123456",
    confirm_password= "123456",
)

response = await service.register(customer_registration=customer)

print(response)
