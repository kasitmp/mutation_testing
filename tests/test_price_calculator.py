from price_calculator.price_calculator import PriceCalculator


class TestOrderValue:
    _calculator: PriceCalculator = PriceCalculator()

    def test_single_item_order(self):
        assert self._calculator.order_value(1, 1.0) == 1.0

    def test_single_item_order_different_price(self):
        assert self._calculator.order_value(1, 2.0) == 2.0

    def test_zero_item_order(self):
        assert self._calculator.order_value(0, 2.0) == 0.0


class TestApplyUtahTax:
    _calculator: PriceCalculator = PriceCalculator()

    def test_taxed_order_value(self):
        assert self._calculator.apply_tax(1.0) == 1.0685

    def test_taxed_order_value_different(self):
        assert self._calculator.apply_tax(2.0) == 2.137


class TestFlexibleTax:
    _calculator: PriceCalculator = PriceCalculator()

    def test_taxed_order_value_nevada(self):
        assert self._calculator.apply_tax(1.0, 0.08) == 1.08


class TestTotalPrice:
    _calculator: PriceCalculator = PriceCalculator()

    def test_nevada(self):
        assert self._calculator.total_value(1, 1.0, "NV") == 1.08

    def test_utah(self):
        assert self._calculator.total_value(1, 1.0, "UT") == 1.0685
