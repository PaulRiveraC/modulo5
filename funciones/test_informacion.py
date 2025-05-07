import informacion

anio_actual=2025
cantidad=13

for i in range(cantidad):
    nombre=input("Ingresar nombre: ")
    edad= int(input("Ingresar año nacimiento: "))
    informacion.agregar_nombre(nombre)
    informacion.agregar_edad(anio_actual-edad)

print("***Nombres***")
informacion.imprimir(informacion.nombre_paciente)
print("***Edades***")
informacion.imprimir(informacion.edad)
print("***Paciente Mayor***")
informacion.obtener_mayor()
print("***Paciente Menor***")
informacion.obtener_menor()
