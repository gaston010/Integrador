from exceptions.ExceptionsHandler import ServerNotFound, ServerNotCreate, ServerExist, MissingData, UserNotFound
from models import UserModel
from models.UserModel import ModelUser
from utils.Conexion import Conexion
from models.entity.Server import Server, ServeUser


class ModelServer:

    @classmethod
    def repeat(cls, data):
        server_list = []
        for server in data:
            server = Server(server[0], server[1], server[2],
                            server[3], server[4], server[5], server[6])
            server_list.append(server.to_json())
        return server_list

    @classmethod
    def get_server(cls):
        conn = Conexion()
        sql = """SELECT * FROM servidor WHERE estado = 1"""
        conn.execute(sql)
        fetch = conn.fetchall()
        if not fetch:
            raise ServerNotFound()
        else:
            return cls.repeat(fetch)

    @classmethod
    def get_server_by_id(cls, id_server):
        conn = Conexion()
        sql = 'SELECT * FROM servidor WHERE id_servidor = %s'
        conn.execute(sql, (id_server,))
        servidor = conn.fetchall()
        if not servidor:
            raise ServerNotFound()
        else:
            return cls.repeat(servidor)

    @classmethod
    def get_by_last_add(cls):
        conn = Conexion()
        try:
            sql = 'SELECT * FROM servidor ORDER BY id_servidor DESC LIMIT 1'
            conn.execute(sql)
            servidor = conn.fetchall()
            return cls.repeat(servidor)
        except Exception as e:
            raise Exception(e)

    @classmethod
    def check_server(cls, nombre_servidor):
        """Comprueba si existe un servidor con el nombre pasado por parametro"""
        conn = Conexion()

        sql = 'SELECT nombre_servidor FROM servidor WHERE nombre_servidor = %s'
        conn.execute(sql, (nombre_servidor,))
        server = conn.fetchall()
        if not server:
            return False
        else:
            return True

    @classmethod
    def add_server(cls, nombre_servidor, descripcion, autor_id):
        """Añade un servidor a la base de datos, si el mismo ya existe devuelve un mensaje de error"""

        # Comprueba si el servidor ya existe ESTO ES LA PRIMER COMPROBACION A PESAR DE QUE EL USUARIO NO EXISTA
        if cls.check_server(nombre_servidor):
            raise ServerExist()

        if not nombre_servidor or not descripcion or not autor_id:
            raise MissingData()

        if ModelUser.check_user_id(autor_id):
            conn = Conexion()
            sql = 'INSERT INTO servidor (nombre_servidor, descripcion, autor_id) VALUES (%s, %s, %s)'
            conn.execute(sql, (nombre_servidor, descripcion, autor_id))
            conn.commit()
            if conn.rowcount() > 0:
                data_response = {
                    'message': 'Server created successfully',
                    'New Server info:': cls.get_by_last_add(),
                }
                return data_response, 201
            else:
                raise ServerNotCreate()
        else:
            raise UserNotFound()

    @classmethod
    def server_update(cls, nombre_servidor, descripcion, id_server):

        conn = Conexion()
        try:
            sql = 'UPDATE servidor SET nombre_servidor = %s, descripcion = %s WHERE id_servidor = %s'
            conn.execute(sql, (nombre_servidor, descripcion, id_server))
            conn.commit()
            update = cls.get_server_by_id(id_server)
            if conn.rowcount() > 0:
                response_data = {
                    'message': 'Server updated successfully',
                    "New update info": {
                        "id_servidor": update[0]['id_servidor'],
                        "nombre_servidor": update[0]['nombre_servidor'],
                        "descripcion": update[0]['descripcion'],
                        "autor_id": update[0]['autor_id'],
                        "fecha_creacion": update[0]['fecha_creacion'],
                        "estado": update[0]['estado']
                    }
                }
                return response_data, 200
            else:
                response_data = {
                    'message': 'Server not updated'
                }
                return response_data, 400
        except Exception as e:
            raise Exception(e)

    @classmethod
    def delete_server(cls, id_server):
        conn = Conexion()
        try:
            sql = 'UPDATE servidor SET estado = 0 WHERE id_servidor = %s'
            conn.execute(sql, (id_server,))
            conn.commit()
            if conn.rowcount() > 0:
                return {'message': 'Server deleted successfully',
                        'TIP': 'Serves was be disable status = 0 on database'}, 200
            else:
                return {'message': 'Server not found'}, 404
        except Exception as error:
            raise Exception(error)

    @classmethod
    def add_server_user(cls, id_user, id_server):
        conn = Conexion()
        combine = str(id_user) + str(id_server)
        try:
            sql = 'INSERT INTO usuario_servidor (usuario_id, servidor_id, combine_id) VALUES (%s, %s, %s)'
            conn.execute(sql, (id_user, id_server, combine))
            conn.commit()
            if conn.rowcount() > 0:
                response_data = {
                    'message': 'User added to server successfully'

                }
                return response_data, 200
            else:
                response_data = {
                    'message': 'User not added to server'
                }
                return response_data, 400
        except Exception as error:
            raise Exception(error)

    @classmethod
    def get_server_by_user(cls, id_user):
        conn = Conexion()
        try:
            sql = """SELECT id_usuario, nombre, email ,nick , servidor_id, nombre_servidor, descripcion
                    from usuario_servidor us
                    inner join usuario u on id_usuario = usuario_id
                    inner join servidor s on id_servidor = servidor_id
                     where usuario_id = %s"""
            conn.execute(sql, (id_user,))
            servers = conn.fetchall()
            server_list = []
            if servers is None:
                response_data = {
                    'message': 'User not found'
                }
                return response_data, 404
            else:
                for server in servers:
                    server = ServeUser(server[0], server[1], server[2], server[3], server[4], server[5], server[6])
                    server_list.append(server.to_json())

            return server_list, 200
        except Exception as e:
            raise Exception(e)

    @classmethod
    def get_server_disable(cls):
        conn = Conexion()
        sql = """SELECT * FROM servidor WHERE estado = 0"""
        conn.execute(sql)
        fetch = conn.fetchall()
        if not fetch:
            raise ServerNotFound()
        else:
            return cls.repeat(fetch)
