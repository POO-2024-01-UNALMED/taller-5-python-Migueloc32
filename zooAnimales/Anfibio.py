from animal import Animal

class Anfibio(Animal):

    _listado=[]

    salamandras=0
    ranas=0

    @classmethod
    def crearSalamandra(cls, nombre,edad, habitat, genero):
        salamandra=cls(nombre,edad, habitat, genero)
        salamandra._colorPiel="negro y amarillo"
        salamandra._venenoso=False
        salamandra._habitat="selva"
        cls._listado.append(salamandra)
        cls.salamandras+=1
        return salamandra

    @classmethod
    def crearRana(cls, nombre,edad, habitat, genero):
        rana=cls(nombre,edad, habitat, genero)
        rana._colorPiel="rojo"
        rana._venenoso=True
        rana._habitat="selva"
        cls._listado.append(rana)
        cls.ranas+=1
        return rana

    
    # Getter y setter para el atributo _colorPiel
    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self, color):
        self._colorPiel = color

    # Getter y setter para el atributo _venenoso
    def getVenenoso(self):
        return self._venenoso

    def setVenenoso(self, venenoso):
        self._venenoso = venenoso
    # Getter para obtener el valor del atributo _listado
    def get_listado(self):
        return self._listado
    # Setter para asignar un nuevo valor al atributo _listado
    def set_listado(self, listado):
        self._listado = listado
    @classmethod
    def cantidadAnfibios(cls):
        len(cls._listado)