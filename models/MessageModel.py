from exceptions.ExceptionsHandler import GeneralError, MissingData, NoCreate, MessageNotFound
from utils.Conexion import Conexion
from models.entity.Menssage import Message


class MessageModel:

    @classmethod
    def add_message(cls, mensajes, servidor_id, canal_id, autor_id):
        con = Conexion()

        if not servidor_id or not canal_id or not autor_id:
            raise MissingData()

        try:
            sql = """INSERT INTO mensaje(mensajes, servidor_id, canal_id, autor_id) VALUES (%s, %s, %s, %s)"""
            con.execute(sql, (mensajes, servidor_id, canal_id, autor_id))
            con.commit()
            if con.rowcount() > 0:
                data_response = {
                    "message": "message created successfully",
                }
                return data_response, 200
            else:
                raise NoCreate()
        except GeneralError:
            raise GeneralError()

    @classmethod
    def get_message(cls, id_channel):
        con = Conexion()

        if not id_channel:
            raise MissingData()
        try:
            sql = """SELECT * FROM mensaje WHERE canal_id = %s"""
            con.execute(sql, (id_channel,))
            data = con.fetchall()
            if con.rowcount() > 0:
                mensaje_list = []
                for row in data:
                    item = Message(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    mensaje_list.append(item.to_json())
                return mensaje_list, 200
            else:
                raise MessageNotFound()
        except GeneralError:
            raise GeneralError()

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
    def date_mensj(cls, id_message):
        conn = Conexion()
        try:
            sql = """SELECT ultima_actualizacion FROM mensaje WHERE id_mensaje = %s"""
            conn.execute(sql, (id_message,))
            data = conn.fetchall()
            if conn.rowcount() > 0:
                fecha = data[0][0]
                return fecha, 200
            else:
                data_response = {
                    "MSG": [],
                }
                return data_response, 400
        except Exception as e:
            return Exception(e)

    @classmethod
    def update_message(cls, id_message, mensajes):
        conn = Conexion()
        try:
            sql = """UPDATE mensaje SET mensajes = %s WHERE id_mensaje = %s"""
            conn.execute(sql, (mensajes, id_message,))
            conn.commit()
            if conn.rowcount() > 0:
                data_response = {
                    "MSG": "Mensaje actualizado correctamente",
                    "fecha_actualizacion": {
                        "fecha": cls.date_mensj(id_message)
                    }
                }
                return data_response, 200
            else:
                data_response = {
                    "MSG": "No se pudo actualizar el mensaje",
                }
                return data_response, 400
        except Exception as e:
            return Exception(e)

    @classmethod
    def get_message_by_id(cls, id_message):
        conn = Conexion()
        try:
            sql = """SELECT  m.id_mensaje, m.mensajes, m.autor_id, m.canal_id, m.servidor_id, m.fecha_creacion,
                    m.ultima_actualizacion, u.id_usuario, u.nombre,u.nick, u.email FROM mensaje m
                    INNER JOIN usuario u ON m.autor_id = u.id_usuario
                    WHERE m.id_mensaje = %s"""
            conn.execute(sql, (id_message,))
            data = conn.fetchall()
            mensaje_list = []
            if conn.rowcount() > 0:
                for row in data:
                    items = {
                        "id_mensaje": row[0],
                        "mensaje": row[1],
                        "autor_id": row[2],
                        "canal_id": row[3],
                        "servidor_id": row[4],
                        "fecha_creacion": row[5],
                        "ultima_actualizacion": row[6],
                        "USUARIO": {
                            "id_usuario": row[7],
                            "Nombre": row[8],
                            "nick": row[9],
                            "Email": row[10]
                        }
                    }
                    mensaje_list.append(items)
                return mensaje_list, 200
            else:
                data_response = {
                    "MSG": "No se encontraron mensajes con el id",
                }
                return data_response, 400
        except Exception as e:
            return Exception(e)
