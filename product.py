from uuid_generator import generateUUID


class Product:
    def __init__(self, name, variants=[]):
        self._ID = generateUUID() 
        self._name = name
        self._variants = variants

    @property
    def ID(self):
        return self._ID
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def variants(self):
        return self._variants
    
    @variants.setter
    def variants(self, variants):
        self._variants = variants
