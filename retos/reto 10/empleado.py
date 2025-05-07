from abc import ABC,abstractmethod

class Empleado(ABC):
    def __init__(self,nombre,salario):
        super().__init__()
        self.nombre=nombre
        self.salario=salario

    @abstractmethod
    def calcular_salario(self):
        pass
    