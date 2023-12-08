# variant.py
# This file contains the Variant class, a subclass of Product. 
# It represents a specific variant of a product, including attributes like 
# variant name, country of origin, price, description, and properties.

from product import Product


class Variant(Product):
    def __init__(self, name, variant_name, country, 
                 price, description, properties):
        """
        Initialize a new Variant instance.

        Args:
            name (str): The name of the product.
            variant_name (str): The name of the variant.
            country (str): The country of origin of the variant.
            price (float): The price of the variant.
            description (str): The description of the variant.
            properties (dict): A dictionary of properties such as sizes, 
            colors, and fit.
        """
        super().__init__(name)
        self._variant_name = variant_name
        self._country_of_origin = country
        self._price = price
        self._description = description
        self._properties = {
            "sizes": properties["sizes"],
            "colors": properties["colors"],
            "fit": properties["fit"]
        }

    @property
    def variant_name(self):
        """
        Get the variant name.

        Returns:
            str: The name of the variant.
        """
        return self._variant_name 
    
    @variant_name.setter
    def variant_name(self, variant_name):
        """
        Set the variant name.

        Args:
            variant_name (str): The new name of the variant.
        """
        self._variant_name = variant_name
    
    @property
    def country_of_origin(self):
        """
        Get the country of origin of the variant.

        Returns:
            str: The country of origin.
        """
        return self._country_of_origin
    
    @country_of_origin.setter
    def country_of_origin(self, country):
        """
        Set the country of origin of the variant.

        Args:
            country (str): The new country of origin.
        """
        self._country_of_origin = country

    @property
    def price(self):
        """
        Get the price of the variant.

        Returns:
            str: The price formatted as a string with a dollar sign.
        """
        return f"${self._price}"
    
    @price.setter
    def price(self, price):
        """
        Set the price of the variant.

        Args:
            price (float): The new price of the variant.
        """
        self._price = price

    @property
    def description(self):
        """
        Get the description of the variant.

        Returns:
            str: The description of the variant.
        """
        return self._description
    
    @description.setter
    def description(self, description):
        """
        Set the description of the variant.

        Args:
            description (str): The new description of the variant.
        """
        self._description = description

    @property
    def properties(self):
        """
        Get the properties of the variant.

        Returns:
            dict: The properties of the variant, including sizes, 
            colors, and fit.
        """
        return self._properties
    
    @properties.setter
    def properties(self, properties):
        """
        Set the properties of the variant.

        Args:
            properties (dict): The new properties dictionary, including sizes, 
            colors, and fit.
        """
        self._properties = {
            "sizes": properties["sizes"],
            "colors": properties["colors"],
            "fit": properties["fit"]
        }
