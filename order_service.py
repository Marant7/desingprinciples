from payment_methods import PaymentMethod, CreditCardPayment, PayPalPayment
from order import Order

class OrderService:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process_order(self, order):
        total_with_payment = self.payment_method.calculate_total(order)
        print(f"Processing order with total payment: ${total_with_payment:.2f}")