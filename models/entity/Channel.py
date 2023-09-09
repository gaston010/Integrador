class Channel:

    def __init__(self, id_channel, nombre_canal, descripcion, servidor_d, autor_id, id_server):
        self.id_channel = id_channel
        self.name_channel = nombre_canal
        self.description = descripcion
        self.server_id = servidor_d
        self.author_id = autor_id
        self.id_server = id_server

    def to_json(self):
        respose_data = {
            'id_channel': self.id_channel,
            'name_channel': self.name_channel,
            'description': self.description,
            'server_id': self.server_id,
            'author_id': self.author_id,
            'id_server': self.id_server
        }
        return respose_data
