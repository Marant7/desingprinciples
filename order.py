# order.py
class Order:
    def __init__(self, items):
        self.items = items
        self.total_amount = sum(item['price'] for item in items)

    def calculate_total(self):
        return self.total_amount