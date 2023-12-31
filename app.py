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
            "Add user on Server": "/api/server/<int:id_user>/add",
            "Server By user": "/api/server/user/<int:id_user>",
            "Server on User": "api/server/user/<int:id_user>/list",
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
            "Channel by id": "/api/channel/server/<int:id_server>",
            "Add Channel": "/api/channel/add",
            "Channel List": "/api/channel/list"
        },
        "Login User": {
            "Login": "/api/user/login",
            "Logout": "/api/user/logout",
            "Update Password": "/api/user/update/password/<int:id_user>"
        },
        "Message EndPoints": {
            "Message by id channel": "/api/message?<int:id_channel>",
            "Add Message": "/api/message/add",
            "Delete Message": "/api/message/delete/<int:id_message>",
            "Update Message": "/api/message/update/<int:id_message>",
            "Message by id": "/api/message/<int:id_message>"
        }

    }
    return data_response, 200


if __name__ == '__main__':
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.run(debug=True)
