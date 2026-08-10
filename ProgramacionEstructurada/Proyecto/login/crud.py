import mysql.connector

def validar_usuario(usuario, password, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            sql = "SELECT * FROM usuarios WHERE usuario = %s AND password = %s"
            cursor.execute(sql, (usuario, password))
            resultado = cursor.fetchone()
            return resultado is not None
        return False
    except mysql.connector.Error:
        return False

def registrar_usuario(usuario, password, correo, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            sql = "INSERT INTO usuarios VALUES (null, %s, %s, %s)"
            cursor.execute(sql, (usuario, password, correo))
            conexionBD.commit()
            return True, "Usuario registrado exitosamente"
        return False, "Error de conexión con la base de datos"
    except mysql.connector.Error as err:
        if err.errno == 1062:
            return False, "El nombre de usuario ya existe en el sistema"
        return False, f"Error en la base de datos: {err.msg}"