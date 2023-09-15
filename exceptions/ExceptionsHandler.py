from flask import jsonify


class CustomException(Exception):

    def __init__(self, status_code, name="Custom Error", description='Error'):
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = status_code

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response


class GeneralError(CustomException):
    def __init__(self):
        super().__init__(500, name="General Error", description="Internal Server Error")


class UserNotFound(CustomException):
    def __init__(self):
        super().__init__(404, name="User Not Found", description="User not found in database")


class NoUsers(CustomException):
    def __init__(self):
        super().__init__(404, name="No Users", description="No users in database")


class UserNotCreate(CustomException):
    def __init__(self):
        super().__init__(404, name="User Not Create", description="Could not create user")


class EmailUse(CustomException):
    def __init__(self):
        super().__init__(409, name="Email Use", description="Email already in use")


class UpdateNotCreate(CustomException):
    def __init__(self):
        super().__init__(404, name="Update Not Create", description="Could not update ")


class ChannelNoExist(CustomException):
    def __init__(self):
        super().__init__(404, name="Channel Not Found", description="Channel not found in database")


class MissingData(CustomException):
    def __init__(self):
        super().__init__(400, name="Missing Data", description="Some data on the request is missing")


class ServerNotFound(CustomException):
    def __init__(self):
        super().__init__(404, name="Server Not Found", description="Server not found in database")


class ServerNotCreate(CustomException):
    def __init__(self):
        super().__init__(404, name="Server Not Create", description="Could not create server")


class ServerExist(CustomException):
    def __init__(self):
        super().__init__(409, name="Server Exist", description="Server already exist in database")


class ServerJetDelete(CustomException):
    def __init__(self):
        super().__init__(409, name="Server Jet Delete", description="Server already delete in database")
