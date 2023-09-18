class Server:

    def __init__(self, id_servidor, nombre_servidor, descripcion, autor_id, fecha_creacion, ultima_actualizacion,
                 estado):
        self.id_servidor = id_servidor
        self.nombre_servidor = nombre_servidor
        self.descripcion = descripcion
        self.autor_id = autor_id
        self.fecha_creacion = fecha_creacion
        self.ultima_actualizacion = ultima_actualizacion
        self.estado = estado

    def to_json(self):
        return {
            "id_servidor": self.id_servidor,
            "nombre_servidor": self.nombre_servidor,
            "descripcion": self.descripcion,
            "autor_id": self.autor_id,
            "fecha_creacion": self.fecha_creacion,
            "ultima_actualizacion": self.ultima_actualizacion,
            "estado": self.estado
        }


class ServeUser:

    def __init__(self, id_usuario, nombre, email, nick, servidor_id, nombre_servidor, descripcion):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.nick = nick
        self.servidor_id = servidor_id
        self.nombre_servidor = nombre_servidor
        self.descripcion = descripcion

    def to_json(self):
        return {
            "Datos": [
                {
                    "Usuario": {
                        "id_usuario": self.id_usuario,
                        "nombre": self.nombre,
                        "email": self.email,
                        "nick": self.nick,

                    },
                    "Servidor": {
                        "servidor_id": self.servidor_id,
                        "nombre_servidor": self.nombre_servidor,
                        "descripcion": self.descripcion
                    }
                }
            ]
        }
