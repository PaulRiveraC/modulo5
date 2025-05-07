datos = []  # Lista para almacenar los datos

cantidad = int(input("¿Cuántos datos deseas ingresar? "))

# Ingreso de datos
for i in range(cantidad):
    valor = input(f"Ingrese el dato #{i+1}: ")
    
    # Validación para números enteros
    if valor.lstrip('-').isdigit():
        datos.append(int(valor))
    
    # Validación para números decimales
    elif valor.lstrip('-').replace('.', '', 1).isdigit() and valor.count('.') == 1:
        datos.append(float(valor))
    
    # Si no es numérico
    else:
        datos.append(valor)

# Mostrar resultados uno por uno
print("\n=== RESULTADOS ===")
for i in range(len(datos)):
    print(f"El dato {i+1} es: {datos[i]} (Tipo: {type(datos[i]).__name__})")

# Mostrar lista completa al final
print("\nLista completa:")
print(f"Su lista es: {datos}")