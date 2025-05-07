from laptop import Laptop
import random

# Herencia: se pasa por argumento la clase padre "Laptop"
class Laptop_Business(Laptop):
    def __init__(self, marca, memoria, almacenamiento, duración_bateria, costo=500, impuesto=10):
        super().__init__(marca, "i5", memoria, 800,12)
        self.almacenamiento=almacenamiento
        self.duración_bateria=duración_bateria

    def __str__(self):
        return f"Marca: {self.marca} \n Memoria: {self.memoria} \n Almacenamiento: {self.almacenamiento} \n Duracion bateria: {self.duración_bateria} \n"

    # Sobreescritura: se cambia el cuerpo del metodo realizar_diagnostico_sistema 
    def realizar_diagnostico_sistema(self):
        diagnostico_basico = super().realizar_diagnostico_sistema()
        resultado_procesamiento = self.realizar_diagnostico_procesador()
        diagnostico_basico["Resultado procesador"]=resultado_procesamiento
        resultado_conectividad=self.verificar_conectividad_red()
        diagnostico_basico["Conectividad de red"]=resultado_conectividad
        return diagnostico_basico


    def realizar_diagnostico_procesador(self):
        roles=["contador","administrador","gerencia"]
        resultados={}
        for rol in roles:
            procesador_base=3
            if "contador" == rol:
                tipo_procesador = f"i{procesador_base}"
            elif "administrador" == rol:
                tipo_procesador = f"i{procesador_base+2}"
            else:
                tipo_procesador = f"i{procesador_base+4}"

            resultados[rol] = f"core {tipo_procesador}"
        return resultados
    
    def verificar_conectividad_red(self):
        resultado={
            "WIFI" : "OK" if random.choice([True,False]) else "Sin conexion",
            "ACCESO SERVIDORES" : "OK" if random.choice([True,False]) else "Denegado",
            "LATENCIA" : "OK" if random.choice([True,False]) else "Alta",
        }
        return resultado



