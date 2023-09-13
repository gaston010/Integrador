from utils.Conexion import Conexion
from models.entity.Menssage import Message


class MessageModel:

    @classmethod
    def add_message(cls, mensajes, servidor_id, canal_id, autor_id):
        con = Conexion()
        try:
            sql = """INSERT INTO mensaje(mensajes, servidor_id, canal_id, autor_id) VALUES (%s, %s, %s, %s)"""
            con.execute(sql, (mensajes, servidor_id, canal_id, autor_id))
            con.commit()
            if con.rowcount() > 0:
                data_response = {
                    "MSG": "Mensaje agregado correctamente",
                }
                return data_response, 200
            else:
                data_response = {
                    "MSG": "No se pudo agregar el mensaje",
                }
                return data_response, 400
        except Exception as e:
            return Exception(e)

    @classmethod
    def get_message(cls, id_channel):
        con = Conexion()
        try:
            sql = """SELECT * FROM mensaje WHERE canal_id = %s"""
            con.execute(sql, (id_channel,))
            data = con.fetchall()
            if con.rowcount() > 0:
                mensaje_list = []
                for row in data:
                    item = Message(row[0], row[1], row[2], row[3], row[4])
                    mensaje_list.append(item.to_json())
                return mensaje_list, 200
            else:
                data_response = {
                    "MSG": "No se encontraron mensajes con el id del servidor y canal",
                }
                return data_response, 400
        except Exception as e:
            return Exception(e)

    @classmethod
    def delete_message(cls, id_message):
        conn = Conexion()
        try:
            sql = """DELETE FROM mensaje WHERE id_mensaje = %s"""
            conn.execute(sql, (id_message,))
            conn.commit()
            if conn.rowcount() > 0:
                data_response = {
                    "MSG": "Mensaje eliminado correctamente",
                }
                return data_response, 200
            else:
                data_response = {
                    "MSG": "No se pudo eliminar el mensaje",
                }
                return data_response, 400
        except Exception as e:
            return Exception(e)

    @classmethod
    def update_message(cls, id_message, mensajes, fecha_creacion, fecha_actualizacion):
        conn = Conexion()
        try:
            sql = """UPDATE mensaje SET mensajes = %s WHERE id_mensaje = %s"""
            conn.execute(sql, (mensajes, id_message, fecha_creacion, fecha_actualizacion,))
            conn.commit()
            if conn.rowcount() > 0:
                data_response = {
                    "MSG": "Mensaje actualizado correctamente",
                }
                return data_response, 200
            else:
                data_response = {
                    "MSG": "No se pudo actualizar el mensaje",
                }
                return data_response, 400
        except Exception as e:
            return Exception(e)
