from flask import Blueprint, jsonify, request

from models.ServerModel import ModelServer

# # Blueprint
server_app = Blueprint('server_app', __name__)


@server_app.route('/list')
def get_server():
    try:
        servers = ModelServer.get_server()
        return jsonify({'Servers': servers}), 200
    except Exception as e:
        return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500


# ARREGLAR DESPUES ESTO , ESTO SOLO DEVUELVE UNA LISTA DE SERVIDORES PERO SI EL MISMO N SE CUENTRA DEVUELVE ALGO VACIO
# # NO QUIERO ESO
# # SI NO QUE DEVUELVA UN MENSAJE DE ERROR O ALGO por el estilo!!!
@server_app.route('/<int:id_server>')
def get_server_by_id(id_server):
    try:
        server = ModelServer.get_server_by_id(id_server)
        return jsonify({'Server': server})
    except Exception as e:
        return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500


@server_app.route('/add', methods=['POST'])
def add_server():
    nombre_servidor = request.json['nombre_servidor']
    descripcion = request.json['descripcion']
    autor_id = request.json['autor_id']
    try:
        server = ModelServer.add_server(nombre_servidor, descripcion, autor_id)
        return jsonify({'Info': server})
    except Exception as e:
        return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500


@server_app.route('/update/<int:id_server>', methods=['PUT'])
def update_server(id_server):
    try:
        nombre_servidor = request.json['nombre_servidor']
        descripcion = request.json['descripcion']

        server = ModelServer.server_update(nombre_servidor, descripcion, id_server)
        return server
    except Exception as e:
        return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500


@server_app.route('/delete/<int:id_server>', methods=['DELETE'])
def del_servidor(id_server):
    try:
        server = ModelServer.delete_server(id_server)
        return server
    except Exception as e:
        return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500


@server_app.route('/<int:id_user>/add', methods=['POST'])
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


@server_app.route('/user/<int:id_user>', methods=['GET'])
def get_server_by_user(id_user):
    try:
        server = ModelServer.get_server_by_user(id_user)
        return server
    except Exception as e:
        return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500
