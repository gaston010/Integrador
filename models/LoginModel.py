from models.entity.User import UserLogin
from utils.Conexion import Conexion


class LoginUser:

    @classmethod
    def login_cls(cls, email, password):
        con = Conexion()
        try:
            sql = """SELECT id_usuario, 
                        nombre, 
                        email, 
                        nick , 
                        avatar, 
                        nick 
                    FROM usuario 
                    WHERE email = %s AND password = %s"""
            con.execute(sql, (email, password))
            user = con.fetchall()
            if user is not None:
                login_user = []
                for usser in user:
                    item = UserLogin(usser[0], usser[1], usser[2], usser[3], usser[4], usser[5])
                    login_user.append(item.to_json_login())
                return login_user, 200
            else:
                response_data = {
                    "Message": "Check email or password"
                }
                return response_data, 404
        except Exception as e:
            raise Exception(e)


