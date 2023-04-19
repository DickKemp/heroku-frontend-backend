import os
from flask import Flask

def create_app():
    app = Flask(__name__, static_url_path='', static_folder='../frontend/build/static')

    return app

if __name__ == '__main__':

    app = create_app()
    app.run(port=5000)
