'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones

'''

n=int(input("¿De que número desea la tabla? "))

tabla=n*1
print(f"{n}*1={tabla}")
tabla=n*2
print(f"{n}*2={tabla}")
tabla=n*3
print(f"{n}*3={tabla}")
tabla=n*4
print(f"{n}*4={tabla}")
tabla=n*5
print(f"{n}*5={tabla}")
tabla=n*6
print(f"{n}*6={tabla}")
tabla=n*7
print(f"{n}*7={tabla}")
tabla=n*8
print(f"{n}*8={tabla}")
tabla=n*9
print(f"{n}*9={tabla}")
tabla=n*10
print(f"{n}*10={tabla}")

input()

'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Con estructuras de control
  2.- Sin funciones

'''

print("\033c")

n=int(input("¿De que número desea la tabla? "))

for i in range (1,11,):
    tabla=n*i
    print(f"{n}*{i}={tabla}")

'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Con estructuras de control solo while
  2.- Sin funciones

'''
n=int(input("¿De que número desea la tabla? "))
i=1
while i!=11:
    tabla=n*i
    print(f"{n}*{i}={tabla}")
    i+=1

input()

'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Con funciones

'''
def tabla(n,i):
    tabla=n*i
    print(f"{n}*{i}={tabla}")
    i+=1
    return i


n=int(input("¿De que número desea la tabla? "))
i=1

i=tabla(n,i)
i=tabla(n,i)
i=tabla(n,i)
i=tabla(n,i)
i=tabla(n,i)
i=tabla(n,i)
i=tabla(n,i)
i=tabla(n,i)
i=tabla(n,i)
i=tabla(n,i)

input()

'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Con estructuras de control
  2.- Con funciones

'''

def tabla(n,i):
    for i in range (1,11):
      tabla=n*i
      print(f"{n}*{i}={tabla}")

n=int(input("¿De que número desea la tabla? "))
i=1

tabla(n,i)

input()
