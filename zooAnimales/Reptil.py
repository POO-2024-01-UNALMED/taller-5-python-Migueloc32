from zooAnimales.animal import Animal


class Reptil(Animal):

    _listado=[]

    iguanas=0
    serpientes=0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola

    @classmethod
    def crearIguana(cls, nombre, edad, genero, habitat="humedal"):
        iguana = cls(nombre, edad, habitat, genero, "verde", 3)
        iguana._habitat = "humedal"  # Corregido error en la asignación de hábitat
        cls._listado.append(iguana)
        cls.iguanas += 1
        return iguana

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero, habitat="jungla"):
        serpiente = cls(nombre, edad, habitat, genero, "verde", 1)
        serpiente._habitat = "jungla"  # Corregido error en la asignación de hábitat
        cls._listado.append(serpiente)
        cls.serpientes += 1
        return serpiente

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self,color):
        self._colorEscamas = color

    # Getter y setter para el atributo _largoCola
    def getLargoCola(self):
        return self._largoCola

    def setLargoCola(self, largo):
        self._largoCola = largo
    # Getter para obtener el valor del atributo _listado
    def get_listado(self):
        return self._listado

    # Setter para asignar un nuevo valor al atributo _listado
    def set_listado(self, listado):
        self._listado = listado
    @classmethod
    def cantidadReptil(cls):
        len(cls._listado)
    @classmethod
    def totalPorTipo(cls):
        return f"{cls.__name__}s : {cls.iguanas+cls.serpientes}"