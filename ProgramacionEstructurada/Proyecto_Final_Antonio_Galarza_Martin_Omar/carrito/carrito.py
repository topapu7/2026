import funciones
from carrito import crud

def menuCarrito():
    print("╔" + "═"*58 + "╗")
    print("║" + " "*16 + "🛒  CARRITO DE COMPRAS  🛒" + " "*16 + "║")
    print("╠" + "═"*58 + "╣")
    print("║   [ 1 ] ➕ Agregar Videojuego                           ║")
    print("║   [ 2 ] ❌ Borrar Videojuego                            ║")
    print("║   [ 3 ] ✏️  Modificar Videojuego                         ║")
    print("║   [ 4 ] 📋 Mostrar Carrito                              ║")
    print("║   [ 5 ] 🔍 Buscar Videojuego                            ║")
    print("║   [ 6 ] 🧾 Generar Ticket de Compra (.txt)              ║")
    print("║   [ 7 ] 💳 Realizar Compra (Individual / Todos)          ║")
    print("║   [ 8 ] 🗑️  Vaciar Carrito                              ║")
    print("║   [ 9 ] ↩️  Regresar al Menú Principal                  ║")
    print("╚" + "═"*58 + "╝")
    return input("\n\t [ 🕹️ ] Elige una opción: ").strip()

def procesarCompra(conexionBD):
    print("\n" + "═"*50)
    print("   💳  MÓDULO DE COMPRAS")
    print("═"*50)
    juegos = crud.consultar(conexionBD)
    
    if len(juegos) == 0:
        funciones.accionNoExitosa("El carrito está vacío. No hay videojuegos para comprar")
        return

    print(" 1.- Comprar UN juego individual")
    print(" 2.- Comprar TODOS los juegos del carrito")
    opcion = input("\n ► Elige el tipo de compra (1 o 2): ").strip()

    if opcion == "1":
        nombre = input(" ► Nombre del videojuego a comprar: ").upper().strip()
        juego = crud.obtener_por_nombre(nombre, conexionBD)
        
        if juego is not None:
            precio = float(juego[2])
            descuento = precio * funciones.DESCUENTO_GAAMER
            subtotal = precio - descuento
            total = subtotal * (1 + funciones.IVA)
            
            print(f"\n   Resumen de Compra para '{juego[1]}':")
            print(f"   ----------------------------------")
            print(f"   Precio original: ${precio:.2f}")
            print(f"   Descuento (10%): -${descuento:.2f}")
            print(f"   IVA (16%):        +${(subtotal * funciones.IVA):.2f}")
            print(f"   TOTAL A PAGAR:    ${total:.2f}")
            
            confirmar = input("\n ¿Confirmar pago? (Si/No): ").lower().strip()
            if confirmar == "si":
                crud.eliminar(juego[1], conexionBD)
                funciones.accionExitosa(f"¡Compra realizada con éxito! Se procesaron ${total:.2f}")
        else:
            funciones.accionNoExitosa(f"No se encontró '{nombre}' en el carrito")

    elif opcion == "2":
        subtotal_acumulado = sum(float(j[2]) for j in juegos)
        descuento = subtotal_acumulado * funciones.DESCUENTO_GAAMER
        monto_con_desc = subtotal_acumulado - descuento
        total = monto_con_desc * (1 + funciones.IVA)
        
        print(f"\n   Resumen de Compra de TODO el Carrito ({len(juegos)} juegos):")
        print(f"   ----------------------------------")
        print(f"   Subtotal:        ${subtotal_acumulado:.2f}")
        print(f"   Descuento (10%): -${descuento:.2f}")
        print(f"   IVA (16%):        +${(monto_con_desc * funciones.IVA):.2f}")
        print(f"   TOTAL A PAGAR:    ${total:.2f}")
        
        confirmar = input("\n ¿Confirmar pago de todos los ítems? (Si/No): ").lower().strip()
        if confirmar == "si":
            crud.vaciar(conexionBD)
            funciones.accionExitosa(f"¡Compra total realizada con éxito! Se pagaron ${total:.2f}")
    else:
        funciones.opcionInvalida()

def agregarJuego(conexionBD):
    print("\n" + "═"*50)
    print("   ➕  AGREGAR AL CARRITO")
    print("═"*50)
    opc = "SI"
    while opc == "SI":
        nombre = input(" ► Nombre del videojuego: ").upper().strip()
        if not nombre:
            funciones.accionNoExitosa("El nombre no puede estar vacío")
            return

        try:
            precio = float(input(" ► Precio ($): "))
            if precio <= 0:
                funciones.accionNoExitosa("El precio debe ser mayor a 0")
                return
        except ValueError:
            funciones.accionNoExitosa("El precio debe ser un número válido")
            return

        plataforma = input(" ► Plataforma (ej. PC, PS5, Xbox): ").upper().strip()
        clasificacion = input(" ► Clasificación (ej. E, T, M): ").upper().strip()
        
        exito, mensaje = crud.insertar(nombre, precio, plataforma, clasificacion, conexionBD)
        if exito: funciones.accionExitosa(mensaje)
        else: funciones.accionNoExitosa(mensaje)
            
        opc = input("\n ¿Deseas agregar otro juego? (Si/No): ").upper().strip()

def mostrarCarrito(conexionBD):
    print("\n" + "═"*85)
    print("   🛒  CONTENIDO DEL CARRITO DE COMPRAS")
    print("═"*85)
    juegos = crud.consultar(conexionBD)
    
    contador_juegos = 0
    subtotal_acumulado = 0.0
    lista_diccionarios = []

    if len(juegos) > 0:
        print(f" {'ID':<5} | {'Nombre':<30} | {'Precio':<10} | {'Plataforma':<15} | {'Clasificación':<15}")
        print("─" * 85)
        for j in juegos:
            contador_juegos += 1
            precio_float = float(j[2])
            subtotal_acumulado += precio_float
            
            dict_juego = {"id": j[0], "nombre": j[1], "precio": precio_float, "plataforma": j[3], "clasificacion": j[4]}
            lista_diccionarios.append(dict_juego)
            print(f" {dict_juego['id']:<5} | {dict_juego['nombre']:<30} | ${dict_juego['precio']:<9.2f} | {dict_juego['plataforma']:<15} | {dict_juego['clasificacion']:<15}")
            
        descuento_aplicado = subtotal_acumulado * funciones.DESCUENTO_GAAMER
        monto_con_descuento = subtotal_acumulado - descuento_aplicado
        monto_iva = monto_con_descuento * funciones.IVA
        total_pagar = (subtotal_acumulado - descuento_aplicado) + monto_iva
        promedio_precio = subtotal_acumulado / contador_juegos if contador_juegos > 0 else 0

        print("─" * 85)
        print(f" Total de items: {contador_juegos} | Precio Promedio: ${promedio_precio:.2f}")
        print(f" Subtotal: ${subtotal_acumulado:.2f} | Descuento (10%): -${descuento_aplicado:.2f} | IVA (16%): +${monto_iva:.2f}")
        print(f" 💵 TOTAL A PAGAR: ${total_pagar:.2f}")
    else:
        print("   [ ℹ️ ] El carrito está vacío actualmente.")
    funciones.esperarTecla()

def generarTicketTXT(conexionBD):
    print("\n" + "═"*50)
    print("   🧾  GENERAR TICKET DE COMPRA (.TXT)")
    print("═"*50)
    juegos = crud.consultar(conexionBD)
    
    if len(juegos) == 0:
        funciones.accionNoExitosa("El carrito está vacío. No hay productos para facturar")
        return

    contador_juegos = 0
    subtotal = 0.0
    
    try:
        with open("ticket_compra.txt", "w", encoding="utf-8") as archivo:
            archivo.write("====================================================\n")
            archivo.write("          🎮 TIENDA DE VIDEOJUEGOS - TICKET 🎮       \n")
            archivo.write("====================================================\n\n")
            archivo.write(f"{'Cant.':<6} | {'Videojuego':<25} | {'Precio Unitario':<12}\n")
            archivo.write("-" * 52 + "\n")
            
            for j in juegos:
                item = {"nombre": j[1], "precio": float(j[2])}
                contador_juegos += 1
                subtotal += item["precio"]
                archivo.write(f"{1:<6} | {item['nombre']:<25} | ${item['precio']:<11.2f}\n")
            
            descuento = subtotal * funciones.DESCUENTO_GAAMER
            sub_descuento = subtotal - descuento
            calculo_iva = sub_descuento * funciones.IVA
            total_final = (subtotal - (subtotal * funciones.DESCUENTO_GAAMER)) * (1 + funciones.IVA)
            
            archivo.write("-" * 52 + "\n")
            archivo.write(f"Total de Artículos: {contador_juegos}\n")
            archivo.write(f"Subtotal:           ${subtotal:.2f}\n")
            archivo.write(f"Descuento (10%):   -${descuento:.2f}\n")
            archivo.write(f"IVA (16%):          +${calculo_iva:.2f}\n")
            archivo.write(f"TOTAL FINAL:        ${total_final:.2f}\n")
            archivo.write("====================================================\n")
            archivo.write("        ¡Gracias por tu compra gamer! 🕹️            \n")
            
        funciones.accionExitosa("Se ha generado el archivo 'ticket_compra.txt' con éxito")
    except Exception as e:
        funciones.accionNoExitosa(f"Fallo al escribir el archivo TXT: {e}")

def borrarJuego(conexionBD):
    print("\n" + "═"*50)
    print("   ❌  BORRAR DEL CARRITO")
    print("═"*50)
    nombre = input(" ► Nombre del videojuego a borrar: ").upper().strip()
    if input(f" ¿Confirmas borrar '{nombre}'? (Si/No): ").lower().strip() == "si":
        exito, mensaje = crud.eliminar(nombre, conexionBD)
        if exito: funciones.accionExitosa(mensaje)
        else: funciones.accionNoExitosa(mensaje)

def modificarJuego(conexionBD):
    print("\n" + "═"*50)
    print("   ✏️  MODIFICAR EN CARRITO")
    print("═"*50)
    nombre_viejo = input(" ► Nombre del videojuego a modificar: ").upper().strip()
    if input(f" ¿Confirmas modificar '{nombre_viejo}'? (Si/No): ").lower().strip() == "si":
        nuevo_nombre = input(" ► Nuevo nombre: ").upper().strip()
        try:
            nuevo_precio = float(input(" ► Nuevo precio ($): "))
            if nuevo_precio <= 0:
                funciones.accionNoExitosa("El precio debe ser mayor a 0")
                return
        except ValueError:
            funciones.accionNoExitosa("El precio debe ser un número válido")
            return
            
        nueva_plataforma = input(" ► Nueva plataforma: ").upper().strip()
        nueva_clasificacion = input(" ► Nueva clasificación: ").upper().strip()
        
        exito, mensaje = crud.actualizar(nombre_viejo, nuevo_nombre, nuevo_precio, nueva_plataforma, nueva_clasificacion, conexionBD)
        if exito: funciones.accionExitosa(mensaje)
        else: funciones.accionNoExitosa(mensaje)

def buscarJuego(conexionBD):
    print("\n" + "═"*85)
    print("   🔍  BUSCAR EN CARRITO")
    print("═"*85)
    nombre = input(" ► Nombre a buscar: ").upper().strip()
    juegos = crud.buscar(nombre, conexionBD)
    if len(juegos) > 0:
        print(f" {'ID':<5} | {'Nombre':<30} | {'Precio':<10} | {'Plataforma':<15} | {'Clasificación':<15}")
        print("─" * 85)
        for j in juegos:
            print(f" {j[0]:<5} | {j[1]:<30} | ${float(j[2]):<9.2f} | {j[3]:<15} | {j[4]:<15}")
    else:
        print(f"\n   [ ℹ️ ] No se encontró coincidencia para '{nombre}'.")
    funciones.esperarTecla()

def limpiarCarrito(conexionBD):
    print("\n" + "═"*50)
    print("   🗑️  VACIAR CARRITO")
    print("═"*50)
    if input(" ⚠️ ¿Confirmas eliminar TODO? (Si/No): ").lower().strip() == "si":
        exito, mensaje = crud.vaciar(conexionBD)
        if exito: funciones.accionExitosa(mensaje)
        else: funciones.accionNoExitosa(mensaje)

def gestionar_carrito(conexionBD):
    opc = ""
    while opc != "9":
        funciones.borrarPantalla()
        opc = menuCarrito()
        funciones.borrarPantalla()
        match opc:
            case "1": agregarJuego(conexionBD)
            case "2": borrarJuego(conexionBD)
            case "3": modificarJuego(conexionBD)
            case "4": mostrarCarrito(conexionBD)
            case "5": buscarJuego(conexionBD)
            case "6": generarTicketTXT(conexionBD)
            case "7": procesarCompra(conexionBD)
            case "8": limpiarCarrito(conexionBD)
            case "9": break
            case _: funciones.opcionInvalida()