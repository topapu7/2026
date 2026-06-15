#Función que borre pantalla
def borrarPantalla():
   print("\033c")

#1.- Funcion que no recibe parametros y no regresa valor
def funcion1():
   #borrarPantalla()
   nombre=input("Escribe el nombre: ").strip().upper()
   apellidos=input("Escribe los apellidos: ").strip().upper()
   print(f"El nombre es: {nombre} {apellidos}")

#3.- Funcion que recibe parametros y no regresa valor 
def funcion3(nombre,apellidos):
   borrarPantalla()
   print(f"El nombre es: {nombre} {apellidos}")


#2.- Funcion que no recibe parametros y regresa valor
def funcion2():
   borrarPantalla()
   nombre=input("Escribe el nombre: ").strip().upper()
   apellidos=input("Escribe los apellidos: ").strip().upper()
   return nombre,apellidos

nom,ape=funcion2()
print(f"El nombre es: {nom} {ape}")

#4.- Funcion que recibe parametros y regresa valor
def funcion4(nom, ape):
    nombre = nom.strip().upper()
    apellido = ape.strip().upper()
    return nombre, apellido