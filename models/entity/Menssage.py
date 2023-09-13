class Message:

    def __init__(self, id_mensaje, mensajes, servidor_id, canal_id, autor_id):
        self.id_mensaje = id_mensaje
        self.mensajes = mensajes
        self.servidor_id = servidor_id
        self.canal_id = canal_id
        self.autor_id = autor_id

    def to_json(self):
        return {
            "Id": self.id_mensaje,
            "Mensaje": self.mensajes,
            "Servidor_ID": self.servidor_id,
            "Canal_ID": self.canal_id,
            "Autor_ID": self.autor_id
        }
