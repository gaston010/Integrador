from flask import Flask
from routes import User, Server
from routes.all import discord_all

# app = Flask(__name__)
app = discord_all()


@app.route('/')
def hello_world():
    data_response = {
        "Servidor EndPoints": {
            "List Server": "/api/server/list",
            "List Server Disable": "/api/server/list/disable",
            "List Server Id": "/api/server/<int:server_id>",
            "Server By user": "/api/server/user/<int:id_user>",
            "Add Server": "/api/server/add",
            "Update Server": "/api/server/update/<int:id_server>",
            "Delete Server": "/api/server/delete/<int:id_server>"
        },
        "User EndPoints": {
            "List User": "/api/user/list",
            "List User Disable": "/api/user/list/disable",
            "List User Id": "/api/user/<int:user_id>",
            "Add User": "/api/user/add",
            "Update User": "/api/user/update/<int:id_user>",
            "Delete User": "/api/user/delete/<int:id_user>"

        },
        "Channel EndPoints": {
            "Channel by id": "/api/channel/server/<int:id_server>"
        },
        "Login User":{
            "Login": "/api/user/login",
        }

    }
    return data_response, 200


if __name__ == '__main__':
    # app.register_blueprint(User.user_app, url_prefix='/api/user')
    # app.register_blueprint(Server.server_app, url_prefix='/api/server')
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.run()
