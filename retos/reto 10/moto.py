from vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio,tipo):
        super().__init__(marca, modelo, anio)
        self.tipo=tipo

    def descripcion(self):
        descripcion_vehiculo = super().descripcion()
        descripcion_vehiculo["Tipo"]=self.tipo
        return descripcion_vehiculo
