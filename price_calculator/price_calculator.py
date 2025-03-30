class PriceCalculator:
    def order_value(self, count: int, price: float) -> float:
        return count * price

    def taxed_order_value(self, count: int, price: float) -> float:
        order_value = self.order_value(count, price)
        return order_value + order_value * 0.0685
