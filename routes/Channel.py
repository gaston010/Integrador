from flask import Blueprint, request

from exceptions.ExceptionsHandler import GeneralError
from models.ChannelModel import ModelChannel

channel_app = Blueprint('channel_app', __name__)


@channel_app.route("/channel/server/<int:id_server>", methods=['GET'])
def channel_id(id_server):
    """
    Get a list of channels belonging to a specific server.

    :parameter:
    - id_server (int): The ID of the server to retrieve channels from.

    :except:
     - GeneralError: If an error occurs while retrieving the channels.

    :return:
    - A JSON response containing a list of channels associated with the specified server.

    """
    try:
        channels = ModelChannel.get_channel_by_server(id_server)
        return channels
    except GeneralError:
        raise GeneralError()


@channel_app.route("/channel/add", methods=['POST'])
def add_channel():
    """
    Add a new channel to a specific server.
    :parameter:
    - nombre_canal (str): The name of the channel to be added.
    - descripcion (str): The description of the channel to be added.
    - servidor_id (int): The ID of the server to which the channel will be added.
    - autor_id (int): The ID of the user who will be the author of the channel.

    :raise GeneralError: If an error occurs while adding the channel.

    :return Channel: A JSON response containing the channel that was added.
    """
    try:
        nombre_canal = request.json['nombre_canal']
        descripcion = request.json['descripcion']
        servidor_id = request.json['servidor_id']
        autor_id = request.json['autor_id']
        channel = ModelChannel.add_channel(nombre_canal, descripcion, servidor_id, autor_id)
        return channel
    except GeneralError:
        raise GeneralError()


@channel_app.route("/channel/update/<int:id_canal>", methods=['PUT'])
def update_channel(id_canal):
    """
        Update a channel by its ID.
        :param:
        - id_canal (int) The ID of the channel to update.
        - descripcion (str): The updated description of the channel.
        - nombre_canal (str) The updated name of the channel.



        :raise GeneralError: If an error occurs during the channel update.
        :return: A JSON response containing information about the updated channel.
    """
    try:
        nombre_canal = request.json['nombre_canal']
        descripcion = request.json['descripcion']
        channel = ModelChannel.update_channel(nombre_canal, descripcion, id_canal)
        return channel
    except GeneralError:
        raise GeneralError()
