class zona:
    def __init__(self,nombre, zoo):
        self._nombre=nombre
        self._zoo=zoo
        self._animales=[]
        

    def agregarAnimales(self, animales):
        self._animales.append(animales) 
    def cantidadTotalAnimales(self):
        return len(self._animales)
    