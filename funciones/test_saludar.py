import saludar, funcion_parametros

saludar.bienvenida()

#Llamada a la funcion con parametros obligatorios
funcion_parametros.datos("Rolando","Orquera",15,"Bienvenido")
#Llamada a la funcion con parametros obligatorios y opcionales
funcion_parametros.datosOpcionales("Rolando","Orquera",39)
#Llamada a la funcion con nombramiento de parametros
##Se usa para enviar los parametros en cualquier orden
funcion_parametros.datos(mensaje="Hola",apellido="Orquera", nombre="Leonardo",edad=70) 
