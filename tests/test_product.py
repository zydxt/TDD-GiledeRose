from unittest import TestCase
from giledRose.product import ProductBase
from giledRose.exceptions import SellInException, QualityException


class TestProductBase(TestCase):

    def test_should_raise_error_when_initialize_with_quality_greater_than_50(self):

        self.assertRaises(SellInException, ProductBase, "name", 0, 20)
        self.assertRaises(QualityException, ProductBase, "name", 1, 51)

    def test_should_raise_error_when_initialize_with_sell_in_less_than_0(self):

        self.assertRaises(SellInException, ProductBase, "name", 0, 20)
