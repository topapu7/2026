from coches import coches
from tkinter import *
from tkinter import messagebox
print("\033c")

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestion de Coches")
        self.ventana.geometry("800x600")
        self.ventana.resizable(0,0)
        self.main()

    ## ...Vistas   
    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def terminarSistema(self):
        input("....:::: GRACIAS POR UTILIZAR NUESTRO SISTEMA, \n  vuelve pronto ::::...")

    def opcionInvalida(self):
        input("\n\t.... ¡Opcion invalidad, vuelve a intentarlo!.... ") 
        
    def menu_acciones(self):
        self.borrarPantalla()
        tipo="Coches"
        Label(self.ventana,text=f"\t\t....:::: Menu de {tipo} ::::...\n")
        Button(self.ventana,text="1.-Agregar",command="").pack(pady=5)
        Button(self.ventana,text="2.-Borrar",command="").pack(pady=5)
        Button(self.ventana,text="3.-Modificar",command="").pack(pady=5)
        Button(self.ventana,text="4.-Mostrar",command="").pack(pady=5)
        Button(self.ventana,text="5.-Regresar",command=self.main).pack(pady=5)

    def main(self):
        self.borrarPantalla()
        Label(self.ventana, text="\n...::: M E N U  P R I N C I P A L :::...").pack(pady=10)
        Button(self.ventana,text="1.- Coches", command=self.menu_acciones).pack(pady=5)
        Button(self.ventana,text="2.- Salir", command=self.ventana.quit).pack(pady=5)

    ## ...Controlador    
    def menu_cocches(self):
        opc =True
        while opc:
            self.borrarPantalla()
            opc=self.menu_acciones("Coches")
            match opc:
                case "1":
                    ##solicitar datos y crear objeto de Coches
                    cochesito= self.datos_coches("Coches")
                    coches1= coches.Coches(cochesito['marca'],cochesito['color'],cochesito['modelo'],cochesito['velocidad'],cochesito['potencia'],cochesito['asientos'])
                    respuesta= coches1.insertar()
                    self.respuesta_sql(respuesta)
                    ##borrar objeto que no utilizas
                    del coches1
                case "2":
                    self.borrarPantalla()
                    # En lugar de solo .strip(), conviértelo a entero int()
                    id = int(input("Ingrese el ID del coche a eliminar: ").strip())
                    respuesta=coches.Coches.eliminar(id)
                    self.respuesta_sql(respuesta)
                case "3":
                    self.borrarPantalla()
                    id= input("Ingrese el ID del coche a actualizar: ").strip()
                    cochesito=self.datos_coches(id)
                    coches1 = coches.Coches(
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
                    registros=coches.Coches.consultar()
                    
                    num_coche=1
                    if len(registros)>0:
                        for fila in registros:
                            print(f"\n\tCoche numero #: {num_coche}\n\t\tID: {fila[0]},\n\t\tMarca: {fila[1]}\n\t\tColor: {fila[2]}\n\t\tModelo: {fila[3]},\n\t\tVelocidad: {fila[4]},\n\t\tPotencia: {fila[5]}\n\t\tAsientos: {fila[6]}")
                            num_coche+=1
                            self.esperarTecla()
                    else:
                        print("...!No se encontraro informacion en la BD")
                        self.esperarTecla()

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


if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()