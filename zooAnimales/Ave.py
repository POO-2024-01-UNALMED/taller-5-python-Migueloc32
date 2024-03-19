from zooAnimales.animal import Animal

class Ave(Animal):

    _listado=[]

    aguilas=0
    halcones=0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas

    @classmethod
    def crearAguila(cls, nombre, edad, genero, colorPlumas="blanco y amarillo"):
        aguila = cls(nombre, edad, "montanas", genero, colorPlumas)
        cls._listado.append(aguila)
        cls.aguilas += 1
        return aguila

    @classmethod
    def crearHalcon(cls, nombre, edad, genero, colorPlumas="café glorioso"):
        halcon = cls(nombre, edad, "montanas", genero, colorPlumas)
        cls._listado.append(halcon)
        cls.halcones += 1
        return halcon

    

    def setColorPlumas(self, color):
        self._colorPlumas=color
    
    def getColorPlumas(self):
        return self._colorPlumas
    
    # Getter para obtener el valor del atributo _listado
    def get_listado(self):
        return self._listado

    # Setter para asignar un nuevo valor al atributo _listado
    def set_listado(self, listado):
        self._listado = listado
    
    
    @classmethod
    def cantiAves(cls):
        len(cls._listado)
    @classmethod
    def totalPorTipo(cls):
        return f"{cls.__name__}s : {cls.aguilas+cls.halcones}"