from empleado import Empleado

class EmpleadoTiempoCompleto(Empleado):

    def calcular_salario(self):
        return self.salario*1.20
