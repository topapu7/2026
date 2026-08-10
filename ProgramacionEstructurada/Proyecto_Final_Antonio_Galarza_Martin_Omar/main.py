import funciones
from login import login
from carrito import carrito
from lista_deseados import videojuegos

def menuPrincipal():
    print("╔" + "═"*58 + "╗")
    print("║" + " "*14 + "🎮  TIENDA DE VIDEOJUEGOS  🎮" + " "*14 + "║")
    print("╠" + "═"*58 + "╣")
    print("║   [ 1 ] 🛒 Carrito de Compras                            ║")
    print("║   [ 2 ] ⭐ Lista de Deseos                               ║")
    print("║   [ 3 ] 🚪 Salir del Sistema                             ║")
    print("╚" + "═"*58 + "╝")
    return input("\n\t [ 🕹️ ] Elige una opción: ").strip()
conexionBD = funciones.conectar()

if conexionBD is not None:
    if login.modulo_login(conexionBD):
        opc = ""
        while opc != "3":
            funciones.borrarPantalla()
            opc = menuPrincipal()
            
            match opc:
                case "1":
                    carrito.gestionar_carrito(conexionBD)
                case "2":
                    videojuegos.gestionar_deseados(conexionBD)
                case "3":
                    funciones.borrarPantalla()
                    funciones.terminar()
                case _:
                    funciones.opcionInvalida()