print("KRAKETRAVELS - CONTROL DE VELOCIDAD")
print("----------------------------------")

# 1. Pedir el país
print("\nPaíses disponibles:")
print("1. Ecuador")
print("2. Colombia")
print("3. Perú")

pais = input("Elija un país (1-3): ")

# 2. Pedir la zona
print("\nZonas disponibles:")
print("1. Urbana")
print("2. Rural")
print("3. Perimetral")

zona = input("Elija una zona (1-3): ")

# 3. Pedir la velocidad
velocidad = float(input("\nIngrese su velocidad en km/h: "))

# 4. Verificar Ecuador
if pais == "1":
    if zona == "1":  # Ecuador - Urbana
        if velocidad < 10:
            print("\nALERTA: Muy lento (mínimo 10 km/h)")
        elif velocidad > 50:
            print("\nALERTA: Muy rápido (máximo 50 km/h)")
        else:
            print("\nCorrecto (10-50 km/h)")
    
    elif zona == "2":  # Ecuador - Rural
        if velocidad < 51:
            print("\nALERTA: Muy lento (mínimo 51 km/h)")
        elif velocidad > 70:
            print("\nALERTA: Muy rápido (máximo 70 km/h)")
        else:
            print("\nCorrecto (51-70 km/h)")
    
    elif zona == "3":  # Ecuador - Perimetral
        if velocidad < 71:
            print("\nALERTA: Muy lento (mínimo 71 km/h)")
        elif velocidad > 90:
            print("\nALERTA: Muy rápido (máximo 90 km/h)")
        else:
            print("\nCorrecto (71-90 km/h)")

# 5. Verificar Colombia
elif pais == "2":
    if zona == "1":  # Colombia - Urbana
        if velocidad < 10:
            print("\nALERTA: Muy lento (mínimo 10 km/h)")
        elif velocidad > 30:
            print("\nALERTA: Muy rápido (máximo 30 km/h)")
        else:
            print("\nCorrecto (10-30 km/h)")
    
    # ... (continuar con otras zonas de Colombia)

# 6. Verificar Perú
elif pais == "3":
    if zona == "1":  # Perú - Urbana
        if velocidad < 10:
            print("\nALERTA: Muy lento (mínimo 10 km/h)")
        elif velocidad > 40:
            print("\nALERTA: Muy rápido (máximo 40 km/h)")
        else:
            print("\nCorrecto (10-40 km/h)")
    
    # ... (continuar con otras zonas de Perú)

# 7. Mensaje si eligió mal el país
else:
    print("\nError: País no válido")

print("\nGracias por usar nuestro sistema!")