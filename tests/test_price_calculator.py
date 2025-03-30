from price_calculator.price_calculator import PriceCalculator


class TestOrderValue:
    _calculator: PriceCalculator = PriceCalculator()

    def test_single_item_order(self):
        assert self._calculator.order_value(1, 1.0) == 1.0

    def test_single_item_order_different_price(self):
        assert self._calculator.order_value(1, 2.0) == 2.0

    def test_zero_item_order(self):
        assert self._calculator.order_value(0, 2.0) == 0.0


class TestUtahTax:
    _calculator: PriceCalculator = PriceCalculator()

    def test_taxed_order_value(self):
        assert self._calculator.taxed_order_value(1, 1.0) == 1.0685

    def test_taxed_order_different_price(self):
        assert self._calculator.taxed_order_value(1, 2.0) == 2.137
