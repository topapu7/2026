from coches import coches, cochesBD
print("\033c")

class App:
    def __init__(self):
        self.main()
    
    def borrarPantalla(self):
        print("\033c")
        
    def esperarTecla(self):
        input("...¡Oprima cualquier tecla para contunuar!...")
    def terminarSistema(self):
        input("....:::: GRACIAS POR UTILIZAR NUESTRO SISTEMA, \n  vuelve pronto ::::...")
    def opcionInvalida(self):
        input("\n\t.... ¡Opcion invalidad, vuelve a intentarlo!.... ") 
        
    def menu_acciones(self,tipo):
        print(f"\t\t....:::: Menu de {tipo} ::::...\n")
        opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Regresar\n\t\tEscribe una opción: ").strip()
        return opcion
    def menu_cocches(self):
        opc =True
        while opc:
            self.borrarPantalla()
            opc=self.menu_acciones("Coches")
            match opc:
                case "1":
                    cochesito= self.datos_coches("Coches")
                    coches1= coches.Coches(cochesito['marca'],cochesito['color'],cochesito['modelo'],cochesito['velocidad'],cochesito['potencia'],cochesito['asientos'])
                    coches1= cochesBD.CochesBD(cochesito['marca'],cochesito['color'],cochesito['modelo'],cochesito['velocidad'],cochesito['potencia'],cochesito['asientos'])
                    respuesta= coches1.insertar()
                    self.respuesta_sql(respuesta)
                    del coches1
                case "2":
                    self.borrarPantalla()
                    id = int(input("Ingrese el ID del coche a actualizar: ").strip())
                    coches1=cochesBD.CochesBD('','','',0,0,0)
                    respuesta=coches1.eliminar(id)
                    self.respuesta_sql(respuesta)
                    del coches1
                case "3":
                    self.borrarPantalla()
                    id= input("Ingrese el ID del coche a actualizar: ").strip()
                    cochesito=self.datos_coches(id)
                    coches1 = cochesBD.CochesBD(
                        cochesito['marca'],
                        cochesito['color'],
                        cochesito['modelo'],
                        cochesito['velocidad'],
                        cochesito['potencia'],
                        cochesito['asientos']
                    )
                    respuesta=coches1.actualizar(id)
                    self.respuesta_sql(respuesta)
                    del coches1
                case "4":
                    self.borrarPantalla()
                    coches1=cochesBD.CochesBD('','','',0,0,0)
                    registros=coches1.consultar()
                    
                    num_coche=1
                    if len(registros)>0:
                        for fila in registros:
                            print(f"\n\tCoche numero #: {num_coche}\n\t\tID: {fila[0]},\n\t\tMarca: {fila[1]}\n\t\tColor: {fila[2]}\n\t\tModelo: {fila[3]},\n\t\tVelocidad: {fila[4]},\n\t\tPotencia: {fila[5]}\n\t\tAsientos: {fila[6]}")
                            num_coche+=1
                            self.esperarTecla()
                    else:
                        print("...!No se encontraro informacion en la BD")
                        self.esperarTecla()
                    del coches1
                case "5":
                    opc=False
                case _:
                    self.opcionInvalida()
    def respuesta_sql(self,respuesta):
        if respuesta:
            input("...¡Accion Realizada con Exito!...")
        else:
            input("...¡Esta Accion no pudo realizarse en este momento !...")
            
    def datos_coches(self,tipo):
        self.borrarPantalla()
        print(f"\n\tIngresar los datos del {tipo}")
        cochesito={}
        cochesito['marca']=input("Marca: ").upper().strip()
        cochesito['color']=input("Color: ").upper().strip()
        cochesito['modelo']=input("Modelo: ").upper().strip()
        cochesito['velocidad']=input("Velocidad: ").strip()
        cochesito['potencia']=input("Potencia: ").strip()
        cochesito['asientos']=input("Asientos: ").strip()
        return cochesito
    def main(self):
        opcion=True
        while opcion:
            self.borrarPantalla()
            opcion=input("\n\t\t ::: MENU PRINCIPAL :::\n\t1- Coches\n\t2- Salir\n\tElige una opcion: ").lower().strip()
            match opcion:
                case "1":
                    self.borrarPantalla()
                    self.menu_cocches()

                case "2":
                    self.borrarPantalla()
                    self.terminarSistema()
                    opcion=False
                case _:
                    self.opcionInvalida()
if __name__=="__main__":
    app=App()
