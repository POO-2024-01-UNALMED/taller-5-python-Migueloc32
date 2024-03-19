from zooAnimales.animal import Animal


class Mamifero(Animal):

    _listado=[]

    caballos=0
    leones=0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas

    @classmethod
    def crearLeon(cls, nombre, edad, genero, habitat="Selva"):
        leon = cls(nombre, edad, habitat, genero, True, 4)  # Añadidos valores para pelaje y patas
        leon._habitad = "selva"  # Corregido error en la asignación de hábitat
        cls._listado.append(leon)
        cls.leones += 1
        return leon

    @classmethod
    def crearCaballo(cls, nombre, edad, genero, habitat="pradera"):
        caballo = cls(nombre, edad, habitat, genero, True, 4)  # Añadidos valores para pelaje y patas
        caballo._habitad = "pradera"  # Corregido error en la asignación de hábitat
        cls._listado.append(caballo)
        cls.caballos += 1
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
    
    
    def isPelaje(self):
        return self._pelaje

    def setPelaje(self, pelaje):
        self._pelaje =pelaje

    # Getter y setter para el atributo _patas
    def getPatas(self):
        return self._patas

    def setPatas(self, patas):
        self._patas = patas

    @classmethod
    def totalPorTipo(cls):
        return f"{cls.__name__}s : {cls.caballos+cls.leones}"


