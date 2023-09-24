class Server:

    def __init__(self, id_servidor, nombre_servidor, descripcion, autor_id, fecha_creacion, ultima_actualizacion,
                 estado, icono):
        self.id_servidor = id_servidor
        self.nombre_servidor = nombre_servidor
        self.descripcion = descripcion
        self.autor_id = autor_id
        self.fecha_creacion = fecha_creacion
        self.ultima_actualizacion = ultima_actualizacion
        self.estado = estado
        self.icono = icono

    def to_json(self):
        return {
            "id_servidor": self.id_servidor,
            "nombre_servidor": self.nombre_servidor,
            "descripcion": self.descripcion,
            "autor_id": self.autor_id,
            "fecha_creacion": self.fecha_creacion,
            "ultima_actualizacion": self.ultima_actualizacion,
            "estado": self.estado,
            "icono": self.icono
        }


class ServeUser:

    def __init__(self, id_servidor, nombre_servidor, descripcion, autor_id, nombre):
        self.id_servidor = id_servidor
        self.nombre_servidor = nombre_servidor
        self.descripcion = descripcion
        self.autor_id = autor_id
        self.nombre = nombre

    def to_json(self):
        return {
            "Servidor": {
                "servidor_id": self.id_servidor,
                "nombre_servidor": self.nombre_servidor,
                "descripcion": self.descripcion,

            },
            "Usuario": {
                "autor_id": self.autor_id,
                "nombre": self.nombre
            }

        }
