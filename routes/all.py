from flask import Flask, jsonify, request
from flask_cors import CORS
from models.ServerModel import ModelServer
from models.UserModel import ModelUser
from models.ChannelModel import ModelChannel


def discord_all():
    app = Flask(__name__)
    CORS(app)

    @app.route('/api/user/list')
    def get_user():
        try:
            user = ModelUser.get_users()
            return jsonify({'Users': user}), 200
        except Exception as e:
            return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500

    @app.route('/api/user/list/disable', methods=['GET'])
    def get_user_status():
        try:
            user_status = ModelUser.get_users_disable()
            return user_status
        except Exception as e:
            return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500

    @app.route('/api/user/<int:user_id>')
    def get_user_id(user_id):
        try:
            user = ModelUser.user_id(user_id)
            return jsonify({'Users': user})
        except Exception as e:
            return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500

    #
    @app.route('/api/user/add', methods=['POST'])
    def add_user():
        nombre = request.json['nombre']
        email = request.json['email']
        password = request.json['password']

        if not nombre or not email or not password:
            return jsonify({'message': 'Missing data'}), 400

        try:
            user = ModelUser.add_user(nombre, email, password)
            return jsonify({"create": user}), 201
        except Exception as e:
            return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500

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
            return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500

    @app.route('/api/user/delete/<int:id_user>', methods=['DELETE'])
    def delete_user(id_user):
        try:
            user_delete = ModelUser.delete_user(id_user)
            return user_delete
        except Exception as e:
            return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500

    #
    @app.route('/api/user/login', methods=['POST'])
    def login():
        email = request.json['email']
        password = request.json['password']

        if not email or not password:
            return jsonify({'message': 'Missing data'}), 400
        try:
            user = ModelUser.login(email, password)
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

    # ARREGLAR DESPUES ESTO , ESTO SOLO DEVUELVE UNA LISTA DE SERVIDORES PERO SI EL MISMO N SE CUENTRA DEVUELVE ALGO VACIO
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

    @app.route("/api/channel/list", methods=['GET'])
    def channel_list():
        try:
            channel = ModelChannel.get_channel_by_user()
            return channel
        except Exception as e:
            return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500

    return app
