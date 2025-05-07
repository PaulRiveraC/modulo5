from datetime import datetime

class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = 0
    
    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
    
    def actualizar_kilometraje(self, kilometraje):
        if kilometraje >= self.kilometraje:
            self.kilometraje = kilometraje
        else:
            print("Error: No se puede reducir el kilometraje")
    
    def realizar_viaje(self, kilometros):
        if kilometros > 0:
            self.kilometraje += kilometros
        else:
            print("Error: La cantidad de kilómetros debe ser positiva")
    
    def estado_auto(self):
        if self.kilometraje < 20000:
            print("Estoy como nuevo")
        elif 20000 <= self.kilometraje <= 100000:
            print("Ya estoy usado")
        else:
            print("¡Ya déjame descansar por favor!")

 # Método de clase para crear autos Toyota del año actual
    @classmethod
    def toyota_del_año_actual(cls, modelo):
        año_actual = datetime.now().year
        return cls(marca="Toyota", modelo=modelo, año=año_actual)
    
    # Método estático para comparar kilometraje
    @staticmethod
    def mismo_kilometraje(auto1, auto2):
        return auto1.kilometraje == auto2.kilometraje
    
    # Método estático adicional: verificar si un auto es clásico (más de 25 años)
    @staticmethod
    def es_clasico(auto):
        año_actual = datetime.now().year
        return (año_actual - auto.año) >= 25
    
    # Método de clase adicional: crear auto eléctrico (marca Tesla por defecto)
    @classmethod
    def auto_electrico(cls, modelo, año):
        return cls(marca="Tesla", modelo=modelo, año=año)
