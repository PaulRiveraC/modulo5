import random

class Laptop:
    # declaracion de constructor: siempre con __init__(self)
    # self es el primer parametro que debe tener el contructor y representa una autoreferencia a la instancia
    # self se usa para asignar los parametros a los atributos de la clase
    def __init__(self, marca, procesador, memoria, costo=500, impuesto=10):
        self.marca=marca
        self.procesador=procesador
        self.memoria=memoria
        self.costo=costo
        self.impuesto=impuesto

    # Metodos de instancia
    def valor_final(self):
        return self.costo+self.impuesto
    
    def valor_descuento(self, descuento):
        return (self.costo*descuento)/100
    
    
    # Metodos estaticos
    @staticmethod
    def comparar_costo(laptop1, laptop2):
        if laptop1.costo == laptop2.costo:
            return "Los costos son iguales"
        return "Los costos son diferentes"
    
    # Metodos de clase
    @classmethod
    def asus_laptop(cls, costo):
        marca="asus"
        procesador="i5"
        memoria=16
        return cls(marca,procesador,memoria,costo)

        
