from flask import Blueprint, jsonify, request

from models.UserModel import ModelUser
from models.LoginModel import LoginUser

# Blueprint
user_app = Blueprint('user_app', __name__)


@user_app.route('/list')
def get_user():
    try:
        user = ModelUser.get_users()
        return jsonify({'Users': user}), 200
    except Exception as e:
        return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500


@user_app.route('/list/disable', methods=['GET'])
def get_user_status():
    try:
        user_status = ModelUser.get_users_disable()
        return user_status
    except Exception as e:
        return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500


@user_app.route('/<int:user_id>')
def get_user_id(user_id):
    try:
        user = ModelUser.user_id(user_id)
        return jsonify({'Users': user})
    except Exception as e:
        return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500


#
@user_app.route('/add', methods=['POST'])
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


@user_app.route('/update/<int:id_user>', methods=['PUT'])
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


@user_app.route('/delete/<int:id_user>', methods=['DELETE'])
def delete_user(id_user):
    try:
        user_delete = ModelUser.delete_user(id_user)
        return user_delete
    except Exception as e:
        return jsonify({'message': 'Internal Server Error', 'Error': str(e)}), 500


#
@user_app.route('/login', methods=['POST'])
def login():
    # nombre = request.json['nombre']
    email = request.json['email']
    password = request.json['password']

    if not email or not password:
        return jsonify({'message': 'Missing data'}), 400
    try:
        user = LoginUser.login_cls(email, password)
        return user
    except Exception as e:
        return Exception({'message': 'Internal Server Error', 'Error': str(e)}), 500
