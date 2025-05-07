datos=[]
caracteres=input("Ingrese los datos deseados: ")

for i in caracteres:
    if i.isdigit() or i.isalpha():
        datos.append(i)

print(f"Su lista de datos es: {datos}")

