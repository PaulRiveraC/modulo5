from reto7 import Auto

# Crear un auto
mi_auto = Auto("Toyota", "Corolla", 2020)

# Mostrar información
print("=== Información del auto ===")
mi_auto.mostrar_informacion()

# Actualizar kilometraje correctamente
mi_auto.actualizar_kilometraje(15000)
print(f"\nKilometraje actual: {mi_auto.kilometraje} km")

# Intentar reducir el kilometraje (debe mostrar error)
mi_auto.actualizar_kilometraje(10000)

# Realizar un viaje
mi_auto.realizar_viaje(500)
print(f"\nKilometraje después del viaje: {mi_auto.kilometraje} km")

# Intentar viaje con km negativos (debe mostrar error)
mi_auto.realizar_viaje(-200)

# Ver estado del auto
print("\n=== Estado del auto ===")
mi_auto.estado_auto()

# Cambiar a estado "usado"
mi_auto.actualizar_kilometraje(25000)
mi_auto.estado_auto()

# Cambiar a estado "descansar"
mi_auto.actualizar_kilometraje(120000)
mi_auto.estado_auto()


print("=== Demostración de métodos ===")

# 1. Método de clase: toyota_del_año_actual
print("\n1. Creando auto Toyota del año actual:")
auto_toyota = Auto.toyota_del_año_actual("Corolla")
auto_toyota.mostrar_informacion()

# 2. Método estático: mismo_kilometraje
print("\n2. Comparando kilometraje entre autos:")
auto1 = Auto("Ford", "Fiesta", 2018)
auto1.actualizar_kilometraje(50000)
auto2 = Auto("Chevrolet", "Spark", 2019)
auto2.actualizar_kilometraje(50000)
auto3 = Auto("Nissan", "Sentra", 2020)
auto3.actualizar_kilometraje(30000)

print(f"¿Auto1 y Auto2 tienen mismo kilometraje?: {Auto.mismo_kilometraje(auto1, auto2)}")
print(f"¿Auto1 y Auto3 tienen mismo kilometraje?: {Auto.mismo_kilometraje(auto1, auto3)}")

# 3. Método estático adicional: es_clasico
print("\n3. Verificando si autos son clásicos:")
auto_viejo = Auto("Volkswagen", "Escarabajo", 1970)
auto_nuevo = Auto("Hyundai", "Tucson", 2020)

print(f"¿El VW Escarabajo 1970 es clásico?: {Auto.es_clasico(auto_viejo)}")
print(f"¿El Hyundai Tucson 2020 es clásico?: {Auto.es_clasico(auto_nuevo)}")

# 4. Método de clase adicional: auto_electrico
print("\n4. Creando auto eléctrico (Tesla):")
tesla = Auto.auto_electrico("Model 3", 2022)
tesla.mostrar_informacion()