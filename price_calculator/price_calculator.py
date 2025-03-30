class PriceCalculator:
    def order_value(self, count: int, price: float) -> float:
        return count * price

    def apply_tax(self, order_value, tax: float = 0.0685) -> float:
        return order_value + order_value * tax

    def total_value(self, count: int, price: float, state: str):
        order_value = self.order_value(count, price)
        if state == "UT":
            return self.apply_tax(order_value)
        return self.apply_tax(order_value, 0.08)
