from unittest import TestCase, mock
from giledRose.product import ProductBase
from giledRose.exceptions import SellInException, QualityException


class TestProductBase(TestCase):

    def test_should_raise_error_when_initialize_with_quality_greater_than_50(self):

        self.assertRaises(SellInException, ProductBase, "name", 0, 20)
        self.assertRaises(QualityException, ProductBase, "name", 1, 51)

    def test_should_raise_error_when_initialize_with_sell_in_less_than_0(self):
        self.assertRaises(SellInException, ProductBase, "name", 0, 20)

    def test_should_call_calculate_and_minus_sell_in_one_day_when_updateInfoAfterOneDay(self):
        with mock.patch("giledRose.product.ProductBase.calculateQualityAfterOneDay", return_value=0) as mockCalculateQuality:
            product = ProductBase("name", 10, 10)
            product.updateInfoAfterOneDay()
            mockCalculateQuality.assert_called()
            self.assertEqual(product.sellIn, 9)
            self.assertEqual(product.quality, 0)
