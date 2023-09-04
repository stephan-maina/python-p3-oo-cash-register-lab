class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, item_name, item_price, quantity=1):
        item_total = item_price * quantity
        self.total += item_total
        self.items.append({"name": item_name, "price": item_price, "quantity": quantity})
        return item_total

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            return self.total
        else:
            return None

    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()
            void_amount = last_item["price"] * last_item["quantity"]
            self.total -= void_amount
        else:
            return None
