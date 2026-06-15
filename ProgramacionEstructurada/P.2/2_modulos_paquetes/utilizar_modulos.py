#1er utilizar los modulos 
import modulos

modulos.borrarPantalla()
modulos.funcion1()

nom="Antonio"
ape="Galarza"

nom,ape=modulos.funcion4(nom,ape)
print(f"Nombre: {nom}\nApellidos:{ape}")

# #modulos.funcion3(nom,ape)
# #print(f"{modulos.ape}")


# #2da formar de utilizar modulos

from modulos import borrarPantalla,funcion4

borrarPantalla()

nom="Antonio"
ape="Galarza"

nom,ape=funcion4(nom,ape)
print(f"Nombre: {nom}\nApellidos:{ape}")
