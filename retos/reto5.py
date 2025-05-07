# Listas para guardar los datos
nombres = []
edades = []
año_actual = 2024  # Ajusta este valor si es necesario

# Datos de los pacientes (simulando entrada por consola)
pacientes = [
    "Antonio Moreno 2000",
    "Carmen Díaz 2001",
    "Fernando García 2003",
    "Teresa Rodríguez 2004",
    "José López 2005",
    "Miguel Ángel Ortiz 1999",
    "Lucia Gómez 2000",
    "Francisco Javier Sánchez 2001",
    "Beatriz Domínguez 2002",
    "Adrián López 2011",
    "Martina Pascual 2012",
    "Álvaro Torres 2013",
    "Berta Romero 2014"
]

# Paso 1: Separar nombres y calcular edades
for paciente in pacientes:
    # Dividir el string en partes (ej: ["Antonio", "Moreno", "2000"])
    datos = paciente.split()  
    
    # El nombre es todo menos el último elemento (el año)
    nombre = " ".join(datos[:-1])  
    año_nacimiento = int(datos[-1])  # El último elemento es el año
    
    # Guardar en listas
    nombres.append(nombre)
    edades.append(año_actual - año_nacimiento)

# Paso 2: Mostrar las listas
print("=== Nombres de pacientes ===")
for nombre in nombres:
    print(nombre)

print("\n=== Edades de pacientes ===")
for edad in edades:
    print(edad)

# Paso 3: Encontrar al mayor y al menor
edad_mayor = max(edades)
edad_menor = min(edades)

# Buscar la posición (índice) de esas edades en la lista
indice_mayor = edades.index(edad_mayor)
indice_menor = edades.index(edad_menor)

# Obtener los nombres correspondientes
nombre_mayor = nombres[indice_mayor]
nombre_menor = nombres[indice_menor]

# Resultado final
print(f"\n{nombre_mayor} con {edad_mayor} años es el/la mayor.")
print(f"{nombre_menor} con {edad_menor} años es el/la menor.")