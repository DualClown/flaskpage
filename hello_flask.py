from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Bienvenidos a Digitales 3"


if __name__ == "__main__":
    app.run(host='aqui va tu ip', port=80, debug=True)
