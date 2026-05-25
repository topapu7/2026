def borrarPantalla():
  print("\033c")

def sueldoBase(s,h):
  sb=s*h
  return sb

aumento=0
respuesta='S'
num_trabajadores=0
sumatoria_sueldos=0

while respuesta=='S':
 borrarPantalla()
 nombre=input("Nombre completo del trabajador: ")
 num_horas=int(input("No. de horas de trabajo: "))
 sueldo_hora=float(input("Sueldo por hora: "))
 sueldo_base=sueldoBase(sueldo_hora,num_horas)

 if num_horas==10: 
   aumento=0.20 
 elif num_horas==15:
   aumento=0.30
 elif num_horas==20:
   aumento=0.15
 elif num_horas>=25:
   aumento=0.08
 else: 
   print("Número inválido, no se aplicará el aumento")
 
 aumento_cobrar=sueldo_base*aumento
 sueldo_neto=sueldo_base+aumento_cobrar
 num_trabajadores+=1
 sumatoria_sueldos+=sueldo_neto  
    
 print(f"Sueldo Neto: {sueldo_neto}\nAumento a cobrar: {aumento_cobrar}")
 respuesta=input("¿Deseas hacer otra captura? S/N").upper()


print(f"Cantidad total de trabajadores: {num_trabajadores}")
print(f"Total de sueldos: {sumatoria_sueldos}")