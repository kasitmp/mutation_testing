class PriceCalculator:
    taxMap = dict(UT=0.0685, NV=0.08)

    def order_value(self, count: int, price: float) -> float:
        return count * price

    def apply_tax(self, order_value, tax: float = 0.0685) -> float:
        return order_value + order_value * tax

    def total_value(self, count: int, price: float, state: str):
        if state not in list(self.taxMap):
            raise ValueError(f"Unsupported state: {state}")
        order_value = self.order_value(count, price)
        if state == "UT":
            return self.apply_tax(order_value)
        return self.apply_tax(order_value, 0.08)
