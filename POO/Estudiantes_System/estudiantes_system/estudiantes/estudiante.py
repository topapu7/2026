import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexionBD import cursor, conexion

class Estudiantes:
    def __init__(self,nombre,nota):
        self._nombre = nombre
        self._nota = nota
    def getNombre(self):
        return self._nombre 
    def setNombre(self,nombre):
        self._nombre=nombre
        
    def getNota(self):
        return self._nota
    def setNota(self,nota):
        self._nota = nota
        
    def insertar (self):
        try:
            cursor.execute("insert into estudiantes values (null,%s,%s)",(self._nombre,self._nota))
            conexion.commit()
            return True
            
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            return False
    def consultar(self):
        try: 
            cursor.execute("select * from estudiantes")
            
            return cursor.fetchall()
        except Exception as e: 
            print(f"Ocurrió un error: {e}")
            return []
    def eliminar(self,id):
        try: 
            cursor.execute("delete from estudiantes where id=%s",(id,))
            conexion.commit()
            return True
        except: 
            return False 
    def actualizar(self,id):
        try:

            cursor.execute("update estudiantes set nombre=%s, nota=%s where id=%s",(self._nombre,self._nota,id))

            conexion.commit()
            return True 
        except Exception as e: 
            print(f"Ocurrió un error: {e}")
            return False
