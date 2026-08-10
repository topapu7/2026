import mysql.connector

def obtener_por_nombre(nombre, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            sql = "SELECT * FROM carrito WHERE nombre = %s"
            cursor.execute(sql, (nombre,))
            return cursor.fetchone()
        return None
    except mysql.connector.Error:
        return None

def insertar(nombre, precio, plataforma, clasificacion, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            sql = "INSERT INTO carrito (nombre, precio, plataforma, clasificacion) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (nombre, precio, plataforma, clasificacion))
            conexionBD.commit()
            return True, "Videojuego agregado al carrito con éxito"
        return False, "Error de conexión con la base de datos"
    except mysql.connector.Error as err:
        return False, f"Fallo al agregar en MySQL: {err.msg}"

def consultar(conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("SELECT * FROM carrito")
            return cursor.fetchall()
        return []
    except mysql.connector.Error:
        return []

def eliminar(nombre, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("DELETE FROM carrito WHERE nombre = %s", (nombre,))
            filas_borradas = cursor.rowcount
            cursor.execute("ALTER TABLE carrito AUTO_INCREMENT = 1")
            conexionBD.commit()
            if filas_borradas > 0:
                return True, f"'{nombre}' se eliminó del carrito"
            return False, f"No se encontró el juego '{nombre}' en el carrito"
        return False, "Error de conexión con la base de datos"
    except mysql.connector.Error as err:
        return False, f"Error al eliminar: {err.msg}"

def actualizar(nombre_viejo, nuevo_nombre, nuevo_precio, nueva_plataforma, nueva_clasificacion, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            sql = """UPDATE carrito 
                     SET nombre = %s, precio = %s, plataforma = %s, clasificacion = %s 
                     WHERE nombre = %s"""
            cursor.execute(sql, (nuevo_nombre, nuevo_precio, nueva_plataforma, nueva_clasificacion, nombre_viejo))
            conexionBD.commit()
            if cursor.rowcount > 0:
                return True, "Videojuego actualizado correctamente"
            return False, f"No se encontró el juego '{nombre_viejo}' para modificar"
        return False, "Error de conexión con la base de datos"
    except mysql.connector.Error as err:
        return False, f"Error al modificar: {err.msg}"

def buscar(nombre, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            sql = "SELECT * FROM carrito WHERE nombre LIKE %s"
            cursor.execute(sql, (f"%{nombre}%",))
            return cursor.fetchall()
        return []
    except mysql.connector.Error:
        return []

def vaciar(conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("TRUNCATE TABLE carrito")
            return True, "Se ha vaciado el carrito por completo"
        return False, "Error de conexión con la base de datos"
    except mysql.connector.Error as err:
        return False, f"Error al vaciar: {err.msg}"