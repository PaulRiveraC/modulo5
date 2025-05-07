import emoji

cantidad_frase=int(input("Cuantas frases desea ingresar: "))

for i in range(cantidad_frase):
    frase=input("Ingrese la frase: ")
    emoji.encontrar1_palabra(frase)
    emoji.agregar_frase(frase)