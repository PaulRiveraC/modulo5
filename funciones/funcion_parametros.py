
#Funcion con parametros obligatorios
def datos(nombre,apellido,edad,mensaje):
    if edad < 18:
        print(f"{mensaje} {nombre} {apellido} es menor de edad")
    else:
        print(f"{mensaje} {nombre} {apellido} es mayor de edad")


#Funcion con parametros obligatorios y opcionales
##Los parametros opcionales van al final
def datosOpcionales(nombre,apellido,edad,mensaje="Bienvenido"):
    if edad < 18:
        print(f"{mensaje} {nombre} {apellido} es menor de edad")
    else:
        print(f"{mensaje} {nombre} {apellido} es mayor de edad")

