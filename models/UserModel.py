# Entity
from exceptions.ExceptionsHandler import MissingData, EmailUse, UserNotFound, NoUsers, UserNotCreate, UpdateNotCreate
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
        sql = """SELECT * FROM usuario"""
        conn.execute(sql)
        fetch = conn.fetchall()
        if not fetch:
            raise NoUsers()

        return cls.response(fetch)

    @classmethod
    def user_id(cls, user_id):
        conn = Conexion()
        sql = """SELECT * FROM usuario WHERE id_usuario = %s"""
        conn.execute(sql, (user_id,))
        dato = conn.fetchall()
        if not dato:
            raise UserNotFound()
        else:
            return cls.response(dato)

    @classmethod
    def add_user(cls, nick, nombre, apellido, email, password):
        conn = Conexion()

        if not nick or not nombre or not apellido or not email or not password:
            raise MissingData()

        if cls.check_user(email):
            raise EmailUse()

        sql = """INSERT INTO usuario (nick, nombre, apellido, email, password) VALUES (%s, %s, %s, %s, %s)"""
        conn.execute(sql, (nick, nombre, apellido, email, password,))
        conn.commit()
        if conn.rowcount() > 0:
            response_data = {
                "Message": "User was created successfully",
            }
            return response_data, 201
        else:
            raise UserNotCreate()

    @classmethod
    def edit_user(cls, nombre, apellido, nick, avatar, id_user):

        if avatar is None:
            avatar = "https://www.gravatar.com/avatar/default?s=200&d=mp"
        # is a default img for user if not have avatar and if no add new img on the edit user table
        # the img as random img for user from the web no for the user

        if cls.check_user(id_user):
            raise UserNotFound()

        conn = Conexion()
        sql = """UPDATE usuario SET nombre = %s, apellido = %s, nick = %s, avatar = %s WHERE id_usuario = %s"""
        conn.execute(sql, (nombre, apellido, nick, avatar, id_user,))
        conn.commit()
        if conn.rowcount() > 0:
            response_data = {
                "Message": "User was updated successfully",
                "New Data": {
                    "Nombre": nombre,
                    "Apellido": apellido,
                    "Nick": nick
                }
            }
            return response_data, 202
        else:
            raise UpdateNotCreate()

    @classmethod
    def delete_user(cls, id_user):
        conn = Conexion()
        sql = 'UPDATE usuario SET estado = 0 WHERE id_usuario = %s'
        conn.execute(sql, (id_user,))
        conn.commit()
        if conn.rowcount() > 0:
            result = {
                'Message': 'User was succesfull delete',
                'Tip': 'User is not delete, only change status to 0'
            }
            return result
        else:
            raise UserNotFound()

    @classmethod
    def get_users_disable(cls):
        conn = Conexion()
        try:
            sql = 'SELECT * FROM usuario WHERE estado = 0'
            conn.execute(sql)
            fetch = conn.fetchall()
            return cls.response(fetch)
        except Exception as e:
            raise Exception(e)

    @classmethod
    def check_user(cls, email):
        conn = Conexion()
        try:
            sql = 'SELECT * FROM usuario WHERE email = %s'
            conn.execute(sql, (email,))
            dato = conn.fetchone()
            if dato is not None:
                return True
            else:
                return False
        except Exception as e:
            raise Exception(e)

    @classmethod
    def check_user_id(cls, user_id):
        conn = Conexion()
        sql = """SELECT * FROM usuario WHERE id_usuario = %s"""
        conn.execute(sql, (user_id,))
        dato = conn.fetchone()
        if not dato:
            raise UserNotFound()
        else:
            return True
