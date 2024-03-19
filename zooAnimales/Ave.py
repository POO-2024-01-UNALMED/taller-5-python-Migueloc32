from animal import Animal

class Ave(Animal):

    _listado=[]

    aguilas=0
    halcones=0

    @classmethod
    def crearAguila(cls, nombre,edad, habitat, genero):
        aguila=cls(nombre,edad, habitat, genero)
        aguila._colorPlumas="blanco y amarillo"
        aguila._habitad="montanas"
        cls._listado.append(aguila)
        cls.aguilas+=1
        return aguila

    @classmethod
    def crearHalcon(cls, nombre,edad, habitat, genero):
        Halcon=cls(nombre,edad, habitat, genero)
        Halcon._colorPlumas="café glorioso"
        Halcon._habitat="montanas"
        cls._listado.append(Halcon)
        cls.halcones+=1
        return Halcon
    

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