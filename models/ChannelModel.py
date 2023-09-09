from utils.Conexion import Conexion


class ModelChannel:

    @classmethod
    def get_channel_by_id(cls, id_channel):
        conn = Conexion()
        try:
            sql = 'SELECT * FROM canal WHERE id_canal = %s'
            conn.execute(sql, (id_channel,))
            return conn.fetchall()
        except Exception as e:
            raise Exception(e)

    @classmethod
    def get_channel_by_user(cls, id_user):
        conn = Conexion()
        try:
            sql = """ SELECT c.id_canal, c.nombre_canal, c.descripcion, c.servidor_id, c.autor_id from canal c
                    inner join servidor s on c.servidor_id = s.id_servidor
                    inner join usuario u on s.autor_id = u.id_usuario
                    where c.autor_id = %s"""
            conn.execute(sql, (id_user,))
            return conn.fetchall()
        except Exception as e:
            raise Exception(e)

    @classmethod
    def add_channel(cls, nombre_canal, descripcion, servidor_id, autor_id):
        conn = Conexion()
        try:
            sql = """INSERT INTO canal (nombre_canal, descripcion, servidor_id, autor_id) VALUES (%s, %s, %s, %s)"""
            conn.execute(sql, (nombre_canal, descripcion, servidor_id, autor_id))
            return conn.commit()
        except Exception as e:
            raise Exception(e)

    @classmethod
    def update_channel(cls, nombre_canal, descripcion, id_canal):
        conn = Conexion()
        try:
            sql = """UPDATE canal SET nombre_canal = %s, descripcion = %s WHERE id_canal = %s"""
            conn.execute(sql, (nombre_canal, descripcion, id_canal))
            return conn.commit()
        except Exception as e:
            raise Exception(e)

    @classmethod
    def delete_channel(cls, id_canal):
        conn = Conexion()
        try:
            sql = """DELETE FROM canal WHERE id_canal = %s"""
            conn.execute(sql, (id_canal,))
            return conn.commit()
        except Exception as e:
            raise Exception(e)

    @classmethod
    def add_channel_user(cls, id_user, id_channel):
        conn = Conexion()
        try:
            sql = """INSERT INTO usuario_canal (usuario_id, canal_id) VALUES (%s, %s)"""
            conn.execute(sql, (id_user, id_channel))
            return conn.commit()
        except Exception as e:
            raise Exception(e)

    @classmethod
    def get_channel_by_server(cls, id_server):
        conn = Conexion()
        try:
            sql = """SELECT * FROM canal WHERE servidor_id = %s"""
            conn.execute(sql, (id_server,))
            channel = conn.fetchall()
            if channel is not None:
                for data in channel:
                    response_data = {
                        "id_canal": data[0],
                        "nombre_canal": data[1],
                        "descripcion": data[2],
                        "servidor_id": data[3],
                        "autor_id": data[4]
                    }
                    return response_data, 200
            else:
                response_data = {
                    "message": "No se encontraron canales"
                }
                return response_data, 404

        except Exception as e:
            raise Exception(e)
