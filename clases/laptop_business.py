from laptop import Laptop
import random

class Laptop_Business(Laptop):
    ROLES_EMPRESA = {
        "contador": {"procesador_min": "i3", "memoria_min": 8, "almacenamiento_min": 256},
        "administrador": {"procesador_min": "i5", "memoria_min": 16, "almacenamiento_min": 512},
        "gerente": {"procesador_min": "i7", "memoria_min": 32, "almacenamiento_min": 1024}
    }

    def __init__(self, marca, procesador, memoria, almacenamiento, duracion_bateria, costo=800, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.almacenamiento = almacenamiento  # en GB
        self.duracion_bateria = duracion_bateria  # en horas
        self.conectividad = self.verificar_conectividad_red()  # Estado inicial

    def realizar_diagnostico_sistema(self):
        """Diagnóstico extendido para laptops empresariales"""
        diagnostico = super().realizar_diagnostico_sistema()
        diagnostico.update({
            "Almacenamiento": f"{self.almacenamiento} GB",
            "Duración batería": f"{self.duracion_bateria} horas",
            "Conectividad": self.conectividad,
            "Compatibilidad roles": self.verificar_compatibilidad_roles()
        })
        return diagnostico

    def verificar_compatibilidad_roles(self):
        """Verifica para qué roles empresariales es adecuada esta laptop"""
        compatibilidad = {}
        for rol, requisitos in self.ROLES_EMPRESA.items():
            procesador_ok = self.procesador >= requisitos["procesador_min"]
            memoria_ok = self.memoria >= requisitos["memoria_min"]
            almacenamiento_ok = self.almacenamiento >= requisitos["almacenamiento_min"]
            compatibilidad[rol] = all([procesador_ok, memoria_ok, almacenamiento_ok])
        return compatibilidad

    def verificar_conectividad_red(self):
        """Verifica el estado de la conectividad de red"""
        return {
            "WiFi": random.choice(["Excelente", "Buena", "Limitada", "Sin conexión"]),
            "Servidores": "OK" if random.random() > 0.3 else "Error",
            "Latencia": f"{random.randint(5, 150)} ms",
            "VPN": random.choice([True, False])
        }

    def actualizar_conectividad(self):
        """Actualiza el estado de conectividad"""
        self.conectividad = self.verificar_conectividad_red()
        return self.conectividad

    @classmethod
    def laptop_gerencial(cls, almacenamiento=1024):
        """Crea una laptop configurada para gerentes"""
        return cls(
            marca="Dell",
            procesador="i7",
            memoria=32,
            almacenamiento=almacenamiento,
            duracion_bateria=12,
            costo=1500
        )