class Message:

    def __init__(self, id_mensaje, mensajes, servidor_id, canal_id, autor_id, fecha_creacion, fecha_actualizacion):
        self.id_mensaje = id_mensaje
        self.mensajes = mensajes
        self.servidor_id = servidor_id
        self.canal_id = canal_id
        self.autor_id = autor_id
        self.fecha_creacion = fecha_creacion
        self.fecha_actualizacion = fecha_actualizacion

    def to_json(self):
        return {
            "Id": self.id_mensaje,
            "Mensaje": self.mensajes,
            "Servidor_ID": self.servidor_id,
            "Canal_ID": self.canal_id,
            "Autor_ID": self.autor_id,
            "Fecha_Creacion": self.fecha_creacion,
            "Fecha_Actualizacion": self.fecha_actualizacion
        }
