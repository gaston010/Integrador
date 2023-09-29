from flask import Blueprint, request

from exceptions.ExceptionsHandler import GeneralError
from models.MessageModel import MessageModel

message_app = Blueprint('message_app', __name__)


@message_app.route("/message/add", methods=['POST'])
def add_message():
    """
    Add a new message to a specified server and channel.

    :param:
    - mensajes (str): The content of the message.
    - servidor_id (int): The ID of the server to which the message belongs.
    - canal_id (int): The ID of the channel to which the message belongs.
    - autor_id (int): The ID of the user who sent the message.

    :return:
       A JSON response containing information about the added message.

    :raises:
    GeneralError: If an error occurs during message addition.
    """
    try:
        mensajes = request.json['mensajes']
        servidor_id = request.json['servidor_id']
        canal_id = request.json['canal_id']
        autor_id = request.json['autor_id']
        message = MessageModel.add_message(mensajes, servidor_id, canal_id, autor_id)
        return message
    except GeneralError:
        raise GeneralError()


@message_app.route("/list", methods=['GET'])
def get_message():
    """
       Get a list of messages from a specific channel.

       This endpoint expects a JSON request with the following parameter:
       - id_channel (int): The ID of the channel to retrieve messages from.

       :return:
      - A JSON response containing a list of messages from the specified channel.

       :except:
      - GeneralError: If an error occurs while retrieving messages.

    """
    id_channel = request.json['id_channel']
    try:
        message = MessageModel.get_message(id_channel)
        return message
    except GeneralError:
        raise GeneralError()


@message_app.route("/delete/<int:id_message>", methods=['DELETE'])
def delete_message(id_message):
    """
       Delete a message by its ID.

       :arg:
       - id_message (int): The ID of the message to delete.

       :return:
        -A JSON response confirming the deletion of the message.

       :except:
        -GeneralError: If an error occurs during the deletion process.
       """
    try:
        message = MessageModel.delete_message(id_message)
        return message
    except GeneralError:
        raise GeneralError()


@message_app.route("/update/<int:id_message>", methods=['PUT'])
def update_message(id_message):
    """
    Update a message by its ID.

    :arg:
    - id_message (int): The ID of the message to update.

    :param:
    - mensajes (str): The updated content of the message.

    :return:
    - A JSON response confirming the update of the message.

    :except:
    - GeneralError: If an error occurs during the update process.
    """
    try:
        mensajes = request.json['mensajes']
        message = MessageModel.update_message(id_message, mensajes)
        return message
    except GeneralError:
        raise GeneralError()


@message_app.route('/<int:id_message>', methods=['GET'])
def get_message_id(id_message):
    """
    Get a message by its ID.

    :arg:
    - id_message (int): The ID of the message to retrieve.

    :return:
    - A JSON response containing the message with the specified ID.

    :except:
    - GeneralError: If an error occurs while retrieving the message.
    """
    try:
        message = MessageModel.get_message_by_id(id_message)
        return message
    except GeneralError:
        raise GeneralError()
