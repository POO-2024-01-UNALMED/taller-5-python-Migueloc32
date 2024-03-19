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
        conteoMamiferos = 0
        conteoAves = 0
        conteoReptiles = 0
        conteoPeces = 0
        conteoAnfibios = 0

        todasClases = globals().values()

        for clase in todasClases:
            if issubclass(clase, cls):
                if clase.__name__ == "Mamifero":
                    conteoMamiferos += len(clase._listado)
                elif clase.__name__ == "Ave":
                    conteoAves += len(clase._listado)
                elif clase.__name__ == "Reptil":
                    conteoReptiles += len(clase._listado)
                elif clase.__name__ == "Pez":
                    conteoPeces += len(clase._listado)
                elif clase.__name__ == "Anfibio":
                    conteoAnfibios += len(clase._listado)

        mensaje = (f"Mamiferos: {conteoMamiferos}\n"
                   f"Aves: {conteoAves}\n"
                   f"Reptiles: {conteoReptiles}\n"
                   f"Peces: {conteoPeces}\n"
                   f"Anfibios: {conteoAnfibios}")

        return mensaje
    
    def toString(self):
        if self._zona==None:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"

        return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona}, en el {self._zoo}"
        
