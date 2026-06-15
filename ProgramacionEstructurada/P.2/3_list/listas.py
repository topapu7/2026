print("\033c")

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
# numeros=[23,45,23,33,25,100,-100]
# print(numeros)

# lista="["
# for i in numeros:
#     lista+=f"{i}, " 
# print(f"{lista}]")

# lista="["
# for i in range(0,len(numeros)):
#     lista+=f"{numeros[i]}, "
# print(f"{lista}]")

# lista="["
# i=0
# while i<len(numeros):    
#     lista+=f"{numeros[i]}, " 
#     i+=1
# print(f"{lista}]")

# print(1254)
#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
# palabras=["Hola","NBA","Ganador","Perdedor"]
# palabra=input("Dame una palabra: ")

#1er forma
# encontro=palabra in palabras
# if encontro==True: 
#     print("La palabra ",palabra," si existe en la lista")
# else:
#     print("La palabra ",palabra," no esta en la lista")

#2DA FORMA
# palabras=["Hola","NBA","Ganador","Perdedor", "Hola"]
# palabra=input("Dame la palabra a buscar: ")

# encontre=False
# for i in palabras:
#     if i in palabras:
#         encontre=True


# if encontre:

#      print("Esta palabra: ", palabra, ", si se encuentra en la lista" )
# else:
#     print("Esta palabra: ", palabra, ", no se encuentra en la lista")


#3er FORMA
# palabras=["Hola","NBA","Ganador","Perdedor", "Hola"]
# palabra=input("Dame la palabra a buscar: ")

# encontre=False
# n=0
# while n<len(palabras):
#       if palabras[n] in palabra:
#         encontre=True
#         n=+1

# if encontre:
#      print("Esta palabra: ", palabra, ", si se encuentra en la lista" )
# else:
#     print("Esta palabra: ", palabra, ", no se encuentra en la lista")


#Ejemplo 3 Añadir elementos a la lista
# lista=[]
# true="S"
# while true=="S":
#     valor=input("Dame un valor de la lista").upper().strip()
#     lista.append(valor)
#     true=input("Deseas añadir otro elemento a la lista? (S/N)").upper().strip()
  

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda
agenda=[
            ["Carlos","6181234567"],
            ["Juan", "6182334567"],
            ["Tony","6182342323"]
        ]

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])

lista=""
for r in range(0,3):
    for c in range(0,2):
        lista+=f"{agenda[r][c]}, "
    lista+="\n"
print("["+lista+"]")

print(agenda)

for i in agenda:
    print(i)