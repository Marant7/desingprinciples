
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def calculate_total(self, order):
        pass

class CreditCardPayment(PaymentMethod):
    def calculate_total(self, order):
        return order.calculate_total() * 1.02  # Apply 2% commission

class PayPalPayment(PaymentMethod):
    def calculate_total(self, order):
        return order.calculate_total() * 1.05  # Apply 5% commission