# order.py
# This file contains the Order class which represents a customer's order. 
# It includes details such as client name, delivery location, and a list of 
# products. 
# Each order is uniquely identified by an ID generated using the generateUUID 
# function.

from uuid_generator import generateUUID


class Order():
    def __init__(self, client_name, delivery_location, products=[]):
        """
        Initialize a new Order instance.

        Args:
            client_name (str): The name of the client placing the order.
            delivery_location (str): The delivery address for the order.
            products (list): A list of products included in the order. 
            Defaults to an empty list.
        """
        self._ID = generateUUID() 
        self._client_name = client_name
        self._delivery_location = delivery_location
        self._products = products

    @property
    def ID(self):
        """
        Get the unique ID of the order.

        Returns:
            UUID: The unique identifier of the order.
        """
        return self._ID

    @property
    def client_name(self):
        """
        Get the client's name associated with the order.

        Returns:
            str: The name of the client.
        """
        return self._client_name 
    
    @client_name.setter
    def client_name(self, client_name):
        """
        Set the client's name for the order.

        Args:
            client_name (str): The new name of the client.
        """
        self._client_name = client_name
    
    @property
    def delivery_location(self):
        """
        Get the delivery location for the order.

        Returns:
            str: The delivery address of the order.
        """
        return self._delivery_location
    
    @delivery_location.setter
    def delivery_location(self, delivery_location):
        """
        Set the delivery location for the order.

        Args:
            delivery_location (str): The new delivery address for the order.
        """
        self._delivery_location = delivery_location

    @property
    def products(self):
        """
        Get the list of products in the order.

        Returns:
            list: The products included in the order.
        """
        return self._products
    
    @products.setter
    def products(self, products):
        """
        Set the list of products for the order.

        Args:
            products (list): The new list of products for the order.
        """
        self._products = products
