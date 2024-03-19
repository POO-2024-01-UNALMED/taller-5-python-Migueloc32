from Animal import Animal

class Pez(Animal):

    _listado=[]

    salmones=0
    bacalaos=0

    @classmethod
    def crearSalmon(cls, nombre,edad, habitat, genero):
        salmon=cls(nombre,edad, habitat, genero)
        salmon._colorEscamas="rojo"
        salmon._cantidadAletas=6
        salmon._habitat="oceano"
        cls._listado.append(salmon)
        cls.salmones+=1
        return salmon

    @classmethod
    def crearSerpiente(cls, nombre,edad, habitat, genero):
        bacalao=cls(nombre,edad, habitat, genero)
        bacalao._colorEscamas="gris"
        bacalao._cantidadAletas=6
        bacalao._habitat="oceano"
        cls._listado.append(bacalao)
        cls.bacalaos+=1
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