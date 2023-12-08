# product.py
# This file contains the Product class which represents a product with a 
# unique ID, name, and variants. 
# The unique ID is generated using the generateUUID function from the 
# uuid_generator module.

from uuid_generator import generateUUID


class Product:
    def __init__(self, name, variants=[]):
        """
        Initialize a new Product instance.

        Args:
            name (str): The name of the product.
            variants (list): A list of variants for the product. Defaults to 
            an empty list.
        """
        self._ID = generateUUID() 
        self._name = name
        self._variants = variants

    @property
    def ID(self):
        """
        Get the unique ID of the product.

        Returns:
            UUID: The unique identifier of the product.
        """
        return self._ID
    
    @property
    def name(self):
        """
        Get the name of the product.

        Returns:
            str: The name of the product.
        """
        return self._name
    
    @name.setter
    def name(self, name):
        """
        Set the name of the product.

        Args:
            name (str): The new name of the product.
        """
        self._name = name
    
    @property
    def variants(self):
        """
        Get the list of variants of the product.

        Returns:
            list: The variants of the product.
        """
        return self._variants
    
    @variants.setter
    def variants(self, variants):
        """
        Set the list of variants for the product.

        Args:
            variants (list): The new list of variants for the product.
        """
        self._variants = variants
