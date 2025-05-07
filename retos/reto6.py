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