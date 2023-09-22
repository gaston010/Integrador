from werkzeug.security import check_password_hash, generate_password_hash


class UserLogin:
    def __init__(self, id_usuario, nombre, email, nick, password, avatar):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.password = password
        self.nick = nick
        self.avatar = avatar

    def to_json_login(self):
        return {
            "user_id": self.id_usuario,
            "Nombre": self.nombre,
            "Email": self.email,
            "Nick": self.nick,
            "Avatar": self.avatar
        }


class User:

    def __init__(self, id_usuario, nombre, email, password, apellido, nick, avatar, estado, fecha_creacion,
                 ultima_actualizacion):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.password = password
        self.apellido = apellido
        self.nick = nick
        self.avatar = avatar
        self.estado = estado
        self.fecha_creacion = fecha_creacion
        self.ultima_actualizacion = ultima_actualizacion

    def to_json(self):
        return {
            'id_usuario': self.id_usuario,
            'nombre': self.nombre,
            'email': self.email,
            'password': self.password,
            'apellido': self.apellido,
            'nick': self.nick,
            'avatar': self.avatar,
            'estado': self.estado,
            'fecha_creacion': self.fecha_creacion,
            'ultima_actualizacion': self.ultima_actualizacion
        }

    @classmethod
    def check_password(cls, hashed_password, password):
        """
        Chequea si el password dado coincide con el password hasheado del usuario.

        Args:
            hashed_password (str): el password hasheado del usuario.
            password (str): el password chequeado.

        Returns:
            bool:True si el password coincide, False en caso contrario.
        """
        return check_password_hash(hashed_password, password)

    @classmethod
    def generate_hash(cls, password):
        """
        Genera un has para un password dado.
        Args:
            password (str): el password a hashear.

        Returns:
            str: el password hasheado.
        """
        return generate_password_hash(password)
