from models.entity.User import UserLogin, User
from utils.Conexion import Conexion

import re


class LoginUser:

    @classmethod
    def email_validator(cls, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, email):
            return True
        return False
