from reto6 import Auto

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