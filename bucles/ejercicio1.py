lista=[1,2,3,4,5,"Rolando","Juan",1,2,3,4,8,7,7,"Pedro"]

#Impresion con salto de linea
for i in lista:
    print(i)

#Impresion sin salto de linea
for i in lista:
    print(i, end=(", "))

#Verificacion de elemento
elemento="Juan"
for i in lista:
    if elemento==i:
        print(f"Elemento {elemento} esta dentro de la lista.")
