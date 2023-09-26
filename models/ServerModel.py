from models.UserModel import ModelUser
from utils.Conexion import Conexion
from models.entity.Server import Server, ServeUser


class ModelServer:

    @classmethod
    def repeat(cls, data):
        server_list = []
        for server in data:
            server = Server(server[0], server[1], server[2],
                            server[3], server[4], server[5], server[6], server[7])
            server_list.append(server.to_json())
        return server_list

    @classmethod
    def get_server(cls):
        conn = Conexion()
        try:
            conn.execute('SELECT * FROM servidor')
            servers = conn.fetchall()
            print('desde la database', servers)
            server_list = []
            if servers is None:
                return f'Empty servers {server_list}', 404
            else:
                return cls.repeat(servers)
        except Exception as e:
            raise Exception(e)

    @classmethod
    def get_server_by_id(cls, id_server):
        conn = Conexion()
        try:
            sql = 'SELECT * FROM servidor WHERE id_servidor = %s'
            conn.execute(sql, (id_server,))
            servidor = conn.fetchall()
            if servidor is not None:
                return cls.repeat(servidor)
            else:
                result = {
                    'status': 404,
                    'message': 'Server not found'
                }
                return result
        except Exception as e:
            raise Exception(e)

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
    def add_server(cls, nombre, descripcion, autor):
        """Añade un servidor a la base de datos, si el mismo ya existe devuelve un mensaje de error"""
        if cls.check_server(nombre):
            return {'message': 'Server already exists'}, 400

        if not nombre or not descripcion or not autor:
            return {'message': 'Empty data'}, 400

        if ModelUser.check_user_id(autor):
            conn = Conexion()
            sql = 'INSERT INTO servidor (nombre_servidor, descripcion, autor_id) VALUES (%s, %s, %s)'
            conn.execute(sql, (nombre, descripcion, autor))
            conn.commit()
            id_server = cls.get_by_last_add()[0]['id_servidor']
            if conn.rowcount() > 0:
                cls.add_user_to_server(autor, id_server)
                data_response = {
                    'message': 'Server created successfully',
                    'New Server info:': cls.get_by_last_add(),
                }
                return data_response, 201
            else:
                data_response = {
                    'message': 'Server not created a error'
                }
                return data_response, 400
        else:
            return {'message': 'User not found'}, 404

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
            sql = """
                SELECT id_servidor, nombre_servidor, descripcion, autor_id, nombre
                from servidor s
                         inner join usuario u on autor_id = id_usuario
                where autor_id = %s"""
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
                    server = ServeUser(server[0], server[1], server[2], server[3], server[4])
                    server_list.append(server.to_json())
            return server_list, 200
        except Exception as e:
            raise Exception(e)

    @classmethod
    def get_server_disable(cls):
        conn = Conexion()
        try:
            sql = """SELECT * FROM servidor WHERE estado = 0 """
            conn.execute(sql)
            servers = conn.fetchall()
            server_list = []
            if servers is None:
                response_data = {
                    'message': 'Servers not found'
                }
                return response_data, 404
            else:
                for server in servers:
                    server = Server(server[0], server[1], server[2],
                                    server[3], server[4], server[5], server[6])
                    server_list.append(server.to_json())
            return server_list, 200
        except Exception as e:
            raise Exception(e)

    @classmethod
    def server_user(cls, id_user):
        conn = Conexion()
        try:
            sql = """SELECT nombre, usuario_id, s.nombre_servidor, servidor_id from usuario_servidor
                INNER JOIN usuario on usuario.id_usuario = usuario_servidor.usuario_id
                INNER JOIN servidor s on s.id_servidor = usuario_servidor.servidor_id
                WHERE usuario_id = %s AND s.estado = 1"""
            conn.execute(sql, (id_user,))
            servers = conn.fetchall()
            server_list = []
            if servers is None:
                response_data = {
                    'message': 'Servers not found'
                }
                return response_data, 404
            else:
                for server in servers:
                    response_data = {
                        "nombre": server[0],
                        "user_id": server[1],
                        "server_name": server[2],
                        "server_id": server[3]
                    }
                    server_list.append(response_data)
            return server_list, 200
        except Exception as e:
            raise Exception(e)

    @classmethod
    def add_user_to_server(cls, id_user, id_server):
        conn = Conexion()
        combine = str(id_user) + str(id_server)

        try:
            sql = 'INSERT INTO usuario_servidor (usuario_id, servidor_id, combine_id) VALUES (%s, %s, %s)'
            conn.execute(sql, (id_user, id_server, combine))
            conn.commit()
            user = ModelUser.user_id(id_user)
            server = cls.get_server_by_id(id_server)
            if conn.rowcount() > 0:
                response_data = {
                    "Message": "User was added successfully",
                    "Data": [
                        {
                            "User": user,
                            "Server": server
                        }
                    ]
                }
                return response_data, 200
            else:
                return {'message': 'User not added to server'}, 400
        except Exception:
            raise Exception
