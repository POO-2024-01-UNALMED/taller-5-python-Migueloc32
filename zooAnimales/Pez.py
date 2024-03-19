from zooAnimales.animal import Animal


class Pez(Animal):

    _listado=[]

    salmones=0
    bacalaos=0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas

    @classmethod
    def crearSalmon(cls, nombre, edad, genero, habitat="oceano", colorEscamas="rojo", cantidadAletas=6):
        salmon = cls(nombre, edad, habitat, genero, colorEscamas, cantidadAletas)
        cls._listado.append(salmon)
        cls.salmones += 1
        return salmon

    @classmethod
    def crearBacalao(cls, nombre, edad, genero, habitat="oceano", colorEscamas="gris", cantidadAletas=6):
        bacalao = cls(nombre, edad, habitat, genero, colorEscamas, cantidadAletas)
        cls._listado.append(bacalao)
        cls.bacalaos += 1
        return bacalao
    
    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self,color):
        self._colorEscamas = color

    # Getter y setter para el atributo _largoCola
    def getCantidadAletas(self):
        return self._cantidadAletas

    def setCantidadAletas(self, aletas):
        self._cantidadAletas = aletas
    # Getter para obtener el valor del atributo _listado
    def get_listado(self):
        return self._listado

    # Setter para asignar un nuevo valor al atributo _listado
    def set_listado(self, listado):
        self._listado = listado
    @classmethod
    def cantidadPez(cls):
        len(cls._listado)
    @classmethod
    def totalPorTipo(cls):
        return f"{cls.__name__}s : {cls.salmones+cls.bacalaos}"