from models.entity.User import UserLogin
from utils.Conexion import Conexion

import re


class LoginUser:

    @classmethod
    def login_cls(cls, email, password):
        con = Conexion()
        try:
            sql = """SELECT id_usuario, nombre, email, nick , avatar, nick,password FROM usuario 
                    WHERE email = %s AND password = %s"""
            con.execute(sql, (email, password))
            user = con.fetchall()
            print(user)
            if not user:
                response_data = {
                    "message": "Email or password miss match"
                }
                return response_data, 404
            else:
                login_user = []
                for usser in user:
                    item = UserLogin(usser[0], usser[1], usser[2], usser[3], usser[4], usser[5])
                    login_user.append(item.to_json_login())
                return login_user, 200
        except Exception as e:
            raise Exception(e)

    @classmethod
    def email_validator(cls, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, email):
            return True
        return False
