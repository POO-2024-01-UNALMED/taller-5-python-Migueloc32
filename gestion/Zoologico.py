
class Zoologico:

    def __init__(self, nombre, ubicacion,):
        self._nombre=nombre
        self._ubicacion=ubicacion
        self._zonas=[]

    def agregarZonas(self, Zona):
        self._zonas.append(Zona)

    def cantidadTotalAnimales(self):
        total=0
        for zona in self._zonas:
            total+=zona.cantidadAnimales()
        return total
    
    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._ubicacion

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def getZona(self):
        return self._zonas

    def setZonas(self, zonas):
        self._zonas = zonas

     