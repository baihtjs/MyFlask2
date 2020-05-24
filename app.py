from flask import Flask

from App.views import blue

app = Flask(__name__)
app.register_blueprint(blueprint=blue)

@app.route('/hello')
def hello_world():
    return 'Hello Just!'



if __name__ == '__main__':
    app.run()
