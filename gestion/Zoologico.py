class Zoologico:

    def __init__(self, nombre, ubicacion,):
        self._nombre=nombre
        self._ubicacion=ubicacion
        self._zonas=[]

    def agregarZonas(self, Zona):
        self._zonas.append(Zona)

    def cantidadTotalAnimales(self):
        total=0
        for zona in self.zonas:
            total+=zona.cantidadAnimales()
        return total


