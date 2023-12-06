from uuid_generator import generateUUID


class Product:
    def __init__(self, name):
        self._ID = generateUUID() 
        self._name = name

    @property
    def ID(self):
        return self._ID
    
    @ID.setter
    def ID(self):
        self._ID = generateUUID()

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
