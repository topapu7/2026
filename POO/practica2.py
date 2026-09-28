"""
Ejercicio Practico #2 “Modelar y Diagramar en POO”

"""
print("\033c")

#Clase de Coches

class Coches:
    def __init__(self,color,marca,velocidad):
        self.__color=color
        self.__marca=marca
        self.__velocidad=velocidad

    def acelarar(self):
        self.__velocidad+=1 

    def frenar(self):
        self.__velocidad-=1 

    def tocar_claxon(self):
        print("pi pi pi")
        

coche1=Coches("Blanco","VW",220)
coche2=Coches ("Azul", "Nissan",180) 

# print (f"El color del coche 1 es: {coche1.__color}") No se pueden utilizar directamente los atributos porque son privados. 
print (f"El claxon del coche 1 hace:")
coche1.tocar_claxon()

print (f"El claxon del coche 2 hace:")
coche2.tocar_claxon()

coche1.acelarar()
coche1.acelarar()
coche1.acelarar()
coche1.acelarar()
coche1.frenar()


#Instanciar o crear objetos de la clase Coches







