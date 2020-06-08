from unittest import TestCase

from giledRose.product import NormalProduct, BackstagePass
from giledRose.productFactory import productFactory


class Test(TestCase):
    def test_product_factory_should_return_normalProduct_when_type_is_normal(self):
        product = productFactory("name", 1, 2, "normal")
        self.assertIsInstance(product, NormalProduct)
        self.assertEqual(product.name, "name")
        self.assertEqual(product.sellIn, 1)
        self.assertEqual(product.quality, 2)

    def test_product_factory_should_return_backStagePass_when_type_is_backstagePass(self):
        product = productFactory("name", 1, 2, "backstagePass")
        self.assertIsInstance(product, BackstagePass)
        self.assertEqual(product.name, "name")
        self.assertEqual(product.sellIn, 1)
        self.assertEqual(product.quality, 2)

    def test_product_factory_should_raise_TypeError_when_type_is_not_in_map(self):
        self.assertRaises(TypeError, productFactory, "name", 1, 2, "other")
