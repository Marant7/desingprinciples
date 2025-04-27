class CreditCardProcessor:
    def process_credit_card(self, card_number, amount):
        print(f"Processing credit card payment of ${amount} using card {card_number}")

class PayPalProcessor:
    def process_paypal(self, email, amount):
        print(f"Processing PayPal payment of ${amount} for account {email}")