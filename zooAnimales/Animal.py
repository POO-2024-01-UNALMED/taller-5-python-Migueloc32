class Animal:

    _totalAnimales=0

    def __init__(self, nombre, edad, habitat, genero,):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        self._zona=None

    # Getter y Setter para nombre
    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    # Getter y Setter para edad
    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    # Getter y Setter para habitat
    def getHabitat(self):
        return self._habitat

    def setHabitat(self, habitat):
        self._habitat = habitat

    # Getter y Setter para genero
    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero

    # Getter y Setter para zona
    def getZona(self):
        return self._zona

    def setZona(self, zona):
        self._zona = zona

    def setTotalAnimales(self, animales):
        self._totalAnimales=animales
    
    def getTotalAnimales(self):
        return self._totalAnimales
    
    def movimiento():
        pass
    
    @classmethod
    def totalPorTipo(cls):
        return f"{cls.__name__}s : {cls._totalAnimales}"
    
    def toString(self):
        if self._zona==None:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"

        return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona}, en el {self._zoo}"
        
