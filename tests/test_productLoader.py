import json
from os import path

from unittest import TestCase, mock

from giledRose.product import NormalProduct, BackstagePass
from giledRose.productLoader import productLoader


class Test(TestCase):

    def setUp(self):
        self.mockProductInfo = [
            {"name": "test1", "sellIn": 1, "quality": 10, "type": "normal"},
            {"name": "test2", "sellIn": 1, "quality": 10, "type": "normal"},
            {"name": "testPass", "sellIn": 1, "quality": 10, "type": "backstagePass"},
        ]

    def test_product_loader_return_product_list_according_to_json_file(self):
        mock_open = mock.mock_open(read_data=json.dumps(self.mockProductInfo))
        with mock.patch("builtins.open", mock_open):
            productList = productLoader()
            mock_open.assert_called_with(
                path.join(path.dirname(path.dirname(path.abspath(__file__))), "giledRose/productInfo.json"), 'r')
            self.assertEqual(len(productList), 3)
            self.assertIsInstance(productList[0], NormalProduct)
            self.assertIsInstance(productList[1], NormalProduct)
            self.assertIsInstance(productList[2], BackstagePass)
