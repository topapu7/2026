from estudiantes import estudiantes
from tkinter import *
from tkinter import messagebox

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestion de estudiantes")
        self.ventana.geometry("600x600")
        self.ventana.resizable(0,0)
        self.main()

    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()
        

    def menu_acciones(self):
        self.borrarPantalla()
        self.tipo = "Estudiantes"
        Label(self.ventana, text= f"...::: Menu de {self.tipo} :::...").pack(pady=5)
        Button(self.ventana, text="1.- Agregar", command=self.insertar_view).pack(pady=10)
        Button(self.ventana, text="2.- Borrar", command=self.eliminar_view).pack(pady=10)
        Button(self.ventana, text="3.- Modificar", command=self.modificar_view).pack(pady=10)
        Button(self.ventana, text="4.- Mostrar", command=self.consultar_view).pack(pady=10)
        Button(self.ventana, text="5.- Regresar", command=self.main).pack(pady=10)     

    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(title="... Exitoso ...", message= "✅ ¡Accion Realizada con Exito! ✅")
        else:
            messagebox.showerror(title="... ¡ Verifica por favor ! ...", message="❌ ¡Opcion invalida! Oprima cualquier tecla para continuar... ❌")


    def main(self):
        self.borrarPantalla()
        Label(self.ventana, text="\n...:: M E N U  P R I N C I P A L ::...").pack(pady=10)
        Button(self.ventana, text="1.- Estudiantes", command=self.menu_acciones).pack(pady=5)
        Button(self.ventana, text="2.- Salir", command=self.ventana.quit).pack(pady=10)

    def insertar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...Ingresar los datos del coche...").pack(pady=10)

        Label(self.ventana, text="Nombre: ").pack(pady=10)
        self.nombre = Entry(self.ventana)
        self.nombre.focus()
        self.nombre.pack(pady=5)
        Label(self.ventana, text="Nota: ").pack(pady=10)
        self.nota = Entry(self.ventana)
        self.nota.pack(pady=5)
        Button(self.ventana, text="Guardar", command=self.insertar_controller).pack(pady=5)
        Button(self.ventana, text= "Regresar", command=self.menu_acciones).pack(pady=5)

    def eliminar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...Ingresar el ID del estudiante a eliminar...").pack(pady=10)
        Label(self.ventana, text="ID: ").pack(pady=10)
        self.id = Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)

        Button(self.ventana, text= "Eliminar", command=self.eliminar_controller).pack(pady=5)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=5)

    def modificar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...Ingresar el ID del estudiante a modificar...").pack(pady=10)

        Label(self.ventana, text="ID: ").pack(pady=10)
        self.id = Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)

        Label(self.ventana, text="Nuevo nombre: ").pack(pady=10)
        self.nombre = Entry(self.ventana)
        self.nombre.pack(pady=5)

        Label(self.ventana, text="Nueva nota: ").pack(pady=10)
        self.nota = Entry(self.ventana)
        self.nota.pack(pady=5)

        Button(self.ventana, text="Guardar", command=self.modificar_controller).pack(pady=5)
        Button(self.ventana, text= "Regresar", command=self.menu_acciones).pack(pady=5)

    def consultar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...::Consultar los estudiantes::...").pack(pady=10)
        filas=""
        filas=self.consultar_controller(filas)
        Label(self.ventana, text=f"{'NO.':<20}{'ID':<20}{'Nombre':<20}{'Nota':<20}").pack(pady=5, padx=10)
        Label(self.ventana, text=f"-"*100).pack(pady=10)
        Label(self.ventana, text=f"{filas}").pack(pady=10)
        Button(self.ventana, text="Regresar", command=self.menu_acciones).pack(pady=5)

#------------------- Controler ------------------------------

    def insertar_controller(self):
        estudiante1 = estudiantes.Estudiantes(self.nombre.get(), self.nota.get())                    
        respuesta = estudiante1.insertar()
        self.respuesta_sql(respuesta)
        del estudiante1
        self.borrarPantalla()
        self.insertar_view()

    def eliminar_controller(self):
        id=self.id.get()
        respuesta = estudiantes.Estudiantes.eliminar(id)
        self.respuesta_sql(respuesta)
        self.borrarPantalla()
        self.eliminar_view()

    def modificar_controller(self):
        id=self.id.get()                     
        estudiante1 = estudiantes.Estudiantes(self.nombre.get(), self.nota.get())
        respuesta = estudiante1.actualizar(id)
        self.respuesta_sql(respuesta)
        del estudiante1
        self.borrarPantalla()
        self.modificar_view()

    def consultar_controller(self, filas):
        registros=estudiantes.Estudiantes.consultar()
        if len(registros) > 0:
            numero_estudiantes=1
            for fila in registros:
                #Se va a concatenar con el + 
                filas=filas + f"{numero_estudiantes:<20}{fila[0]:<20}{fila[1]:<20}{fila[2]:20}\n"
                numero_estudiantes += 1
        else:
            filas = "... ¡No existe datos que mostrar por el momento! ..."
        return filas

    

if __name__=="__main__":
    ventana = Tk()
    app=App(ventana)
    ventana.mainloop()
    
#Carpetas
#Vista 
#controlador
#Modelo