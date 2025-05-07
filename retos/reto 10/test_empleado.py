from empleadoMedioTiempo import EmpleadoMedioTiempo
from empleadoTiempoCompleto import EmpleadoTiempoCompleto

juan_emp=EmpleadoTiempoCompleto("Juan Valdez",500)
ana_emp=EmpleadoMedioTiempo("Ana Arco",400)

print(f"Salario: {juan_emp.calcular_salario()}")
print(f"Salario: {ana_emp.calcular_salario()}")

empleados=[juan_emp,ana_emp]

for empleado in empleados:
    print(f"Salario {empleado.nombre}: {empleado.calcular_salario()}")

