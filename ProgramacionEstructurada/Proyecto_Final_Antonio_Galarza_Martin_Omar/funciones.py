import os
import mysql.connector 

# --- CONSTANTES ---
IVA = 0.16
DESCUENTO_GAAMER = 0.10
MAX_INTENTOS_LOGIN = 3
MONEDA_SIMBOLO = "$"

def borrarPantalla():
    print("\033c", end="")
    
def esperarTecla():
    input("\n\t [ 🎮 ] Presiona ENTER para continuar...")
    
def terminar():
    borrarPantalla()
    print("═"*65)
    print("   ★彡 ¡GRACIAS POR UTILIZAR NUESTRA TIENDA DE VIDEOJUEGOS! 彡★")
    print("═"*65)
    input("\n\t [ 🕹️ ] Presiona ENTER para salir...")
    
def opcionInvalida():
    print("\n\t [ ⚠️ ERROR ] ¡Opción inválida! Intenta con un número del menú.")
    esperarTecla()

def accionExitosa(mensaje="Acción realizada con éxito"):
    print(f"\n\t [ ⚡ ÉXITO ] ¡{mensaje}!")
    esperarTecla()

def accionNoExitosa(mensaje="No se pudo completar la acción"):
    print(f"\n\t [ ❌ ERROR ] {mensaje}.")
    esperarTecla()

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_tienda_videojuegos"
        ) 
        return conexion   
    except mysql.connector.Error as err:
        borrarPantalla()
        print("═"*65)
        print(" [ ❌ ERROR DE CONEXIÓN CON LA BASE DE DATOS MySQL ]")
        print("═"*65)
        print(f" Detalle del fallo: {err}")
        print(" Verifica que Apache y MySQL estén activos en XAMPP.")
        esperarTecla()
        return None