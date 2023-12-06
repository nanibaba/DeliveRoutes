from product import Product


class Variant(Product):
    def __init__(self, name, variant_name, country, price,
                 description, properties):
        super().__init__(name)
        self._variant_name = variant_name
        self._country_of_origin = country
        self._price = price
        self._description = description
        self._properties = {
            "sizes": properties['sizes'],
            "colors": properties['colors'],
            "fit": properties['fit']
        }

    @property
    def variant_name(self):
        return self._variant_name 
    
    @variant_name.setter
    def variant_name(self, variant_name):
        self._variant_name = variant_name
    
    @property
    def country_of_origin(self):
        return self._country_of_origin
    
    @country_of_origin.setter
    def countryOfOrigin(self, country):
        self._country_of_origin = country

    @property
    def price(self):
        return f"${self._price}"
    
    @price.setter
    def price(self, price):
        self._price = price

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        self._description = description

    @property
    def properties(self):
        return self._properties
    
    @properties.setter
    def properties(self, properties):
        self._properties = {
            "sizes": properties['sizes'],
            "colors": properties['colors'],
            "fit": properties['fit']
        }

