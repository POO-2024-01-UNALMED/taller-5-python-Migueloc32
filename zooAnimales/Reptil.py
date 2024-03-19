from animal import Animal

class Reptil(Animal):

    _listado=[]

    iguanas=0
    serpientes=0

    @classmethod
    def crearIguana(cls, nombre,edad, habitat, genero):
        iguana=cls(nombre,edad, habitat, genero)
        iguana._colorEscamas="verde"
        iguana._largoCola=3
        iguana._habitad="humedal"
        cls._listado.append(iguana)
        cls.iguanas+=1
        return iguana

    @classmethod
    def crearSerpiente(cls, nombre,edad, habitat, genero):
        serpiente=cls(nombre,edad, habitat, genero)
        serpiente._colorEscamas="verde"
        serpiente._largoCola=1
        serpiente._habitat="jungla"
        cls._listado.append(serpiente)
        cls.serpientes+=1
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