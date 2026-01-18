from flask import flask

app = flask(__name__)
@app.route('/')
def hola():
    return "<h1>¡Hola Byron Andres Angulo- practica docker!</h1>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)