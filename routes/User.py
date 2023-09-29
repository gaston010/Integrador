from flask import blueprints, request

from exceptions.ExceptionsHandler import GeneralError, NoUsers
from models.UserModel import ModelUser

user_app = blueprints.Blueprint('user_app', __name__)


@user_app.route('/list')
def get_user():
    try:
        user = ModelUser.get_users()
        return user
    except GeneralError:
        raise GeneralError()


@user_app.route('/disable', methods=['GET'])
def get_user_status():
    try:
        user_status = ModelUser.get_users_disable()
        return user_status
    except GeneralError:
        raise GeneralError()


@user_app.route('/<int:user_id>')
def get_user_id(user_id):
    try:
        user = ModelUser.user_id(user_id)
        return user
    except GeneralError:
        raise GeneralError()


@user_app.route('/add', methods=['POST'])
def add_user():
    try:
        nick = request.json['nick']
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        email = request.json['email']
        password = request.json['password']

        user = ModelUser.add_user(nick, nombre, apellido, email, password)
        return user

    except GeneralError:
        raise GeneralError()


@user_app.route('/update/<int:id_user>', methods=['PUT'])
def edit_user(id_user):
    try:
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        nick = request.json['nick']
        avatar = request.json['avatar']

        user_edit = ModelUser.edit_user(nombre, apellido, nick, avatar, id_user)
        return user_edit

    except GeneralError:
        raise GeneralError()


@user_app.route('/delete/<int:id_user>', methods=['PUT'])
def delete_user(id_user):
    try:
        user_delete = ModelUser.delete_user(id_user)
        return user_delete
    except GeneralError:
        raise GeneralError()
