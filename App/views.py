from flask import Blueprint





blue=Blueprint('myfirstblue',__name__)

@blue.route('/')
def hello_world():
    return 'Hello World!'