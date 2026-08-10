import mysql.connector

def obtener_por_nombre(nombre, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            sql = "SELECT * FROM lista_deseados WHERE nombre = %s"
            cursor.execute(sql, (nombre,))
            return cursor.fetchone()
        return None
    except mysql.connector.Error:
        return None

def insertar(nombre, plataforma, clasificacion, requerimientos, precio, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            sql = """INSERT INTO lista_deseados (nombre, plataforma, clasificacion, requerimientos, precio) 
                     VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (nombre, plataforma, clasificacion, requerimientos, precio))
            conexionBD.commit()
            return True, "Videojuego agregado a la Lista de Deseos"
        return False, "Error de conexión con la base de datos"
    except mysql.connector.Error as err:
        return False, f"Error al insertar en MySQL: {err.msg}"

def consultar(conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("SELECT * FROM lista_deseados")
            return cursor.fetchall()
        return []
    except mysql.connector.Error:
        return []

def eliminar(nombre, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("DELETE FROM lista_deseados WHERE nombre = %s", (nombre,))
            filas_borradas = cursor.rowcount
            cursor.execute("ALTER TABLE lista_deseados AUTO_INCREMENT = 1")
            conexionBD.commit()
            if filas_borradas > 0:
                return True, f"'{nombre}' borrado de la Lista de Deseos"
            return False, f"No se encontró el juego '{nombre}'"
        return False, "Error de conexión con la base de datos"
    except mysql.connector.Error as err:
        return False, f"Error al eliminar: {err.msg}"

def actualizar(nombre_viejo, nuevo_nombre, nueva_plataforma, nueva_clasificacion, nuevos_requerimientos, nuevo_precio, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            sql = """UPDATE lista_deseados 
                     SET nombre = %s, plataforma = %s, clasificacion = %s, requerimientos = %s, precio = %s 
                     WHERE nombre = %s"""
            cursor.execute(sql, (nuevo_nombre, nueva_plataforma, nueva_clasificacion, nuevos_requerimientos, nuevo_precio, nombre_viejo))
            conexionBD.commit()
            if cursor.rowcount > 0:
                return True, "Registro en Lista de Deseos actualizado"
            return False, f"No se encontró '{nombre_viejo}' para modificar"
        return False, "Error de conexión con la base de datos"
    except mysql.connector.Error as err:
        return False, f"Error al modificar: {err.msg}"

def buscar(nombre, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            sql = "SELECT * FROM lista_deseados WHERE nombre LIKE %s"
            cursor.execute(sql, (f"%{nombre}%",))
            return cursor.fetchall()
        return []
    except mysql.connector.Error:
        return []

def vaciar(conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("TRUNCATE TABLE lista_deseados")
            return True, "Se ha limpiado la Lista de Deseos"
        return False, "Error de conexión con la base de datos"
    except mysql.connector.Error as err:
        return False, f"Error al vaciar lista: {err.msg}"