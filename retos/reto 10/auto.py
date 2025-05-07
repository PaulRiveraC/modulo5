from vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, num_puertas):
        super().__init__(marca, modelo, anio)
        self.num_puertas=num_puertas

    def descripcion(self):
        descripcion_vehiculo= super().descripcion()
        descripcion_vehiculo["Puertas"]=self.num_puertas
        return descripcion_vehiculo

    