nombre_paciente=[]
edad=[]
def agregar_nombre (datos):
    nombre_paciente.append(datos)

def agregar_edad (datos):
    edad.append(datos)


def imprimir(info):
    for dato in info:
        print(f"- {dato}")

def obtener_mayor():
    edad_maxima=max(edad)
    indice=edad.index(edad_maxima)
    nombre=nombre_paciente[indice]
    print(f"{nombre} con la edad de {edad_maxima} años es mayor a los demás pacientes")

def obtener_menor():
    edad_minima=min(edad)
    indice=edad.index(edad_minima)
    nombre=nombre_paciente[indice]
    print(f"{nombre} con la edad de {edad_minima} años es menor a los demás pacientes")