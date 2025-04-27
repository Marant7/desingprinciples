class PaymentMethod:
    def calculate_total(self, order):
        raise NotImplementedError

class CreditCardPayment(PaymentMethod):
    def calculate_total(self, order):
        return order.total_amount * 1.02  # Apply 2% commission

class PayPalPayment(PaymentMethod):
    def calculate_total(self, order):
        return order.total_amount * 1.05  # Apply 5% commission
