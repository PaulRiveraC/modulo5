from laptop_business import Laptop_Business

def test_laptop_business():
    print("=== TEST DE LAPTOP BUSINESS ===")
    
    # Crear laptop empresarial básica
    laptop1 = Laptop_Business(
        marca="HP",
        procesador="i5",
        memoria=16,
        almacenamiento=512,
        duracion_bateria=8
    )
    
    print("\nDiagnóstico inicial:")
    for k, v in laptop1.realizar_diagnostico_sistema().items():
        print(f"{k}: {v}")
    
    # Crear laptop gerencial preconfigurada
    laptop_gerente = Laptop_Business.laptop_gerencial()
    
    print("\nDiagnóstico laptop gerencial:")
    for k, v in laptop_gerente.realizar_diagnostico_sistema().items():
        print(f"{k}: {v}")
    
    # Actualizar conectividad
    print("\nActualizando conectividad...")
    print("Nuevo estado:", laptop1.actualizar_conectividad())

if __name__ == "__main__":
    test_laptop_business()