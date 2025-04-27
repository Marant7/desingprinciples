# Abstract payment processor interface
class PaymentProcessor:
    def process(self, order):
        raise NotImplementedError

class CreditCardProcessor(PaymentProcessor):
    def process(self, order):
        print(f"Processing credit card payment of ${order.total_amount}")

class OrderService:
    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor

    def process_order(self, order):
        print("Processing order...")
        self.payment_processor.process(order)
