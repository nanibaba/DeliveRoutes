# test_product.py
# Unit tests for the Product class in product.py.

import unittest
from product import Product
from uuid_generator import generateUUID


class TestProduct(unittest.TestCase):

    def test_product_initialization(self):
        """ Test the initialization of the Product class. """
        product = Product("TestProduct", ["Variant1", "Variant2"])
        self.assertEqual(product.name, "TestProduct")
        self.assertEqual(product.variants, ["Variant1", "Variant2"])
        self.assertIsInstance(product.ID, type(generateUUID()))

    def test_name_getter(self):
        """ Test the name getter method. """
        product = Product("TestProduct")
        self.assertEqual(product.name, "TestProduct")

    def test_name_setter(self):
        """ Test the name setter method. """
        product = Product("OldName")
        product.name = "NewName"
        self.assertEqual(product.name, "NewName")

    def test_variants_getter(self):
        """ Test the variants getter method. """
        product = Product("TestProduct", ["Variant1"])
        self.assertEqual(product.variants, ["Variant1"])

    def test_variants_setter(self):
        """ Test the variants setter method. """
        product = Product("TestProduct", ["OldVariant"])
        product.variants = ["NewVariant"]
        self.assertEqual(product.variants, ["NewVariant"])

    
