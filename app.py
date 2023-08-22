from flask import Flask
from routes import User, Server
from routes.all import discord_all

# app = Flask(__name__)
app = discord_all()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    # app.register_blueprint(User.user_app, url_prefix='/api/user')
    # app.register_blueprint(Server.server_app, url_prefix='/api/server')
    app.run()
