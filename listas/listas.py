#listas

planetas = ["Mercurio","Venus","Tierra","Marte","Jupiter","Saturno","Urano","Neptuno",5,6.8,True]

#Obtener elementos por indice
print(f"Ultimo planeta: {planetas[-1]}")
print(f"Penultimo planeta: {planetas[-2]}")
print(f"Primer planeta: {planetas[0]}")
print(f"Tercer planeta: {planetas[2]}")

#Obtener elementos por sublistas (rangos).
##Obtener desde el indice 1 los 6 primeros elementos
print(planetas[1:6])

##Obtener todos los elementos desde el indice 2
print(planetas[2:])

##Obtener el numero de elementos
print(len(planetas))

#Trabajar con una lista de numeros
gravedad_en_planetas = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
peso_bus=124054

print(f"En la tierra el auto de 2 pisos pesa {peso_bus} N")
print(f"En mercurio el auto de 2 pisos pesa {peso_bus * gravedad_en_planetas[0]} N")

##funcion min y max
print(f"Bus mas pesado en sistema solar: {peso_bus*max(gravedad_en_planetas)} N")
print(f"Bus mas liviano en sistema solar: {peso_bus*min(gravedad_en_planetas)} N")
