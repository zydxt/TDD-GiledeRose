from unittest import TestCase, mock
from giledRose.product import ProductBase, NormalProduct, BackstagePass
from giledRose.exceptions import SellInException, QualityException


class TestProductBase(TestCase):

    def test_should_raise_error_when_initialize_with_quality_greater_than_50(self):
        self.assertRaises(SellInException, ProductBase, "name", 0, 20)
        self.assertRaises(QualityException, ProductBase, "name", 1, 51)

    def test_should_raise_error_when_initialize_with_sell_in_less_than_0(self):
        self.assertRaises(SellInException, ProductBase, "name", 0, 20)

    def test_should_call_calculate_and_minus_sell_in_one_day_when_updateInfoAfterOneDay(self):
        with mock.patch("giledRose.product.ProductBase.calculateQualityAfterOneDay",
                        return_value=0) as mockCalculateQuality:
            product = ProductBase("name", 10, 10)
            product.updateInfoAfterOneDay()
            mockCalculateQuality.assert_called()
            self.assertEqual(product.sellIn, 9)
            self.assertEqual(product.quality, 0)


class TestNormalProduct(TestCase):

    def test_get_decrease_quality_today_should_return_1_when_sell_in_greater_than_0(self):
        normalProduct = NormalProduct("normal", 10, 10)
        self.assertEqual(normalProduct.getDecreaseQualityToday(), 1)

    def test_get_decrease_quality_today_should_return_1_when_sell_in_equal_0(self):
        normalProduct = NormalProduct("normal", 10, 10)
        normalProduct.sellIn = 0
        self.assertEqual(normalProduct.getDecreaseQualityToday(), 1)

    def test_get_decrease_quality_today_should_return_2_when_sell_in_less_than_0(self):
        normalProduct = NormalProduct("normal", 10, 10)
        normalProduct.sellIn = -1
        self.assertEqual(normalProduct.getDecreaseQualityToday(), 2)

    @mock.patch("giledRose.product.NormalProduct.getDecreaseQualityToday", return_value=20)
    def test_calculate_quality_after_one_day_should_return_0_when_quality_less_than_0(self, mock_method):
        normalProduct = NormalProduct("normal", 10, 10)
        self.assertEqual(normalProduct.calculateQualityAfterOneDay(), 0)
        mock_method.assert_called()

    @mock.patch("giledRose.product.NormalProduct.getDecreaseQualityToday", return_value=3)
    def test_calculate_quality_after_one_day_should_return_decrease_by_getDecreaseQualityToday(self, mock_method):
        normalProduct = NormalProduct("normal", 10, 10)
        self.assertEqual(normalProduct.calculateQualityAfterOneDay(), 7)
        mock_method.assert_called()

    def test_convert_to_dict_should_return_correct_dict(self):
        normalDict = NormalProduct("normal", 10, 10).toDict()
        self.assertEqual(normalDict['name'], "normal")
        self.assertEqual(normalDict['sellIn'], 10)
        self.assertEqual(normalDict['quality'], 10)
        self.assertEqual(normalDict['type'], "normal")


class TestBackstagePass(TestCase):

    @mock.patch("giledRose.product.BackstagePass.getDecreaseQualityToday", return_value=1)
    def test_calculate_quality_after_one_day_should_return_0_when_sell_in_less_than_0(self, mock_method):
        backstagePass = BackstagePass("pass", 1, 10)
        backstagePass.sellIn = 0

        self.assertEqual(backstagePass.calculateQualityAfterOneDay(), 0)
        backstagePass.sellIn = -1

        self.assertEqual(backstagePass.calculateQualityAfterOneDay(), 0)
        mock_method.assert_not_called()

    @mock.patch("giledRose.product.BackstagePass.getDecreaseQualityToday", return_value=-50)
    def test_calculate_quality_after_one_day_should_return_50_when_quality_greater_than_50(self, mock_method):
        backstagePass = BackstagePass("pass", 1, 10)
        self.assertEqual(backstagePass.calculateQualityAfterOneDay(), 50)
        mock_method.assert_called()

    @mock.patch("giledRose.product.BackstagePass.getDecreaseQualityToday", return_value=-2)
    def test_calculate_quality_after_one_day_should_increase_by_getDecreaseQualityToday(self, mock_method):
        backstagePass = BackstagePass("pass", 1, 10)
        self.assertEqual(backstagePass.calculateQualityAfterOneDay(), 12)
        mock_method.assert_called()

    def test_get_decrease_quality_today_should_return_negative_1_when_sellIn_greater_than_10(self):
        self.assertEqual(BackstagePass("pass", 11, 10).getDecreaseQualityToday(), -1)

    def test_get_decrease_quality_today_should_return_negative_2_when_sellIn_between_5_to_10(self):
        backstagePass = BackstagePass("pass", 10, 10)
        self.assertEqual(backstagePass.getDecreaseQualityToday(), -2)
        backstagePass.sellIn = 6
        self.assertEqual(backstagePass.getDecreaseQualityToday(), -2)

    def test_get_decrease_quality_today_should_return_negative_3_when_sellIn_between_0_to_5(self):
        backstagePass = BackstagePass("pass", 5, 10)
        self.assertEqual(backstagePass.getDecreaseQualityToday(), -3)

    def test_convert_to_dict_should_return_correct_dict(self):
        normalDict = BackstagePass("pass", 10, 10).toDict()
        self.assertEqual(normalDict['name'], "pass")
        self.assertEqual(normalDict['sellIn'], 10)
        self.assertEqual(normalDict['quality'], 10)
        self.assertEqual(normalDict['type'], "backstagePass")
