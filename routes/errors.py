from flask import Blueprint

from exceptions.ExceptionsHandler import CustomException, EmailUse, MissingData, UserNotFound, UpdateNotCreate

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(EmailUse)
def handle_exception(error):
    return error.get_response()


@errors.app_errorhandler(MissingData)
def missing_data(error):
    return error.get_response()


@errors.app_errorhandler(UserNotFound)
def user_not_found(error):
    return error.get_response()


@errors.app_errorhandler(UpdateNotCreate)
def update_nocreate(error):
    return error.get_response()


@errors.app_errorhandler(CustomException)
def user_no_server(error):
    return error.get_response()


@errors.app_errorhandler(CustomException)
def server_no_create(error):
    return error.get_response()


@errors.app_errorhandler(CustomException)
def server_exist(error):
    return error.get_response()


@errors.app_errorhandler(CustomException)
def no_insert(error):
    return error.get_response()


@errors.app_errorhandler(CustomException)
def no_channels(error):
    return error.get_response()


@errors.app_errorhandler(CustomException)
def user_disable(error):
    return error.get_response()
