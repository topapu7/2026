import funciones
from lista_deseados import crud
from carrito import crud as crud_carrito

def menuDeseados():
    print("╔" + "═"*58 + "╗")
    print("║" + " "*17 + "⭐  LISTA DE DESEOS  ⭐" + " "*18 + "║")
    print("╠" + "═"*58 + "╣")
    print("║   [ 1 ] ➕ Agregar a Deseos                             ║")
    print("║   [ 2 ] ❌ Borrar de Deseos                             ║")
    print("║   [ 3 ] ✏️  Modificar en Deseos                          ║")
    print("║   [ 4 ] 📋 Mostrar Lista                                ║")
    print("║   [ 5 ] 🔍 Buscar en Lista                              ║")
    print("║   [ 6 ] 🗑️  Vaciar Lista                                 ║")
    print("║   [ 7 ] 🛒 Mover Videojuego al Carrito                  ║")
    print("║   [ 8 ] ↩️  Regresar al Menú Principal                  ║")
    print("╚" + "═"*58 + "╝")
    return input("\n\t [ 🕹️ ] Elige una opción: ").strip()

def moverAlCarrito(conexionBD):
    print("\n" + "═"*50)
    print("   🛒  MOVER DE LISTA DE DESEOS AL CARRITO")
    print("═"*50)
    nombre = input(" ► Nombre del juego a mover al carrito: ").upper().strip()
    
    juego = crud.obtener_por_nombre(nombre, conexionBD)
    if juego is not None:
        # Extraer datos: (id, nombre, plataforma, clasificacion, req, precio)
        nombre_juego = juego[1]
        plataforma = juego[2]
        clasificacion = juego[3]
        precio = juego[5]
        
        # 1. Insertar en tabla del carrito
        exito_ins, msj_ins = crud_carrito.insertar(nombre_juego, precio, plataforma, clasificacion, conexionBD)
        
        if exito_ins:
            # 2. Borrar de lista de deseos
            crud.eliminar(nombre_juego, conexionBD)
            funciones.accionExitosa(f"'{nombre_juego}' se movió con éxito al Carrito de Compras")
        else:
            funciones.accionNoExitosa(f"No se pudo transferir: {msj_ins}")
    else:
        funciones.accionNoExitosa(f"No se encontró '{nombre}' en tu Lista de Deseos")

def agregarDeseado(conexionBD):
    print("\n" + "═"*50)
    print("   ⭐  AGREGAR A LISTA DE DESEOS")
    print("═"*50)
    opc = "SI"
    while opc == "SI":
        nombre = input(" ► Nombre del videojuego: ").upper().strip()
        if not nombre:
            funciones.accionNoExitosa("El nombre no puede estar vacío")
            return

        plataforma = input(" ► Plataforma (ej. PC, PS5, Xbox): ").upper().strip()
        clasificacion = input(" ► Clasificación (ej. E, T, M): ").upper().strip()
        requerimientos = input(" ► Requerimientos del sistema: ").strip()
        
        try:
            precio = float(input(" ► Precio estimado ($): "))
            if precio <= 0:
                funciones.accionNoExitosa("El precio debe ser mayor a 0")
                return
        except ValueError:
            funciones.accionNoExitosa("El precio debe ser un número válido")
            return
        
        exito, mensaje = crud.insertar(nombre, plataforma, clasificacion, requerimientos, precio, conexionBD)
        if exito: funciones.accionExitosa(mensaje)
        else: funciones.accionNoExitosa(mensaje)
            
        opc = input("\n ¿Deseas agregar otro videojuego? (Si/No): ").upper().strip()

def mostrarDeseados(conexionBD):
    print("\n" + "═"*100)
    print("   ⭐  CONTENIDO DE LA LISTA DE DESEOS")
    print("═"*100)
    juegos = crud.consultar(conexionBD)
    if len(juegos) > 0:
        print(f" {'ID':<5} | {'Nombre':<25} | {'Plataforma':<12} | {'Clasif.':<8} | {'Precio':<10} | {'Requerimientos':<25}")
        print("─" * 100)
        for j in juegos:
            print(f" {j[0]:<5} | {j[1]:<25} | {j[2]:<12} | {j[3]:<8} | ${j[5]:<9.2f} | {j[4]:<25}")
    else:
        print("   [ ℹ️ ] La lista de deseos está vacía.")
    funciones.esperarTecla()

def borrarDeseado(conexionBD):
    print("\n" + "═"*50)
    print("   ❌  BORRAR DE DESEOS")
    print("═"*50)
    nombre = input(" ► Nombre del juego a borrar: ").upper().strip()
    if input(f" ¿Confirmas borrar '{nombre}'? (Si/No): ").lower().strip() == "si":
        exito, mensaje = crud.eliminar(nombre, conexionBD)
        if exito: funciones.accionExitosa(mensaje)
        else: funciones.accionNoExitosa(mensaje)

def modificarDeseado(conexionBD):
    print("\n" + "═"*50)
    print("   ✏️  MODIFICAR EN DESEOS")
    print("═"*50)
    nombre_viejo = input(" ► Nombre del juego a modificar: ").upper().strip()
    if input(f" ¿Confirmas modificar '{nombre_viejo}'? (Si/No): ").lower().strip() == "si":
        nuevo_nombre = input(" ► Nuevo nombre: ").upper().strip()
        nueva_plataforma = input(" ► Nueva plataforma: ").upper().strip()
        nueva_clasificacion = input(" ► Nueva clasificación: ").upper().strip()
        nuevos_req = input(" ► Nuevos requerimientos: ").strip()
        try:
            nuevo_precio = float(input(" ► Nuevo precio ($): "))
            if nuevo_precio <= 0:
                funciones.accionNoExitosa("El precio debe ser mayor a 0")
                return
        except ValueError:
            funciones.accionNoExitosa("El precio debe ser un número válido")
            return
            
        exito, mensaje = crud.actualizar(nombre_viejo, nuevo_nombre, nueva_plataforma, nueva_clasificacion, nuevos_req, nuevo_precio, conexionBD)
        if exito: funciones.accionExitosa(mensaje)
        else: funciones.accionNoExitosa(mensaje)

def buscarDeseado(conexionBD):
    print("\n" + "═"*100)
    print("   🔍  BUSCAR EN DESEOS")
    print("═"*100)
    nombre = input(" ► Nombre o palabra clave a buscar: ").upper().strip()
    juegos = crud.buscar(nombre, conexionBD)
    if len(juegos) > 0:
        print(f" {'ID':<5} | {'Nombre':<25} | {'Plataforma':<12} | {'Clasif.':<8} | {'Precio':<10} | {'Requerimientos':<25}")
        print("─" * 100)
        for j in juegos:
            print(f" {j[0]:<5} | {j[1]:<25} | {j[2]:<12} | {j[3]:<8} | ${j[5]:<9.2f} | {j[4]:<25}")
    else:
        print(f"\n   [ ℹ️ ] No se encontró '{nombre}' en la lista de deseos.")
    funciones.esperarTecla()

def limpiarDeseados(conexionBD):
    print("\n" + "═"*50)
    print("   🗑️  VACIAR LISTA DE DESEOS")
    print("═"*50)
    if input(" ⚠️ ¿Confirmas vaciar TODA tu lista de deseos? (Si/No): ").lower().strip() == "si":
        exito, mensaje = crud.vaciar(conexionBD)
        if exito: funciones.accionExitosa(mensaje)
        else: funciones.accionNoExitosa(mensaje)

def gestionar_deseados(conexionBD):
    opc = ""
    while opc != "8":
        funciones.borrarPantalla()
        opc = menuDeseados()
        funciones.borrarPantalla()
        match opc:
            case "1": agregarDeseado(conexionBD)
            case "2": borrarDeseado(conexionBD)
            case "3": modificarDeseado(conexionBD)
            case "4": mostrarDeseados(conexionBD)
            case "5": buscarDeseado(conexionBD)
            case "6": limpiarDeseados(conexionBD)
            case "7": moverAlCarrito(conexionBD)
            case "8": break
            case _: funciones.opcionInvalida()