class Order:
    def __init__(self, items, total_amount):
        self.items = items
        self.total_amount = total_amount

    def calculate_total(self):
        return sum(item['price'] for item in self.items)
