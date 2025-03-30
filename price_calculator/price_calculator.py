class PriceCalculator:
    taxMap = dict(UT=0.0685, NV=0.08, TX=0.0625, AL=0.04, CA=0.0825)

    def order_value(self, count: int, price: float) -> float:
        return count * price

    def apply_tax(self, order_value, tax: float = 0.0685) -> float:
        return order_value + order_value * tax

    def total_value(self, count: int, price: float, state: str):
        if state not in list(self.taxMap):
            raise ValueError(f"Unsupported state: {state}")
        order_value = self.order_value(count, price)
        return self.apply_tax(order_value, self.taxMap[state])
