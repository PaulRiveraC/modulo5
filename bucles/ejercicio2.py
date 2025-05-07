frase=input("Ingresa la frase: ")
letra=input("Ingresa la letra: ")

contador=0
for i in frase:
    if i == letra:
        contador+=1

print(f"La letra {letra} se repite {contador}")

print(frase.count(letra))