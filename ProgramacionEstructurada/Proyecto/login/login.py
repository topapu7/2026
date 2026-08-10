import re
import funciones
from login import crud

def menu_login():
    print("╔" + "═"*58 + "╗")
    print("║" + " "*17 + "🎮  ACCESO AL SISTEMA  🎮" + " "*17 + "║")
    print("╠" + "═"*58 + "╣")
    print("║   [ 1 ] ⚡ Iniciar Sesión                                ║")
    print("║   [ 2 ] 📝 Registrarse                                  ║")
    print("║   [ 3 ] 🚪 Salir                                         ║")
    print("╚" + "═"*58 + "╝")
    return input("\n\t [ 🕹️ ] Elige una opción: ").strip()

def validar_formato_correo(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, correo) is not None

def iniciar_sesion(conexionBD):
    contador_intentos = 0
    
    while contador_intentos < funciones.MAX_INTENTOS_LOGIN:
        intento_actual = contador_intentos + 1
        intentos_restantes = funciones.MAX_INTENTOS_LOGIN - intento_actual
        
        print("\n" + "═"*50)
        print(f"   🔑  INICIO DE SESIÓN (Intento {intento_actual} de {funciones.MAX_INTENTOS_LOGIN})")
        print("═"*50)
        usuario = input(" ► Usuario: ").strip()
        password = input(" ► Contraseña: ").strip()
        
        if crud.validar_usuario(usuario, password, conexionBD):
            funciones.accionExitosa("¡Inicio de sesión exitoso! Bienvenido")
            return True
        else:
            contador_intentos += 1
            if intentos_restantes > 0:
                print(f"\n   [ ⚠️ ] Credenciales incorrectas. Te quedan {intentos_restantes} intento(s).")
            else:
                funciones.accionNoExitosa("Ha superado el número máximo de intentos permitidos")
    return False

def registrar_usuario(conexionBD):
    print("\n" + "═"*50)
    print("   📝  REGISTRO DE NUEVO USUARIO")
    print("═"*50)
    
    usuario = input(" ► Ingresa nombre de usuario (mínimo 4 caracteres): ").strip()
    if len(usuario) < 4:
        funciones.accionNoExitosa("El nombre de usuario debe contener al menos 4 caracteres")
        return
        
    password = input(" ► Ingresa contraseña (mínimo 4 caracteres): ").strip()
    if len(password) < 4:
        funciones.accionNoExitosa("La contraseña debe contener al menos 4 caracteres")
        return
        
    correo = input(" ► Ingresa correo electrónico (ej. usuario@dominio.com): ").strip()
    if not validar_formato_correo(correo):
        funciones.accionNoExitosa("El correo electrónico no tiene un formato válido")
        return
    
    exito, mensaje = crud.registrar_usuario(usuario, password, correo, conexionBD)
    if exito:
        funciones.accionExitosa(mensaje)
    else:
        funciones.accionNoExitosa(mensaje)

def modulo_login(conexionBD):
    acceso_concedido = False
    opc = ""
    while opc != "3" and not acceso_concedido:
        funciones.borrarPantalla()
        opc = menu_login()
        funciones.borrarPantalla()
        
        match opc:
            case "1": acceso_concedido = iniciar_sesion(conexionBD)
            case "2": registrar_usuario(conexionBD)
            case "3":
                funciones.terminar()
                break
            case _: funciones.opcionInvalida()
                
    return acceso_concedido