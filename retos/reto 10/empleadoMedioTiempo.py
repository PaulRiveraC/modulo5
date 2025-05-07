from empleado import Empleado

class EmpleadoMedioTiempo(Empleado):

    def calcular_salario(self):
        return self.salario*1.10