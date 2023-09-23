# Entity
from models.entity.User import User, UserLogin

from utils.Conexion import Conexion


class ModelUser:

    # la misma funcion de abajo se esta repitiendo
    @classmethod
    def response(cls, data):
        user_list = []
        for row in data:
            users = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            user_list.append(users.to_json())
        return user_list

    @classmethod
    def get_users(cls):
        conn = Conexion()
        try:
            sql = 'SELECT * FROM usuario'
            conn.execute(sql)
            user = conn.fetchall()
            if user is not None:
                return cls.response(user)
            else:
                result = {
                    'status': 404,
                    'message': 'Not data in database'
                }
                return result
        except Exception as e:
            return Exception(e)
        finally:
            conn.close()

    @classmethod
    def login(cls, email, password):
        conn = Conexion()
        try:
            sql = 'SELECT nombre, email, password FROM usuario WHERE email = %s'
            conn.execute(sql, (email,))
            dato = conn.fetchone()
            print(dato)
            if dato[1] == email and dato[2] == password:  # noqa
                result = {
                    "Message": "login success",
                    "User": {
                        'nombre': dato[0],
                        'email': dato[1],
                    }
                }
                return result, 200
            elif dato[1] != email or dato[2] != password:
                result = {
                    'message': 'Password or email incorrect'
                }
                return result, 401
            else:
                result = {
                    'message': 'User not found in database'
                }
                return result, 404
        except Exception as e:
            raise Exception(e)

    #
    @classmethod
    def user_id(cls, user_id):
        conn = Conexion()
        try:
            sql = 'SELECT * FROM usuario WHERE id_usuario = %s'
            conn.execute(sql, (user_id,))
            dato = conn.fetchall()
            if dato is not None:
                return cls.response(dato)
            else:
                result = {
                    'status': 404,
                    'message': 'No user in database, please check the id'
                }
                return result
        except Exception as e:
            raise Exception(e)

    @classmethod
    def add_user(cls, nombre, email, password, nick):
        conn = Conexion()
        avatar = f"https://ui-avatars.com/api/?background=random&name={nombre}"

        if cls.check_user(email):
            result = {
                'status': 409,
                'message': 'El usuario ya existe'
            }
            return result
        else:
            password_hash = User.generate_hash(password)
            try:
                sql = """INSERT INTO usuario (nombre, email, password, avatar, nick) VALUES (%s, %s, %s, %s,%s)"""
                values = (nombre, email, password_hash, avatar, nick)
                conn.execute(sql, values)
                conn.commit()
                if conn.rowcount() > 0:
                    result = {
                        'status': 201,
                        'message': 'Usuario creado correctamente'
                    }
                    return result
            except Exception as e:
                raise Exception(e)

    @classmethod
    def check_pass(cls, email, password):
        conn = Conexion()
        try:
            sql = """SELECT password FROM usuario WHERE email = %s"""
            conn.execute(sql, (email,))
            dato = conn.fetchone()
            ps = User.check_password(dato[0], password)
            if ps:
                return True
            else:
                return False
        except Exception as e:
            raise Exception(e)

    @classmethod
    def login_cls(cls, email, password):
        if cls.check_pass(email, password):
            return cls.login_user(email, password)
        else:
            result = {
                'status': 401,
                'message': 'Password or email incorrect'
            }
            return result

    @classmethod
    def check_user(cls, email):
        conn = Conexion()
        try:
            sql = """SELECT * FROM usuario WHERE email = %s"""
            conn.execute(sql, (email,))
            dato = conn.fetchone()
            if dato is not None:
                return True
            else:
                return False
        except Exception as e:
            raise Exception(e)

    @classmethod
    def edit_user(cls, nombre, apellido, nick, avatar, id_user):
        conn = Conexion()
        try:
            sql = """UPDATE usuario SET nombre = %s, apellido = %s, nick = %s, avatar = %s WHERE id_usuario = %s"""
            values = (nombre, apellido, nick, avatar, id_user)
            conn.execute(sql, values)
            conn.commit()
            if conn.rowcount() > 0:
                result = {
                    'status': 202,
                    'message': 'Usuario actualizado correctamente'

                }
                return result
            else:
                result = {
                    'status': 404,
                    'message': 'No se pudo actualizar el usuario'
                }
                return result
        except Exception as e:
            raise Exception(e)
        finally:
            conn.close()

    @classmethod
    def delete_user(cls, id_user):
        conn = Conexion()
        try:
            sql = """UPDATE usuario SET estado = 0 WHERE id_usuario = %s"""
            conn.execute(sql, (id_user,))
            conn.commit()
            if conn.rowcount() > 0:
                result = {
                    'status': 202,
                    'message': 'User was succesfull delete',
                    'TIP': 'The status is 0, the user is disable, not delete'
                }
                return result
            else:
                result = {
                    'status': 404,
                    'message': 'User not found or not exist'
                }
                return result
        except Exception as e:
            raise Exception(e)

    @classmethod
    def get_users_disable(cls):
        conn = Conexion()
        try:
            sql = """SELECT * FROM usuario WHERE estado = 0"""
            conn.execute(sql)
            fetch = conn.fetchall()
            return cls.response(fetch)
        except Exception as e:
            raise Exception(e)

    @classmethod
    def login_user(cls, email, password):
        conn = Conexion()
        try:
            sql = """SELECT * FROM usuario WHERE email = %s"""
            conn.execute(sql, (email,))
            fetch = conn.fetchone()
            if fetch is not None:
                user = UserLogin(fetch[0], fetch[1], fetch[2], fetch[5], fetch[3], fetch[6])
                return user.to_json_login()
            else:
                result = {
                    'status': 404,
                    'message': 'User not found'
                }
                return result
        except Exception as e:
            raise Exception(e)
