from flask import Flask, jsonify, request
from flask_cors import CORS

from models.LoginModel import LoginUser
from models.ServerModel import ModelServer
from models.UserModel import ModelUser
from models.ChannelModel import ModelChannel
from models.MessageModel import MessageModel


def discord_all():
    app = Flask(__name__)
    CORS(app)

    @app.route('/api/user/list')
    def get_user():
        try:
            user = ModelUser.get_users()
            return jsonify({'Users': user}), 200
        except Exception as e:
            return jsonify({'Msg': 'Internal Server Error', 'Error': str(e)}), 500

    @app.route('/api/user/list/disable', methods=['GET'])
    def get_user_status():
        try:
            user_status = ModelUser.get_users_disable()
            return user_status
        except Exception as e:
            return jsonify({'Msg': 'Internal Server Error', 'Error': str(e)}), 500

    @app.route('/api/user/<int:user_id>')
    def get_user_id(user_id):
        try:
            user = ModelUser.user_id(user_id)
            return jsonify({'Users': user})
        except Exception as e:
            return jsonify({'Msg': 'Internal Server Error', 'Error': str(e)}), 500

    #
    @app.route('/api/user/add', methods=['POST'])
    def add_user():
        nombre = request.json['nombre']
        email = request.json['email']
        password = request.json['password']

        if not nombre or not email or not password:
            return jsonify({'Msg': 'Missing data'}), 400

        try:
            user = ModelUser.add_user(nombre, email, password)
            return jsonify({"Create": user}), 201
        except Exception as e:
            return jsonify({'Msg': 'Internal Server Error', 'Error': str(e)}), 500

    @app.route('/api/user/update/<int:id_user>', methods=['PUT'])
    def edit_user(id_user):
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        nick = request.json['nick']
        avatar = request.json['avatar']

        try:
            user_edit = ModelUser.edit_user(nombre, apellido, nick, avatar, id_user)
            return user_edit
        except Exception as e:
            return jsonify({'Msg': 'Internal Server Error', 'Error': str(e)}), 500

    @app.route('/api/user/delete/<int:id_user>', methods=['DELETE'])
    def delete_user(id_user):
        try:
            user_delete = ModelUser.delete_user(id_user)
            return user_delete
        except Exception as e:
            return jsonify({'Msg': 'Internal Server Error', 'Error': str(e)}), 500

    #
    @app.route('/api/user/login', methods=['POST'])
    def login():
        email = request.json['email']
        password = request.json['password']

        if not email:
            return jsonify({'Msg': 'Missing email'}), 400

        if not password:
            return jsonify({'Msg': 'Missing password'}), 400

        try:
            user = LoginUser.login_cls(email, password)
            return user
        except Exception as e:
            return Exception({'message': 'Internal Server Error', 'Error': str(e)}), 500

    # SERVIDORES

    @app.route('/api/server/list')
    def get_server():
        try:
            servers = ModelServer.get_server()
            return jsonify({'Servers': servers}), 200
        except Exception as e:
            return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500

    # ARREGLAR DEEL MISMO N SE CUENTRA DEVUELVE ALGO VACIO
    # # NO QUIERO ESO
    # # SI NO QUE DEVUELVA UN MENSAJE DE ERROR O ALGO por el estilo!!!

    @app.route("/api/server/list/disable", methods=['GET'])
    def get_server_disable():
        try:
            server_disable = ModelServer.get_server_disable()
            return server_disable
        except Exception as e:
            return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500

    @app.route('/api/server/<int:id_server>')
    def get_server_by_id(id_server):
        try:
            server = ModelServer.get_server_by_id(id_server)
            return jsonify({'Server': server})
        except Exception as e:
            return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500

    @app.route('/api/server/add', methods=['POST'])
    def add_server():
        nombre_servidor = request.json['nombre_servidor']
        descripcion = request.json['descripcion']
        autor_id = request.json['autor_id']
        try:
            server = ModelServer.add_server(nombre_servidor, descripcion, autor_id)
            return jsonify({'Info': server})
        except Exception as e:
            return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500

    @app.route('/api/server/update/<int:id_server>', methods=['PUT'])
    def update_server(id_server):
        try:
            nombre_servidor = request.json['nombre_servidor']
            descripcion = request.json['descripcion']

            server = ModelServer.server_update(nombre_servidor, descripcion, id_server)
            return server
        except Exception as e:
            return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500

    @app.route('/api/server/delete/<int:id_server>', methods=['DELETE'])
    def del_servidor(id_server):
        try:
            server = ModelServer.delete_server(id_server)
            return server
        except Exception as e:
            return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500

    @app.route('/api/server/<int:id_user>/add', methods=['POST'])
    def add_server_user(id_user):
        """
        Agrega un servidor a un usuario

        :param id_user: id del usuario
        {
            "id_server": 1
        }
        """
        id_server = request.json['id_server']
        try:
            server = ModelServer.add_server_user(id_user, id_server)
            return server
        except Exception as e:
            return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500

    @app.route('/api/server/user/<int:id_user>', methods=['GET'])
    def get_server_by_user(id_user):
        try:
            server = ModelServer.get_server_by_user(id_user)
            return server
        except Exception as e:
            return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500

    # CANALES

    @app.route("/api/channel/server/<int:id_server>", methods=['GET'])
    def channel_id(id_server):
        try:
            channel = ModelChannel.get_channel_by_server(id_server)
            return channel
        except Exception as e:
            return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500

    @app.route("/api/channel/add", methods=['POST'])
    def add_channel():
        try:
            nombre_canal = request.json['nombre_canal']
            descripcion = request.json['descripcion']
            servidor_id = request.json['servidor_id']
            autor_id = request.json['autor_id']
            channel = ModelChannel.add_channel(nombre_canal, descripcion, servidor_id, autor_id)
            return channel
        except Exception as e:
            return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500

    # MENSAJES
    @app.route("/api/message/add", methods=['POST'])
    def add_message():
        try:
            mensajes = request.json['mensajes']
            servidor_id = request.json['servidor_id']
            canal_id = request.json['canal_id']
            autor_id = request.json['autor_id']
            message = MessageModel.add_message(mensajes, servidor_id, canal_id, autor_id)
            return message
        except Exception as e:
            return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500

    @app.route("/api/message/<int:id_channel>", methods=['GET'])
    def get_message(id_channel):
        try:
            message = MessageModel.get_message(id_channel)
            return message
        except Exception as e:
            return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500

    @app.route("/api/message/delete/<int:id_message>", methods=['DELETE'])
    def delete_message(id_message):
        try:
            message = MessageModel.delete_message(id_message)
            return message
        except Exception as e:
            return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500

    @app.route("/api/message/update/<int:id_message>", methods=['PUT'])
    def update_message(id_message):
        try:
            mensajes = request.json['mensajes']
            message = MessageModel.update_message(id_message, mensajes)
            return message
        except Exception as e:
            return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500

    @app.route('/api/message/<int:id_message>', methods=['GET'])
    def get_message_id(id_message):
        try:
            message = MessageModel.get_message_by_id(id_message)
            return message
        except Exception as e:
            return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500

    return app
