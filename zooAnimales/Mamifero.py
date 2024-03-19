from animal import Animal

class Mamifero(Animal):

    _listado=[]

    caballos=0
    leones=0
    @classmethod
    def crearLeon(cls, nombre,edad, habitat, genero):
        leon=cls(nombre,edad, habitat, genero)
        leon._pelaje=True
        leon._patas=4
        leon._habitad="selva"
        cls._listado.append(leon)
        cls.leones+=1
        return leon

    @classmethod
    def crearCaballos(cls, nombre,edad, habitat, genero):
        caballo=cls(nombre,edad, habitat, genero)
        caballo._pelaje=True
        caballo._patas=4
        caballo._habitad="pradera"
        cls._listado.append(caballo)
        cls.caballos+=1
        return caballo
    
    @classmethod
    def cantidadMamiferos(cls):
        len(cls._listado)

     # Getter para obtener el valor del atributo _listado
    def get_listado(self):
        return self._listado

    # Setter para asignar un nuevo valor al atributo _listado
    def set_listado(self, listado):
        self._listado = listado
    
    
    def getPelaje(self):
        return self._pelaje

    def setPelaje(self, pelaje):
        self._pelaje =pelaje

    # Getter y setter para el atributo _patas
    def getPatas(self):
        return self._patas

    def setPatas(self, patas):
        self._patas = patas



