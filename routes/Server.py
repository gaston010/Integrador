from flask import Blueprint, request

from exceptions.ExceptionsHandler import GeneralError
from models.ServerModel import ModelServer

server_app = Blueprint('server_server_app', __name__)


@server_app.route('/list')
def get_server():
    """
        Get a list of servers.

        :return: A JSON response containing a list of servers.

        :raise GeneralError: If an error occurs while retrieving the servers.
    """
    try:
        servers = ModelServer.get_server()
        return servers
    except GeneralError:
        raise GeneralError()


@server_app.route("/disable", methods=['GET'])
def get_server_disable():
    """
        Get a list of disabled servers.

        :return: A JSON response containing a list of disabled servers.

        :raise GeneralError: If an error occurs while retrieving the disabled servers.
    """
    try:
        server_disable = ModelServer.get_server_disable()
        return server_disable
    except GeneralError:
        raise GeneralError()


@server_app.route('/<int:id_server>')
def get_server_by_id(id_server):
    """
        Get server information by its ID.

        :param:
        - id_server (int) The ID of the server to retrieve.

        :return: A JSON response containing information about the server with the specified ID.

        :raise GeneralError: If an error occurs while retrieving the server.
    """
    try:
        server = ModelServer.get_server_by_id(id_server)
        return server
    except GeneralError:
        raise GeneralError()


@server_app.route('/add', methods=['POST'])
def add_server():
    """
    Add a new server.

    :param:
    - nombre_servidor (str) The name of the server to add.
    - descripcion (str) The description of the server to add.
    - autor_id (int) The ID of the user who created the server.

    :return: A JSON response containing information about the added server.

    :raise GeneralError: If an error occurs during server addition.

    """
    try:
        nombre_servidor = request.json['nombre_servidor']
        descripcion = request.json['descripcion']
        autor_id = request.json['autor_id']

        server = ModelServer.add_server(nombre_servidor, descripcion, autor_id)
        return server
    except GeneralError:
        raise GeneralError()


@server_app.route('/update/<int:id_server>', methods=['PUT'])
def update_server(id_server):
    """
        Update server information by its ID.

        :param:
        - id_server (int) The ID of the server to update.
        - nombre_servidor (str) The name of the server to update.
        - descripcion (str) The description of the server to update.

        :return: A JSON response containing information about the updated server.

        :raise GeneralError: If an error occurs during the server update.
    """
    try:
        nombre_servidor = request.json['nombre_servidor']
        descripcion = request.json['descripcion']

        server = ModelServer.server_update(nombre_servidor, descripcion, id_server)
        return server
    except GeneralError:
        raise GeneralError()


@server_app.route('/delete/<int:id_server>', methods=['PUT'])
def del_servidor(id_server):
    """
        Delete a server by its ID.

        :param:
        - id_server (int) The ID of the server to delete.

        :return: A JSON response confirming the deletion of the server.

        :raise GeneralError: If an error occurs during the server deletion.
    """
    try:
        server = ModelServer.delete_server(id_server)
        return server
    except GeneralError:
        raise GeneralError()


@server_app.route('/<int:id_user>/add', methods=['POST'])
def add_server_user(id_user):
    """
        Add a user to a server.

        :param:
        - id_user (int) The ID of the user to add to the server.
        - id_server (int) The ID of the server to which the user will be added.

        :return: A JSON response containing information about the updated server after adding the user.

        :raise GeneralError: If an error occurs during the user addition to the server.

        """
    id_server = request.json['id_server']
    try:
        server = ModelServer.add_user_to_server(id_user, id_server)
        return server
    except GeneralError:
        raise GeneralError()


@server_app.route('/user/<int:id_user>', methods=['GET'])
def get_server_by_user(id_user):
    """
        Get servers associated with a user by their user ID.

        :param:
        - id_user (int) The ID of the user whose servers will be retrieved.

        :return: A JSON response containing a list of servers associated with the specified user.

        :raise GeneralError: If an error occurs while retrieving the servers.
    """
    try:
        server = ModelServer.get_server_by_user(id_user)
        return server
    except GeneralError:
        raise GeneralError()
