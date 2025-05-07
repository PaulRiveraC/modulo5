from vehiculo import Vehiculo
from moto import Moto
from auto import Auto

moto=Moto("Kawasaki","Ninja",2025,"Deportiva")
auto=Auto("Kawasaki","Ninja",2025,5)

print("**Descripcion Moto**")
print(moto.descripcion())
print("**Descripcion Auto**")
print(auto.descripcion())
print("**Polimorfismo**")

vehiculos=[moto,auto]
for vehiculo in vehiculos:
    print(vehiculo.descripcion())