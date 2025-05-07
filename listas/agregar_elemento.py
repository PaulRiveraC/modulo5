#Agregar elementos a una lista
lista=[1,2,3,4,5]
##Agrega elemento al final de la lista
lista.append(6)
##Agrega elemento por indice
lista.insert(2,"Rolando")
##Agrega una sublista al final
lista.extend([6,7,8,9])
print(lista)

#Concatenar listas
lista2=[1,2,3]
lista3=[5,6,7]
lista4=lista2+lista3
print(lista4)