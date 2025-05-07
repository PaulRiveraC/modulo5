datos = []  # Lista para almacenar los datos

cantidad = int(input("¿Cuántos datos deseas ingresar? "))

for i in range(cantidad):
    valor = input(f"Ingrese el dato #{i+1}: ")
    
    # Validación para números enteros (positivos y negativos)
    if valor.lstrip('-').isdigit():
        datos.append(int(valor))
    
    # Validación para números decimales (positivos y negativos)
    elif valor.lstrip('-').replace('.', '', 1).isdigit() and valor.count('.') == 1:
        datos.append(float(valor))
    
    # Si no es numérico
    else:
        datos.append(valor)

# Mostrar resultados
print("\n" + "="*30)
print(f"Su lista es: {datos}")
print("="*30)
print("Detalle por tipo:")
for elemento in datos:
    print(f"- {elemento} ({type(elemento).__name__})")