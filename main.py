# main.py
from order_service import OrderService
from payment_methods import CreditCardPayment, PayPalPayment
from order import Order

# Create an order
items = [{"name": "Laptop", "price": 1000}, {"name": "Mouse", "price": 50}]
order = Order(items)

# Select the payment method
payment_method = CreditCardPayment()  # Or use PayPalPayment()

# Process the order with the selected payment method
order_service = OrderService(payment_method)
order_service.process_order(order)