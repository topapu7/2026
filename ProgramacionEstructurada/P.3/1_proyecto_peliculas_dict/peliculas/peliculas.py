import funciones

def menuPrincipal():
    print("\n\t\t\t...::: M E N U   P R I N C I P A L :::... \n")
    opcion = input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Buscar \n\t 6.- Limpiar \n\t 7.- Salir \n \t\tElige una Opcion: ").strip()
    return opcion

def agregarPeliculas(pelis):
    print("\n\t\t\t...::: AGREGAR PELICULAS :::... \n")
    peli = input("Escribir el nombre de la pelicula: ").upper().strip()
    
    
    if peli not in pelis:
        pelis[peli] = {}

    continuar = "si"
    while continuar == "si":
        caracteristica = input("¿Qué característica deseas agregar? (Ej. GENERO, AÑO, DIRECTOR): ").upper().strip()
        valor = input(f"Escribe el valor para {caracteristica}: ").upper().strip()
        

        pelis[peli][caracteristica] = valor
        

        continuar = input("\n¿Deseas agregar otra característica a esta película? (Si/No): ").lower().strip()
        while continuar != "si" and continuar != "no":
            continuar = input("Por favor, responde 'Si' o 'No': ").lower().strip()
            
    funciones.accionExitosa()
    
def mostrarPeliculas(pelis):
    print("\n\t\t\t...::: MOSTRAR PELICULAS Y DETALLES :::... \n")
    if len(pelis) > 0:
        for peli, caracteristicas in pelis.items():
            print(f"\nPelícula: {peli}")
            if len(caracteristicas) > 0:
                for carac, val in caracteristicas.items():
                    print(f"  -> {carac}: {val}")
            else:
                print("  (Sin características registradas)")
    else:
        print("... ¡No hay peliculas que Mostrar, verifique! ... ")
    funciones.esperarTecla()
    
def limpiarPeliculas(pelis):
    print("\n\t\t\t...::: BORRAR TODAS LAS PELICULAS :::... \n")
    opc = ""
    while opc != "si" and opc != "no":
        opc = input("¿Estas seguro que deseas borrar TODAS las películas y sus datos? (Si/No): ").lower().strip()
    if opc == "si":
        pelis.clear()
        funciones.accionExitosa()

def buscarPeliculas(pelis):
    print("\n\t\t\t...::: BUSCAR PELICULA :::... \n")
    peli = input("Escribe la pelicula a buscar: ").upper().strip()

    if peli in pelis:
        print(f"\nPelícula encontrada: {peli}")
        if len(pelis[peli]) > 0:
            for carac, val in pelis[peli].items():
                print(f"  -> {carac}: {val}")
        else:
            print("  (Esta película no tiene características registradas aún)")
        funciones.esperarTecla()
    else:
        input("\n\t... ¡No existe la pelicula a buscar, verifique! ...")

def borrarPeliculas(pelis):
    print("\n\t\t\t...::: BORRAR PELICULA :::... \n")
    peli = input("Escribe la pelicula a eliminar: ").upper().strip()
    
    if peli in pelis:
        opc = ""
        while opc != "si" and opc != "no":
            opc = input(f"¿Estas seguro que deseas borrar la pelicula '{peli}' y todos sus datos? (Si/No): ").lower().strip()
        if opc == "si":
            pelis.pop(peli)
            funciones.accionExitosa()
    else:
        input("\n\t... ¡No existe la pelicula a borrar, verifique! ...")
            
def modificarPeliculas(pelis):
    print("\n\t\t\t...::: MODIFICAR CARACTERISTICAS :::... \n")
    peli = input("Escribe la pelicula a modificar: ").upper().strip()
    
    if peli in pelis:
        print(f"\nDatos actuales de {peli}:")
        for carac, val in pelis[peli].items():
            print(f"  - {carac}: {val}")
            
        caracteristica = input("\n¿Qué característica deseas modificar o agregar?: ").upper().strip()
        nuevo_valor = input(f"Escribe el nuevo valor para {caracteristica}: ").upper().strip()
        
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Estas seguro que deseas guardar los cambios (Si/No)? ").lower().strip()
            
        if opc == "si":
            pelis[peli][caracteristica] = nuevo_valor
            funciones.accionExitosa()
    else:
        input("\n\t... ¡No existe la película, verifique! ...")