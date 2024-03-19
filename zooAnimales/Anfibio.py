from zooAnimales.animal import Animal

class Anfibio(Animal):

    _listado=[]

    salamandras=0
    ranas=0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero, habitat="selva"):
        salamandra = cls(nombre, edad, habitat, genero, "negro y amarillo", False)
        salamandra._habitat = "selva"  # Corregido error en la asignación de hábitat
        cls._listado.append(salamandra)
        cls.salamandras += 1
        return salamandra

    @classmethod
    def crearRana(cls, nombre, edad, genero, habitat="selva"):
        rana = cls(nombre, edad, habitat, genero, "rojo", True)
        rana._habitat = "selva"  # Corregido error en la asignación de hábitat
        cls._listado.append(rana)
        cls.ranas += 1
        return rana

    
    # Getter y setter para el atributo _colorPiel
    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self, color):
        self._colorPiel = color

    # Getter y setter para el atributo _venenoso
    def isVenenoso(self):
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
    @classmethod
    def totalPorTipo(cls):
        return f"{cls.__name__}s : {cls.salamandras+cls.ranas}"