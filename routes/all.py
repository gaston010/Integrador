from flask import Flask, jsonify, request
from flask_cors import CORS

from exceptions.ExceptionsHandler import GeneralError
from models.LoginModel import LoginUser
from models.ServerModel import ModelServer
from models.UserModel import ModelUser
from models.ChannelModel import ModelChannel
from models.MessageModel import MessageModel
from routes.errors import errors


def discord_all():
    app = Flask(__name__)
    CORS(app)

    @app.route('/api/user/list')
    def get_user():
        user = ModelUser.get_users()
        return user

    @app.route('/api/user/list/disable', methods=['GET'])
    def get_user_status():
        try:
            user_status = ModelUser.get_users_disable()
            return user_status
        except Exception as e:
            return jsonify({'Msg': 'Internal Server Error', 'Error': str(e)}), 500

    @app.route('/api/user/<int:user_id>')
    def get_user_id(user_id):
        user = ModelUser.user_id(user_id)
        return user

    #
    @app.route('/api/user/add', methods=['POST'])
    def add_user():
        nick = request.json['nick']
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        email = request.json['email']
        password = request.json['password']

        user = ModelUser.add_user(nick, nombre, apellido, email, password)
        return user

    @app.route('/api/user/update/<int:id_user>', methods=['PUT'])
    def edit_user(id_user):
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        nick = request.json['nick']
        avatar = request.json['avatar']

        user_edit = ModelUser.edit_user(nombre, apellido, nick, avatar, id_user)
        return user_edit

    @app.route('/api/user/delete/<int:id_user>', methods=['PUT'])
    def delete_user(id_user):
        user_delete = ModelUser.delete_user(id_user)
        return user_delete

    #
    @app.route('/api/user/login', methods=['POST'])
    def login():
        email = request.json['email']
        password = request.json['password']

        login_data = LoginUser.login_cls(email, password)
        return login_data

    # SERVIDORES

    @app.route('/api/server/list')
    def get_server():
        servers = ModelServer.get_server()
        return servers

    @app.route("/api/server/disable", methods=['GET'])
    def get_server_disable():

        server_disable = ModelServer.get_server_disable()
        return server_disable

    @app.route('/api/server/<int:id_server>')
    def get_server_by_id(id_server):

        server = ModelServer.get_server_by_id(id_server)
        return server

    @app.route('/api/server/add', methods=['POST'])
    def add_server():
        nombre_servidor = request.json['nombre_servidor']
        descripcion = request.json['descripcion']
        autor_id = request.json['autor_id']

        server = ModelServer.add_server(nombre_servidor, descripcion, autor_id)
        return server

    @app.route('/api/server/update/<int:id_server>', methods=['PUT'])
    def update_server(id_server):
        try:
            nombre_servidor = request.json['nombre_servidor']
            descripcion = request.json['descripcion']

            server = ModelServer.server_update(nombre_servidor, descripcion, id_server)
            return server
        except GeneralError:
            raise GeneralError()

    @app.route('/api/server/delete/<int:id_server>', methods=['PUT'])
    def del_servidor(id_server):
        try:
            server = ModelServer.delete_server(id_server)
            return server
        except GeneralError:
            raise GeneralError()

    @app.route('/api/server/<int:id_user>/add', methods=['POST'])
    def add_server_user(id_user):

        id_server = request.json['id_server']
        try:
            server = ModelServer.add_user_to_server(id_user, id_server)
            return server
        except GeneralError:
            raise GeneralError()

    @app.route('/api/server/user/<int:id_user>', methods=['GET'])
    def get_server_by_user(id_user):
        try:
            server = ModelServer.get_server_by_user(id_user)
            return server
        except GeneralError:
            raise GeneralError()

    # CANALES

    @app.route("/api/channel/server/<int:id_server>", methods=['GET'])
    def channel_id(id_server):
        try:
            channel = ModelChannel.get_channel_by_server(id_server)
            return channel
        except GeneralError:
            raise GeneralError()

    @app.route("/api/channel/add", methods=['POST'])
    def add_channel():
        try:
            nombre_canal = request.json['nombre_canal']
            descripcion = request.json['descripcion']
            servidor_id = request.json['servidor_id']
            autor_id = request.json['autor_id']
            channel = ModelChannel.add_channel(nombre_canal, descripcion, servidor_id, autor_id)
            return channel
        except GeneralError:
            raise GeneralError()

    @app.route("/api/channel/update/<int:id_canal>", methods=['PUT'])
    def update_channel(id_canal):
        try:
            nombre_canal = request.json['nombre_canal']
            descripcion = request.json['descripcion']
            channel = ModelChannel.update_channel(nombre_canal, descripcion, id_canal)
            return channel
        except GeneralError:
            raise GeneralError()

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
        except GeneralError:
            raise GeneralError()

    @app.route("/api/message/", methods=['GET'])
    def get_message():
        id_channel = request.json['id_channel']
        try:
            message = MessageModel.get_message(id_channel)
            return message
        except GeneralError:
            raise GeneralError()

    @app.route("/api/message/delete/<int:id_message>", methods=['DELETE'])
    def delete_message(id_message):
        try:
            message = MessageModel.delete_message(id_message)
            return message
        except GeneralError:
            raise GeneralError()

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

    app.register_blueprint(errors)
    return app
