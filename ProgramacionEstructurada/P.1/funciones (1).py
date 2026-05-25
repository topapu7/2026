
"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""
#Función que borre pantalla
def borrarPantalla():
   print("\033c")

#1.- Funcion que no recibe parametros y no regresa valor
def funcion1():
   borrarPantalla()
   nombre=input("Escribe el nombre: ").strip().upper()
   apellidos=input("Escribe los apellidos: ").strip().upper()
   print(f"El nombre es: {nombre} {apellidos}")
funcion1()

#3.- Funcion que recibe parametros y no regresa valor 
def funcion3(nombre,apellidos):
   borrarPantalla()
   print(f"El nombre es: {nombre} {apellidos}")
funcion3

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

#Invocar las funciones

funcion1()

nombre=input("Nombre: ").strip().upper()
apellido=input("Apellido: ").strip().upper()
funcion3(nombre, apellido)

nombre, apellido = funcion2()
print(f"El nombre del alumno es {nombre} {apellido}")

nombre = input("Nombre: ").strip().upper()
apellido = input("Apellido: ").strip().upper()
nom, ape = funcion4(nombre, apellido) 
print(f"El nombre del alumno es: {nom} {ape}")


