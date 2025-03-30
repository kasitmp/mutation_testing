from price_calculator.price_calculator import PriceCalculator

class TestOrderValue:
    _calculator: PriceCalculator = PriceCalculator()

    def test_single_item_order(self):
        assert self._calculator.order_value(1, 1) == 1
    
    def test_single_item_order_different_price(self):
        assert self._calculator.order_value(1, 2) == 2

    def test_zero_item_order(self):
        assert  self._calculator.order_value(0, 2) == 0
